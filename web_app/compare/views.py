import datetime
import io
import json
import os
import shutil
import zipfile
from django.conf import settings
import pandas as pd
import decimal
from decimal import Decimal

from compare.models import Ns, NsToModel, NsToAssumptions, MethodNs, AssumptionsNs, ModelNs, ConstrainNs, NameNs, RefNs
from compare.compare_utils import formatting_csv

from .graphs.generate_graph import plot_contours_from_h5
from .graphs.generate_multiple_graphs import plot_contours_from_checkboxes
from .graphs.extract_paths import extract_contour_number
from .graphs.data_processing import process_data_to_h5, create_temp_directory, remove_temp_directory, create_h5_directory

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.db.models import Q
from django.db.models import Count
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_user


def home(request):
    return render(request, "compare/home.html")


def keyword_filter(select_ns_prefiltered, all_keywords, keyword):
    # Get all the NS filenames from the pre-filtered NS list select_ns_all
    prefiltered_ns = []
    for ns in select_ns_prefiltered:
        prefiltered_ns.append(ns.filename)

    # We select the filenames that have the primary dependencies and the filenames of the prefiltered list
    kwd = all_keywords[keyword]
    if keyword == "list_dep_primary":
        tmp_select = NsToModel.objects.select_related().filter(Q(filename__in=prefiltered_ns) &
                                                               Q(id_model__dependenciesprimary__in=kwd))
    elif keyword == "list_dep_secondary":
        tmp_select = NsToModel.objects.select_related().filter(Q(filename__in=prefiltered_ns) &
                                                               Q(id_model__dependenciessecondary__in=kwd))
    elif keyword == "list_assumptions_primary":
        tmp_select = NsToAssumptions.objects.select_related().filter(Q(filename__in=prefiltered_ns) &
                                                                     Q(id_assumptions__assumptionsprimary__in=kwd))
    elif keyword == "list_assumptions_secondary":
        tmp_select = NsToAssumptions.objects.select_related().filter(Q(filename__in=prefiltered_ns) &
                                                                     Q(id_assumptions__assumptionssecondary__in=kwd))
    else:
        return select_ns_prefiltered

    # Get unique filenames from this selection
    temp_select_values = tmp_select.values_list('filename', flat=True).distinct()

    # We select the NS who have the filenames based on the selection above
    select_ns_filtered = Ns.objects.select_related().filter(filename__in=list(temp_select_values))

    return select_ns_filtered

def get_distinct_values(queryset, field_name):
    values_list = queryset.values_list(field_name, flat=True).order_by(field_name)
    distinct_values = []
    for value in values_list:
        if value not in distinct_values:
            distinct_values.append(value)
    return distinct_values

def get_sorted_distinct_values(queryset, field_name):
    values_list = queryset.values_list(field_name, flat=True)
    values_list_lower = list(values_list)
    sorted_values_lower = sorted(values_list_lower, key=lambda x: x.lower())
    distinct_values = []
    for value in sorted_values_lower:
        if value not in distinct_values:
            distinct_values.append(value)
    return [value for value in distinct_values]

def visu_data(request):

    # We select all the Ns from the database without models and assumptions but
    # with "ref" ,"name" ,"constrain" and "method" with method select_related
    select_ns_all = Ns.objects.select_related().all().order_by('filename')

    class_list = ["NS Spin", "Transiently_Accreting_NS", "NS Mass", "NS-NS mergers",
                  "PPM", "qLMXB", "Cold MSP", "Thermal INSs", "Type-I X-ray bursts"]

    for ns in select_ns_all:
        filepath = os.path.join(settings.STATIC_ROOT, 'static', 'h5', ns.h5_filename)
        if not os.path.exists(filepath):
            ns.file_exists = False
        else:
            ns.file_exists = True

    # We check for GET request
    if request.method == 'GET':

        # In case the user send a Get Request we extract the values
        # We recover the data sent in AJAX
        json_checklist = request.GET.get('dataCheckList', '')
        string_search = request.GET.get('dataSearch', '')
        dict_select = request.GET.get('dataSelect', '')
        bibtex_select = request.GET.get('bibtexfile')
        download_select = request.GET.get('filedwnl')

        # For the selection of files to download
        if download_select:
            to_download = json.loads(download_select)
            zip_buffer = io.BytesIO()

            with zipfile.ZipFile(zip_buffer, 'a', zipfile.ZIP_DEFLATED, False) as zip_file:
                # Add each downloaded file to the ZIP file folder
                for h5_filename in to_download:
                    filepath = os.path.join(settings.STATIC_ROOT, 'static', 'h5', h5_filename)
                    if os.path.exists(filepath):
                        zip_file.write(filepath, arcname=h5_filename)
                    else:
                        return HttpResponseNotFound(f"File not found: {h5_filename}")

                zip_file.printdir()

            # Return the ZIP file as an HTTP response
            zip_buffer.seek(0)
            response = HttpResponse(zip_buffer.getvalue(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="files.zip"'
            return response

        # For the selection of BibTex info to download
        if bibtex_select:
            # Convert JSON string to Python list
            list_bibtex = json.loads(bibtex_select)

            # Retrieve selected records
            selected_records = select_ns_all.filter(h5_filename__in=list_bibtex)

            # Retrieve the filenames from selected records
            file_names = [record.filename for record in selected_records]

            # Retrieve selected Bibtex information
            selected_bibtex = select_ns_all.filter(filename__in=file_names).values_list('id_ref__bibtex', flat=True)

            # Concatenate selected Bibtex
            bibtex_content = '\n\n'.join(selected_bibtex)

            # Return the Bibtex content as an HTTP response
            response = HttpResponse(bibtex_content, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename="Bibtex.txt"'
            return response

        # For 'string' searches with the search bar
        if string_search:
            # We run a query to search for the string on all database table (case-insensitive)
            select_ns_all = select_ns_all.filter(Q(id_name__namedb__icontains=string_search) |
                                                 Q(id_name__classdb__icontains=string_search) |
                                                 Q(id_method__method__icontains=string_search) |
                                                 Q(id_method__datadate__icontains=string_search) |
                                                 Q(id_method__processinfinfo__icontains=string_search) |
                                                 Q(id_constrain__constraintype__icontains=string_search) |
                                                 Q(id_constrain__constrainversion__icontains=string_search) |
                                                 Q(id_constrain__constrainvariable__icontains=string_search))

        # For the class selection with the left checkbox panel
        if json_checklist:
            # We retrieve the checkbox list via a JSON
            checkbox_list = json.loads(json_checklist)

            # For an empty checkbox list, we do as if all the checkboxes were checked
            if not checkbox_list:
                checkbox_list = class_list

            # We filter the NS from the database for which the ClassDB corresponds to the values in the checkbox list
            select_ns_all = select_ns_all.filter(id_name__classdb__in=checkbox_list)

        # For the keyword selection in the filter panel
        if dict_select:
            # We retrieve the keyword list via a JSON as a dictionary (key: selected box, value: selected item )
            keywords = json.loads(dict_select)

            # If keywords are selected, we filter based on the keyword list, from the pre-filtered NS list select_ns_all
            if keywords['list_methods']:
                select_ns_all = select_ns_all.filter(id_method__method__in=keywords['list_methods'])
            if keywords['list_variable']:
                select_ns_all = select_ns_all.filter(id_constrain__constrainvariable__in=keywords['list_variable'])
            if keywords['list_constrain_type']:
                select_ns_all = select_ns_all.filter(id_constrain__constraintype__in=keywords['list_constrain_type'])

            # For the model dependencies (primary)
            if keywords['list_dep_primary']:
                select_ns_all = keyword_filter(select_ns_all, keywords, 'list_dep_primary')

            # For the model dependencies (secondary)
            if keywords['list_dep_secondary']:
                select_ns_all = keyword_filter(select_ns_all, keywords, 'list_dep_secondary')

            # For the assumptions (primary)
            if keywords['list_assumptions_primary']:
                select_ns_all = keyword_filter(select_ns_all, keywords, 'list_assumptions_primary')

            # For the model dependencies (secondary)
            if keywords['list_assumptions_secondary']:
                select_ns_all = keyword_filter(select_ns_all, keywords, 'list_assumptions_secondary')

            # For the H5 file
            h5_filename_list = Ns.objects.filter(filename__in=[ns.filename for ns in select_ns_all]).values_list('h5_filename', flat=True)
            result_h5 = []

            for h5_filename in h5_filename_list:
                filepath_h5 = os.path.join(settings.STATIC_ROOT, 'static', 'h5', h5_filename)
                file_exists = os.path.exists(filepath_h5)
                result_h5.append(file_exists)

            # Once the filtering is done, we put the necessary info of selected NS (select_ns_all) in a filtered_list
            filtered_list = []
            for i, ns in enumerate(select_ns_all):
                # We put in the list only the attributes shown in the table into a dictionary
                ns_info = {'namedb': ns.id_name.namedb,
                           'filename': ns.filename,
                           'h5_filename': h5_filename_list[i],
                           'result_h5': result_h5[i],
                           'classdb': ns.id_name.classdb,
                           'method': ns.id_method.method,
                           'method_specific': ns.id_method.method_specific,
                           'constraintype': ns.id_constrain.constraintype,
                           'constrainversion': ns.id_constrain.constrainversion,
                           # TODO: Why is this converted to a string ?
                           'constrainvariable': str(ns.id_constrain.constrainvariable),
                           'doi': ns.id_ref.doi,
                           'author': ns.id_ref.author,
                           'year': ns.id_ref.refyear
                           }

                # We select the filenames linked to model dependencies and add all the model dependencies to a list
                select_ns_model = NsToModel.objects.select_related().filter(filename=ns.filename)
                list_model_dependencies, list_model_dependencies_primary, list_model_dependencies_secondary = [], [], []
                for snm in select_ns_model:
                    # We pre-format the string of model dependencies (prim. and sec.)
                    list_model_dependencies.append("<li><u>{}</u>: {}</li>".format(snm.id_model.dependenciesprimary,
                                                                                   snm.id_model.dependenciessecondary))
                    list_model_dependencies_primary.append(snm.id_model.dependenciesprimary)
                    list_model_dependencies_secondary.append(snm.id_model.dependenciessecondary)
                
                # Check if all the values in the list are None or "None".
                if all(val is None or val == "None" for val in list_model_dependencies_primary):
                    list_model_dependencies_primary = ["None"]

                if all(val is None or val == "None" for val in list_model_dependencies_secondary):
                    list_model_dependencies_secondary = ["None"]

                # The pre-formatted list is added to the dictionary
                ns_info['model'] = list_model_dependencies
                ns_info['modelprimary'] = list_model_dependencies_primary
                ns_info['modelsecondary'] = list_model_dependencies_secondary

                # We select the filenames linked to assumptions and add all the models to a list
                select_ns_ass = NsToAssumptions.objects.select_related().filter(filename=ns.filename)
                list_assumptions, list_assumptionsprimary, list_assumptionssecondary = [], [], []
                for snm in select_ns_ass:
                    # we get the assumption (prim. and sec.) and put it in a string and after the dictionary of the NS
                    list_assumptions.append("<li><u>{}</u>: {}</li>".format(snm.id_assumptions.assumptionsprimary,
                                                                            snm.id_assumptions.assumptionssecondary))
                    list_assumptionsprimary.append(snm.id_assumptions.assumptionsprimary)
                    list_assumptionssecondary.append(snm.id_assumptions.assumptionssecondary)

                # Check if all the values in the list are None or "None".
                if all(val is None or val == "None" for val in list_assumptionsprimary):
                    list_assumptionsprimary = ["None"]

                if all(val is None or val == "None" for val in list_assumptionssecondary):
                    list_assumptionssecondary = ["None"]

                # The pre-formatted list is added to the dictionary
                ns_info['assumptions'] = list_assumptions
                ns_info['assumptionsprimary'] = list_assumptionsprimary
                ns_info['assumptionssecondary'] = list_assumptionssecondary

                # We add the dictionary of the ns to the filtered_list of all ns
                filtered_list.append(ns_info)

            # We return the filtered_list of all ns back to the HTML
            return HttpResponse(json.dumps(filtered_list), content_type='application/json',)

        else:
            # We add the model dependencies, assumptions and files of all NS
            list_ns_model_dependencies = []
            list_ns_assumptions = []
            list_ns_files = []

            for ns in select_ns_all:
                # We make the file paths from the filenames (to be used by the django template)
                list_ns_files.append("h5/"+ns.h5_filename)

                # We select the filenames linked to models
                select_ns_model_dependencies = NsToModel.objects.select_related().filter(filename=ns.filename)
                # We select the filenames linked to assumptions
                select_ns_assumptions = NsToAssumptions.objects.select_related().filter(filename=ns.filename)

                # Store the dependencies as a tuple in a single list
                dependencies_list = []
                for s in select_ns_model_dependencies:
                    dependencies_list.append((s.id_model.dependenciesprimary, s.id_model.dependenciessecondary, s.id_model.dependenciesdescription, s.id_model.dependenciesreferences))
                list_ns_model_dependencies.append(dependencies_list)

                # Store the assumptions as a tuple in a single list
                assumptions_list = []
                for s in select_ns_assumptions:
                    assumptions_list.append((s.id_assumptions.assumptionsprimary, s.id_assumptions.assumptionssecondary))
                list_ns_assumptions.append(assumptions_list)

            # Zip all the data into a tuple
            select_ns_all_zip = zip(select_ns_all,
                                    list_ns_model_dependencies,
                                    list_ns_assumptions,
                                    list_ns_files,
                                    [ns.file_exists for ns in select_ns_all])
            
            # Sorted alphabetically + avoids redundancy
            orderMethodDistinct = get_sorted_distinct_values(MethodNs.objects, 'method')
            orderConstraintVariableDistinct = get_sorted_distinct_values(ConstrainNs.objects, 'constrainvariable')
            orderConstraintTypeDistinct = get_sorted_distinct_values(ConstrainNs.objects, 'constraintype')

            orderDepPrimaryDistinct = get_distinct_values(ModelNs.objects, 'dependenciesprimary')
            orderDepSecondaryDistinct = get_distinct_values(ModelNs.objects, 'dependenciessecondary')
            orderAssPrimaryDistinct = get_distinct_values(AssumptionsNs.objects, 'assumptionsprimary')
            orderAssSecondaryDistinct = get_distinct_values(AssumptionsNs.objects, 'assumptionssecondary')

            # We select the data that will appear in the table, and put into a dictionary
            select_all_ns = {"queryall": select_ns_all_zip,
                             "queryMeth": orderMethodDistinct,
                             "queryConV": orderConstraintVariableDistinct,
                             "queryConT": orderConstraintTypeDistinct,
                             "queryDep": orderDepPrimaryDistinct,
                             "queryDepS": orderDepSecondaryDistinct,
                             "queryAss": orderAssPrimaryDistinct,
                             "queryAssS": orderAssSecondaryDistinct,
                             }

            # Send the dictionary to the template
            return render(request, "compare/visu_data.html", select_all_ns)

def detail(request, id):

    # For deletion of entry (button "Remove" in details.html)
    if request.method == 'POST':
        filename = json.loads(request.POST.get('filename'))
        file = Ns.objects.get(filename=filename)

        logfile = open('compare/static/compare/log.txt', "a")
        wri = ['Delete:\n', 'User:', str(request.user.get_username())+'\n',
               'Date:', str(datetime.datetime.now())+'\n', 'Content:', str(file)+'\n\n']
        logfile.writelines(wri)
        logfile.close()

        # Removing the file from the database
        file.delete()
        return HttpResponse(json.dumps('yes'), content_type='application/json')

    # We retrieve all the data linked to the id(filename) of the NS in a query set
    ns_list = Ns.objects.select_related().get(filename=id)

    h5_filename = ns_list.h5_filename
    filepath_h5 = os.path.join(settings.STATIC_ROOT, 'static', 'h5', h5_filename)

    file_exists = os.path.exists(filepath_h5)

    contour_plot, subfolders_and_colors, alert_message = None, None, None
    extracted_contours = []

    if file_exists:
        contour_plot, unique_colors = plot_contours_from_h5(filepath_h5)

        contour_data = extract_contour_number(contour_plot)
        contour_data_list = contour_data.split(",") 
        number_elements = len(contour_data_list) 

        if number_elements > 1:
            extracted_contours.extend([contour.strip("'") for contour in contour_data.strip("[]").split(", ")])
            extracted_contours = [contour.replace('"', '') for contour in extracted_contours]
        else:
            extracted_contours = 1

        # Get subfolders in EOS folder & colors used in the plot
        eos_folder = os.path.join(settings.STATIC_ROOT, 'static', 'eos_radius_mass')
        subfolders = [subfolder for subfolder in os.listdir(eos_folder) if os.path.isdir(os.path.join(eos_folder, subfolder))]

        # Combine these two lists
        if len(unique_colors) > 0 and len(subfolders) > 0:
            subfolders_and_colors = zip(subfolders, unique_colors)
        else:
            subfolders_and_colors = 0
    else:
        alert_message = "The H5 file cannot be found. Impossible to generate graph."

    # We retrieve all the models dependencies linked to the id(filename) of the NS
    ns_model_dependencies = NsToModel.objects.select_related('id_model').filter(filename=id)

    # We retrieve all the assumptions linked to the id(filename) of the NS
    ns_assumptions = NsToAssumptions.objects.select_related('id_assumptions').filter(filename=id)

    # Trick to link to ADS page (need to replace the &, for ex in A&A)
    ns_list.id_ref.shortlink = ns_list.id_ref.short.replace("&", "%26")

    filepath = os.path.join(settings.STATIC_ROOT, 'static', 'h5', h5_filename)
    file_exists = os.path.exists(filepath)

    for mod in ns_model_dependencies:
        if mod.id_model.dependenciesreferences is not None:
            # Put the references in a list (and replace & by url code for links)
            mod.id_model.ref_list = zip(mod.id_model.dependenciesreferences.split(", "),
                                        mod.id_model.dependenciesreferences.replace("&", "%26").split(", "))
        else:
            mod.id_model.ref_list = None

    for ass in ns_assumptions:
        if ass.id_assumptions.assumptionsreferences is not None:
            # Put the references in a list (and replace & by url code for links)
            ass.id_assumptions.ref_list = zip(ass.id_assumptions.assumptionsreferences.split(", "),
                                              ass.id_assumptions.assumptionsreferences.replace("&", "%26").split(", "))
        else:
            ass.id_assumptions.ref_list = None

    # We put the query sets in a dictionary with the keys to display the data of the queryset in the template
    select = {"queryall": ns_list,
              "queryMo": ns_model_dependencies,
              "queryAs": ns_assumptions,
              "alert_message": alert_message,
              "file_exists": file_exists,
              "contour_plot": contour_plot,
              "filename": h5_filename,
              "extracted_contours": extracted_contours,
              "subfolders_and_colors": subfolders_and_colors}

    return render(request, 'compare/detail.html', select)

def generate_plot(request):
    if request.method == 'GET' and 'files[]' in request.GET:
        files = request.GET.getlist('files[]')

        html_graphs, h5_filepath_array, h5_filename_array, extracted_contours = [], [], [], []
        h5_filename_array_contours, h5_filename_array_errors = [], []
        
        for h5_filename in files:
            # H5 file recovery based on file name from the database
            ns_list = Ns.objects.select_related().get(h5_filename=h5_filename)
            h5_filename = ns_list.h5_filename
            filepath_h5 = os.path.join(settings.STATIC_ROOT, 'static', 'h5', h5_filename)
            
            # Check if the corresponding H5 file exists
            if os.path.exists(filepath_h5):
                h5_filepath_array.append(filepath_h5)
                h5_filename_array.append(h5_filename)
            else:
                alert_message = "The H5 file cannot be found. Impossible to generate graph." 

        for files in h5_filename_array:
            if "NS_Mass" in files and files.endswith("MeanErrors.h5"):
                h5_filename_array_errors.append(files)
            else:
                h5_filename_array_contours.append(files)

        if len(h5_filename_array_contours) == 0:
            h5_filename_array_contours = 0

        # If the table contains at least one element, plot the graph and extract the relevant information
        if len(h5_filepath_array) > 0:
            contour_plot_html, unique_colors_eos, unique_colors_errors = plot_contours_from_checkboxes(h5_filepath_array)
            html_graphs.append(contour_plot_html)

            contour_data = extract_contour_number(contour_plot_html)
            contour_data_list = contour_data.split(",") 
            number_elements = len(contour_data_list)

            if number_elements > 1:
                extracted_contours.extend([contour.strip("'") for contour in contour_data.strip("[]").split(", ")])
                extracted_contours = [contour.replace('"', '') for contour in extracted_contours]
            else:
                extracted_contours = 1

            # Get subfolders in EOS folder & colors used in the plot
            eos_folder = os.path.join(settings.STATIC_ROOT, 'static', 'eos_radius_mass')
            subfolders = [subfolder for subfolder in os.listdir(eos_folder) if os.path.isdir(os.path.join(eos_folder, subfolder))]

            # Get H5 error filenames
            if(len(h5_filename_array_errors) > 0 and len(unique_colors_errors) > 0): 
                errors_and_files = zip(h5_filename_array_errors, unique_colors_errors)
            else:
                errors_and_files = 0

            # Combine these two lists
            subfolders_and_colors = zip(subfolders, unique_colors_eos)
        else:
            return render(request, 'compare/plot.html', {'alert_message': alert_message})
        
        context = {'html_graphs': html_graphs[0],
                   'extracted_contours': extracted_contours,
                   'filenames_contours': h5_filename_array_contours,
                   'errors_and_files': errors_and_files,
                   'subfolders_and_colors': subfolders_and_colors}
        
        return render(request, 'compare/plot.html', context)

# TODO:  Next one to check and reformat
@login_required
def modify(request, id):

    ns_list = Ns.objects.select_related().get(filename=id)

    # We retrieve all the info related to the id(filename) of the NS
    ns_Mo = NsToModel.objects.select_related('id_model').filter(filename=id)
    ns_As = NsToAssumptions.objects.select_related('id_assumptions').filter(filename=id)
    name_file = Ns.objects.filter(id_name=ns_list.id_name)
    ref_file = Ns.objects.filter(id_ref=ns_list.id_ref)
    method_file = Ns.objects.filter(id_method=ns_list.id_method)
    constrain_file = Ns.objects.filter(id_constrain=ns_list.id_constrain)

    # We put in lists the filenames linked to this Model dependency and ti this assumption
    molist = []
    asslist = []
    for mo in ns_Mo:
        molist.append(ModelNs.objects.filter(id_model=mo.id_model.id_model))
    for ass in ns_As:
        asslist.append(AssumptionsNs.objects.filter(id_assumptions=ass.id_assumptions.id_assumptions))

    filemo = {}
    fileass = {}
    for m in molist:
        for i in m:
            filemo[i.id_model] = NsToModel.objects.filter(id_model=i.id_model)
    for a in asslist:
        for j in a:
            fileass[j.id_assumptions] = NsToAssumptions.objects.filter(id_assumptions=j.id_assumptions)

    # We get the value off the method enum in a list
    methodoptions = MethodNs.method.field.choices
    listmethod = []
    for mo in methodoptions:
        listmethod.append(mo[0])

    # We get the value off the constraintype enum in a list
    constrainoptions = ConstrainNs.constraintype.field.choices
    listconstrain = []
    for co in constrainoptions:
        listconstrain.append(co[0])

    # We get the value off the constraint variable enum in a list
    constrainvar = ConstrainNs.constrainvariable.field.choices
    listconstrainvar = []
    for cov in constrainvar:
        listconstrainvar.append(cov[0])


    # We check for Post request
    if request.method == 'POST':
        # We check what table the user want to modify
        if 'name' in request.POST:

            # We get all the field and verify if they are correct
            nameNS = NameNs.objects.get(id_name=ns_list.id_name.id_name)

            name = request.POST.get('namens')
            classNs = nameNS.classdb

            if len(name) <= 0 or len(classNs) <= 0:
                messages.error(request, "No")
            else:
                nameSin = request.POST.get('namesin')
                if (nameSin is not None) and (len(nameSin) < 1):
                    nameSin = None

                classSin = request.POST.get('classsin')
                if (classSin is not None) and (len(classSin) < 1):
                    classSin = None

                ra = request.POST.get('r')
                if (ra is not None) and (len(ra) > 1):
                    ra = Decimal(ra)
                else:
                    ra = None

                dec = request.POST.get('dec')
                if (dec is not None) and (len(dec) > 1):
                    dec = Decimal(dec)
                else:
                    dec = None

                loc = request.POST.get('localisation')
                if (loc is not None) and (len(loc) < 1):
                    loc = None

                event = request.POST.get('event')
                if (event is not None) and (len(event) < 1):
                    event = None

                # if the user clic on the update button we change the name of the ns
                if 'update' in request.POST:
                    nameNS.namedb = name
                    nameNS.classdb = classNs
                    nameNS.namesimbad = nameSin
                    nameNS.classsimbad = classSin
                    nameNS.ra = ra
                    nameNS.declination = dec
                    nameNS.localisationfile = loc
                    nameNS.eventdate = event
                    nameNS.save()
                    messages.success(request, "Yes")

                    #to write in the log file
                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Modify:\n', 'User:', str(request.user.get_username())+'\n',
                           'Date:', str(datetime.datetime.now())+'\n', 'Content:', str(nameNS)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

                # if the user clic on the add button
                elif 'add' in request.POST:
                    # We check if the name alreday exist  and linked it if it is the case
                    if (NameNs.objects.filter(namedb=name, classdb=classNs,
                                              namesimbad=nameSin, classsimbad=classSin,
                                              ra=ra,declination=dec,localisationfile=loc)):
                        nameExist = NameNs.objects.filter(namedb=name, classdb=classNs,
                                                          namesimbad=nameSin, classsimbad=classSin,
                                                          ra=ra, declination=dec, localisationfile=loc)
                        nameExist = nameExist[0]
                        ns_list.id_name = nameExist
                        ns_list.save()
                        messages.success(request, "jajajaja")
                    # we add the name
                    else:
                        nameAdd = NameNs(namedb=name, classdb=classNs,
                                         namesimbad=nameSin, classsimbad=classSin,
                                         ra=ra, declination=dec,
                                         localisationfile=loc, eventdate=event)
                        nameAdd.save()
                        ns_list.id_name = nameAdd
                        ns_list.save()
                        messages.success(request, "Yes")

                    #to write in the logo file
                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content: Name ', str(ns_list.id_name)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

            return redirect('modify', id)

        # We do the same things for all field of the table
        if 'ref' in request.POST:

            RefNS = RefNs.objects.get(id_ref=ns_list.id_ref.id_ref)
            auth = request.POST.get('author')
            year = request.POST.get('refyear')
            short = request.POST.get('short')
            bibtex = request.POST.get('bibtex')
            doi = request.POST.get('doi')

            if len(auth) <= 0 or len(year) <=0 or len(short) <=0 or len(bibtex) <=0 or len(doi) <=0:
                messages.error(request, "NO")
            else:
                repdoi = request.POST.get('repdoi')
                if (repdoi is not None) and (len(repdoi) < 1):
                    repdoi = None
                datal = request.POST.get('datalink')
                if (datal is not None) and (len(datal) < 1):
                    datal = None
                if datal == "None":
                    datal = None
                if 'update' in request.POST:
                    RefNS.author = auth
                    RefNS.refyear = year
                    RefNS.short = short
                    RefNS.bibtex = bibtex
                    RefNS.doi = doi
                    RefNS.repositorydoi = repdoi
                    RefNS.datalink = datal
                    RefNS.save()
                    messages.success(request, "Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Modify:\n', 'User:', str(request.user.get_username())+'\n',
                           'Date:', str(datetime.datetime.now())+'\n', 'Content:', str(RefNS)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

                elif 'add' in request.POST:
                    if RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex,
                                            doi=doi,repositorydoi=repdoi ,datalink=datal):
                        refExist = RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex,
                                                        doi=doi, repositorydoi=repdoi, datalink=datal)
                        refExist = refExist[0]
                        ns_list.id_ref = refExist
                        ns_list.save()
                        messages.success(request, "jojojojo")
                    else:
                        ref = RefNs(author=auth, refyear=year, short=short, bibtex=bibtex,
                                    doi=doi, repositorydoi=repdoi, atalink=datal)
                        ref.save()
                        ns_list.id_ref = ref
                        ns_list.save()
                        messages.success(request,"Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content: Ref ', str(ns_list.id_ref)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

            return redirect('modify', id)

        if 'method' in request.POST:
            MethNS = MethodNs.objects.get(id_method=ns_list.id_method.id_method)
            meth = request.POST.get('methodns')
            methS = request.POST.get('methodspe')
            datad = request.POST.get('datadate')
            proceInfo = request.POST.get('processinfinfo')

            if len(meth) <= 0 or len(methS) <= 0 or len(datad) <= 0 or len(proceInfo) <= 0:
                messages.error(request, "Method to insert is not valid")
            else:
                if 'update' in request.POST:
                    MethNS.method = meth
                    MethNS.method_specific = methS
                    MethNS.datadate = datad
                    MethNS.processinfinfo = proceInfo
                    MethNS.save()
                    messages.success(request, "Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Modify:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content:', str(MethNS)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

                elif 'add' in request.POST:
                    if MethodNs.objects.filter(method=meth, method_specific=methS,
                                               datadate=datad, processinfinfo=proceInfo):
                        methodExist = MethodNs.objects.filter(method=meth, method_specific=methS,
                                                              datadate=datad,processinfinfo =proceInfo)
                        methodExist = methodExist[0]
                        ns_list.id_method = methodExist
                        ns_list.save()
                        messages.success(request, "Yes")
                    else:
                        method = MethodNs(method=meth, method_specific=methS,
                                          atadate=datad, processinfinfo=proceInfo)
                        method.save()
                        ns_list.id_method = method
                        ns_list.save()
                        messages.success(request, "Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content:Method ', str(ns_list.id_method)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

            return redirect('modify', id)

        if 'constrain' in request.POST:

            Constrainns = ConstrainNs.objects.get(id_constrain=ns_list.id_constrain.id_constrain)
            constrainT = request.POST.get('constrainT')
            constrainV = request.POST.get('constrainV')
            constrainVar = request.POST.get('constrainVar')

            if len(constrainT) <= 0 or len(constrainV) <= 0 or len(constrainVar) <= 0:
                messages.error(request, "Constrain Variable to insert is not valid")
            else:
                if 'update' in request.POST:
                    Constrainns.constraintype = constrainT
                    Constrainns.constrainvariable = constrainVar
                    Constrainns.constrainversion = constrainV
                    Constrainns.save()

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content: ', str(Constrainns)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

                    messages.success(request,"Yes")

                elif 'add' in request.POST:
                    if ConstrainNs.objects.filter(constraintype=constrainT,
                                                  constrainvariable=constrainVar,
                                                  constrainversion=int(constrainV)):
                        constrainExist = ConstrainNs.objects.filter(constraintype=constrainT,
                                                                    constrainvariable=constrainVar,
                                                                    constrainversion=int(constrainV))
                        constrainExist = constrainExist[0]
                        ns_list.id_constrain = constrainExist
                        ns_list.save()
                        messages.success(request, "Yes")

                    else:
                        constrain = ConstrainNs(constraintype=constrainT,
                                                constrainvariable=constrainVar,
                                                constrainversion=constrainV)
                        constrain.save()
                        ns_list.id_constrain = constrain
                        ns_list.save()
                        messages.success(request, "Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content: ', str(ns_list.id_constrain)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

            return redirect('modify', id)

        if 'model' in request.POST:

            model = ModelNs.objects.get(id_model=request.POST.get('model'))
            depP = request.POST.get('dependenciesprimary')
            depS = request.POST.get('dependenciessecondary')
            depD = request.POST.get('dependenciesdescription')
            depR = request.POST.get('dependenciesreferences')

            if len(depP) < 1:
                depP = None

            if len(depS) < 1:
                depS = None

            if len(depD) < 1:
                depD = None

            if len(depR) < 1:
                depR = None

            # TODO: CHECK THIS ELSE 'ALONE' HERE
            else:
                if 'update' in request.POST:
                    model.dependenciesprimary = depP
                    model.dependenciessecondary = depS
                    model.dependenciesdescription = depD
                    model.dependenciesreferences = depR
                    model.save()
                    messages.success(request,"Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Modify:\n', 'User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', 'Content:', str(model)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

                elif 'add' in request.POST:
                    if(ModelNs.objects.filter(dependenciesprimary=depP,
                                              dependenciessecondary=depS,
                                              dependenciesdescription=depD,
                                              dependenciesreferences=depR)):
                        modelExist = ModelNs.objects.filter(dependenciesprimary=depP,
                                                            dependenciessecondary=depS,
                                                            dependenciesdescription=depD,
                                                            dependenciesreferences=depR)
                        modelExist = modelExist[0]
                        model.id_model = modelExist
                        model.save()

                    else:
                        model = ModelNs(dependenciesprimary=depP,
                                        dependenciessecondary=depS,
                                        dependenciesdescription=depD,
                                        dependenciesreferences=depR)
                        model.save()
                        messages.success(request,"Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username())+'\n',
                           'Date:',str(datetime.datetime.now())+'\n', 'Content: ', str(model)+'\n\n']
                    logfile.writelines(wri)
                    logfile.close()

            return redirect('modify', id)

        if 'assumption' in request.POST:

            assumption = AssumptionsNs.objects.get(id_assumptions=request.POST.get('assumption'))
            AssP = request.POST.get('assumptionsprimary')
            AssS = request.POST.get('assumptionssecondary')
            AssD = request.POST.get('assumptionsdescription')
            AssR = request.POST.get('assumptionsreferences')

            if len(AssP) < 1:
                AssP = None

            if len(AssS) < 1:
                AssS = None

            if len(AssD) < 1:
                AssD = None

            if len(AssR) < 1:
                AssR = None

            # TODO: CHECK THIS ELSE 'ALONE' HERE
            else:
                if 'update' in request.POST:
                    assumption.assumptionsprimary = AssP
                    assumption.assumptionssecondary = AssS
                    assumption.assumptionsdescription = AssD
                    assumption.assumptionsreferences = AssR
                    assumption.save()
                    messages.success(request,"Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Modify:\n', 'User:', str(request.user.get_username()) + '\n', 'Date:',
                           str(datetime.datetime.now()) + '\n', 'Content:', str(assumption) + '\n\n']
                    logfile.writelines(wri)
                    logfile.close()

                elif 'add' in request.POST:
                    if(AssumptionsNs.objects.filter(assumptionsprimary=AssP,
                                                    assumptionssecondary=AssS,
                                                    assumptionsdescription=AssD,
                                                    assumptionsreferences=AssR)):

                        assumptionExist = AssumptionsNs.objects.filter(assumptionsprimary=AssP,
                                                                       assumptionssecondary=AssS,
                                                                       assumptionsdescription=AssD,
                                                                       assumptionsreferences=AssR)
                        assumptionExist = assumptionExist[0]
                        assumption.id_assumptions = assumptionExist
                        assumption.save()
                    else:
                        assumption = AssumptionsNs(assumptionsprimary=AssP,
                                                   assumptionssecondary=AssS,
                                                   assumptionsdescription=AssD,
                                                   assumptionsreferences=AssR)
                        assumption.save()
                        messages.success(request,"Yes")

                    logfile = open('compare/static/compare/log.txt', "a")
                    wri = ['Add:\n', 'User:', str(request.user.get_username()) + '\n', 'Date:',
                           str(datetime.datetime.now()) + '\n', 'Content:Assumptions ', str(assumption) + '\n\n']
                    logfile.writelines(wri)
                    logfile.close()

            return redirect('modify', id)

    # We put in a dictionary the querysets with a key to display in the template modify.html
    select = {"queryall": ns_list,
              "queryMo": ns_Mo,
              "queryAs": ns_As,
              "queryName": name_file,
              "queryRef": ref_file,
              "queryMethod": method_file,
              "queryConstrain": constrain_file,
              "queryModel": molist,
              "queryAssumption": asslist,
              "queryModellinked": filemo,
              "queryAssumptionlinked": fileass,
              "listmethod": listmethod,
              "listconstrain": listconstrain,
              "listconstrainvar": listconstrainvar}

    return render(request, "compare/modify.html", select)


def login(request):
    # We check if a POST request is send
    if request.method == 'POST':
        # We get the username and the password of the inputs fields
        username = request.POST['username']
        psw = request.POST['password']

        # We check if the username and the password are of a user
        user = authenticate(username=username, password=psw)
        if user is not None:
            # We logged in the user and redirect to the Add page
            auth_login(request, user)
            return redirect('insert')
        else:
            # We send an error message
            messages.success(request, "Incorrect Username or Password")
            return redirect('login')
    else:
        return render(request, "compare/login.html")


def logout(request):
    # We log out and redirect to the data table page
    logout_user(request)
    return redirect('visu')


@login_required
def insert_data(request):

    # We check if a Get request is sent from the user (get for the selectlist for nama and ref)
    if request.method == 'GET':
        idName = request.GET.get('idname', '')
        idRef = request.GET.get('idref', '')

        # We get the id of the name selected and select the information of this name
        if idName:
            queryTabName = NameNs.objects.filter(pk=idName)
            querylistName = list(queryTabName.values())
            jsonName = json.dumps(querylistName, default=str)
            return HttpResponse(jsonName, content_type='application/json',)

        # We get the id of the ref selected and select the information of this ref
        if idRef:
            queryTabRef = RefNs.objects.filter(pk=idRef)
            querylistRef = list(queryTabRef.values())
            jsonRef = json.dumps(querylistRef, default=str)
            return HttpResponse(jsonRef, content_type='application/json',)

    # We check if it is a Post request
    if request.method == 'POST':

        # We check if ist a file send
        if 'myfile' in request.FILES:
            if request.FILES['myfile']:
                input_csv_filename = request.FILES['myfile']
                # We put in a dataframe the value of the file
                d= pd.DataFrame(pd.read_csv(input_csv_filename))
                d = formatting_csv(d)

                # List with type of sources
                NsClass = ["NS spin", "Transiently_Accreting_NS", "NS mass", "NS-NS mergers",
                           "PPM", "qLMXB", "Cold MSP", "Thermal INSs", "Type-I X-ray bursts"]

                # We get the enum types in lists
                me = []
                for m in MethodNs.method.field.choices:
                    me.append(m[0])

                ct = []
                for c in ConstrainNs.constraintype.field.choices:
                    ct.append(c[0])

                cv = []
                for v in ConstrainNs.constrainvariable.field.choices:
                    cv.append(v[0])

                to_insert = 0
                inserted = []
                not_inserted = {}

                # Loop on all rows of the Panda DataFrame
                for i in range(1, len(d)+1):

                    # Model dependencies and assumptions are places in lists
                    filename = d['FileName'][i]

                    h5filename = d['H5FileName'][i]

                    listmo = d['ModelDependenciesPrimary'][i].split(",")

                    listmosec = d['ModelDependenciesSecondary'][i].split(",")

                    listmodesc = d['ModelDependencyDescription'][i].split("\n")
                    listmodesc = [i for i in listmodesc if i]
                    if len(listmodesc) == 0:
                        listmodesc = ['']  # Just a hack to avoid an empty list if there are no description provided

                    listmodepref = d['ModelDependencyReferences'][i].split("\n")
                    listmodepref = [i for i in listmodepref if i]
                    if len(listmodepref) == 0:
                        listmodepref = ['']  # Just a hack to avoid an empty list if there are no description provided

                    listass = d['AssumptionsPrimary'][i].split(",")

                    listasssec = d['AssumptionsSecondary'][i].split(",")

                    listassdesc = d['AssumptionsDescription'][i].split("\n")
                    listassdesc = [i for i in listassdesc if i]
                    if len(listassdesc) == 0:
                        listassdesc = ['']  # Just a hack to avoid an empty list if there are no description provided

                    listassref = d['AssumptionsReferences'][i].split("\n")
                    listassref = [i for i in listassref if i]
                    if len(listassref) == 0:
                        listassref = ['']  # Just a hack to avoid an empty list if there are no description provided

                    # Check if the filename exists
                    if Ns.objects.filter(filename=d['FileName'][i]):
                        not_inserted[filename] = "already in"
                        continue

                    # Check the non-null field
                    elif ((len(d['NameDB'][i]) <= 0 or
                           len(d['ClassDB'][i]) <= 0 or
                           len(d['Method'][i]) <= 0) or
                          (len(d['MethodSpecific'][i]) <= 0) or
                          (len(d['DataDate'][i]) <= 0) or
                          (len(d['ProcessingInfo'][i]) <= 0) or
                          (len(d['ConstrainVariable'][i]) <= 0) or
                          (len(d['ConstrainType'][i]) <= 0) or
                          (len(d['Ref1stAuthor'][i]) <= 0) or
                          (len(d['RefYear'][i]) <= 0) or
                          (len(d['RefShort'][i]) <= 0) or
                          # (len(d['RefBibtex'][i])<=0) or
                          (len(d['RefDOI'][i]) <=0)):
                        not_inserted[filename] = "missing mandatory elements"
                        continue

                    # Various verifications...
                    elif((len(listmo) != len(listmosec)) or
                         (len(listmo) != len(listmodesc)) or
                         (len(listmo) != len(listmodepref))):
                        not_inserted[filename] = "mismatch in input model dependencies: " \
                                                 "{} primary, {} secondary, {} descriptions, " \
                                                 "and {} references".format(len(listmo),
                                                                            len(listmosec),
                                                                            len(listmodesc),
                                                                            len(listassref))
                        continue

                    elif((len(listass) != len(listasssec)) or
                         (len(listass) != len(listassdesc)) or
                         (len(listass) != len(listassdesc))):
                        not_inserted[filename] = "has a mismatch in input assumptions " \
                                                 "{} primary, {} secondary, {} descriptions, " \
                                                 "and {} references".format(len(listass),
                                                                            len(listasssec),
                                                                            len(listassdesc),
                                                                            len(listassdesc))
                        continue

                    elif str(d['Method'][i]) not in me:
                        not_inserted[filename] = "{} is not a valid method - choices: {}".format(d['Method'][i], me)
                        continue

                    elif d['ConstrainType'][i] not in ct:
                        not_inserted[filename] = "{} is not a valid constrain type - choices: {}".format(d['ConstrainType'][i], ct)
                        continue

                    elif d['ConstrainVariable'][i] not in cv:
                        not_inserted[filename] = "{} is not a valid constrain variable - choices: {}".format(d['ConstrainVariable'][i], cv)
                        continue

                    elif d['ClassDB'][i] not in NsClass:
                        not_inserted[filename] = "{} is not a valid name class - choices: {}".format(d['ClassDB'][i], NsClass)
                        continue

                    elif len(d['RA'][i]) > 1:
                        try:
                            Decimal(d['RA'][i])
                        except decimal.InvalidOperation:
                            not_inserted[filename] = "{} can not be a converted to decimal".format(d['RA'][i])
                            continue

                    elif len(d['DEC'][i]) > 1:
                        try:
                            Decimal(d['DEC'][i])
                        except decimal.InvalidOperation:
                            not_inserted[filename] = "{} can not be a converted to decimal".format(d['DEC'][i])
                            continue

                    elif len(d['RefYear'][i]) > 1:
                        try:
                            int(d['RefYear'][i])
                        except ValueError:
                            not_inserted[filename] = "{} can not be a converted to integer".format(d['RefYear'][i])
                            continue

                    # We retrieve get the value of the name
                    namen = d['NameDB'][i]
                    classn = d['ClassDB'][i]
                    nameS = d['NameSimbad'][i]
                    classS = d['ClassSimbad'][i]
                    r = d['RA'][i]
                    dec = d['DEC'][i]
                    dat = d['EventDate'][i]
                    loc = d['LocalisationFile'][i]

                    # Verifications in case
                    if len(nameS) < 1:
                        nameS = None

                    if len(classS) < 1:
                        classS = None

                    if len(r)>1:
                        r = Decimal(r)
                    else:
                        r = None

                    if len(dec) > 1:
                        dec = Decimal(dec)
                    else:
                        dec = None

                    if len(loc) < 1:
                        loc = None

                    if len(dat) < 1:
                        dat = None

                    # if the name alreday exist we select it
                    if (NameNs.objects.filter(namedb=namen, classdb=classn, namesimbad=nameS, classsimbad=classS,
                                              ra=r, declination=dec, localisationfile=loc)):
                        idN = NameNs.objects.filter(namedb=namen, classdb=classn, namesimbad=nameS, classsimbad=classS,
                                                    ra=r, declination=dec, localisationfile=loc)
                        idN= idN[0]
                    # else We add the new name
                    else:
                        name = NameNs(namedb=namen, classdb=classn, namesimbad=nameS, classsimbad=classS,
                                      ra=r, declination=dec, localisationfile=loc, eventdate=dat)
                        name.save()
                        idN = NameNs.objects.latest('id_name') # we store the object that we insert to link it after

                    # We do the same for the other columns of the dataframe

                    methodN = d['Method'][i]
                    methodS = d['MethodSpecific'][i]
                    dDate = d['DataDate'][i]
                    ProcInfo = d['ProcessingInfo'][i]

                    if (MethodNs.objects.filter(method=methodN, method_specific=methodS,
                                                datadate=dDate, processinfinfo=ProcInfo)):
                        idM = MethodNs.objects.filter(method=methodN, method_specific=methodS,
                                                      datadate=dDate,processinfinfo=ProcInfo)
                        idM = idM[0]
                    else:
                        method = MethodNs(method=methodN, method_specific=methodS,
                                          datadate=dDate, processinfinfo=ProcInfo)
                        method.save()
                        idM = MethodNs.objects.latest('id_method')

                    consV = d['ConstrainVariable'][i]
                    consT  =d['ConstrainType'][i]

                    # TODO: Add check that constrain version is an integer
                    consVe = d['ConstrainVersion'][i]

                    if ConstrainNs.objects.filter(constraintype=consT,
                                                  constrainvariable=consV,
                                                  constrainversion=int(consVe)):
                        idC = ConstrainNs.objects.filter(constraintype=consT,
                                                         constrainvariable=consV,
                                                         constrainversion=int(consVe))
                        idC = idC[0]
                    else:
                        constrain=ConstrainNs(constraintype =consT,
                                              constrainvariable=consV,
                                              constrainversion=int(consVe))
                        constrain.save()
                        idC = ConstrainNs.objects.latest('id_constrain')

                    auth = d['Ref1stAuthor'][i]
                    year = d['RefYear'][i]
                    short = d['RefShort'][i]
                    bibtex = d['RefBibtex'][i]
                    doi = d['RefDOI'][i]
                    repdoi = d['DataRepositoryDOI'][i]
                    datal = d['DataLink'][i]

                    if len(repdoi) < 1:
                        repdoi = None

                    if len(datal) < 1:
                        datal = None

                    if RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex,
                                            doi=doi,repositorydoi=repdoi ,datalink=datal):
                        idR = RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex,
                                                   doi=doi, repositorydoi=repdoi, datalink=datal)
                        idR = idR[0]
                    else:
                        ref = RefNs(author=auth, refyear=year, short=short, bibtex=bibtex,
                                    doi=doi, repositorydoi=repdoi, datalink=datal)
                        ref.save()
                        idR = RefNs.objects.latest('id_ref')


                    # we create the new NS
                    file = Ns(filename=filename,
                              h5_filename=h5filename,
                              id_ref=idR, id_name=idN,
                              id_method=idM, id_constrain=idC
                              )
                    file.save()
                    # we store the ns for the assumptions and models
                    nsInstance = Ns.objects.get(filename=filename)

                    for j in range(len(listmo)):
                        modelpri = listmo[j]
                        modelsec = listmosec[j]
                        modeldesc = listmodesc[j]
                        modelref = listmodepref[j]

                        if len(modelpri) < 1:
                            modelpri = None

                        if len(modelsec) < 1:
                            modelsec = None

                        if len(modeldesc) < 1:
                            modeldesc = None

                        if len(modelref) < 1:
                            modelref = None

                        if(ModelNs.objects.filter(dependenciesprimary=modelpri,
                                                  dependenciessecondary=modelsec,
                                                  dependenciesdescription=modeldesc,
                                                  dependenciesreferences=modelref)):
                            idMo = ModelNs.objects.filter(dependenciesprimary=modelpri,
                                                          dependenciessecondary=modelsec,
                                                          dependenciesdescription=modeldesc,
                                                          dependenciesreferences=modelref)
                            idMo = idMo[0]
                        else:
                            modelN = ModelNs(dependenciesprimary=modelpri,
                                             dependenciessecondary=modelsec,
                                             dependenciesdescription=modeldesc,
                                             dependenciesreferences=modelref)
                            modelN.save()
                            idMo = ModelNs.objects.latest('id_model')
                        # We create the link between ns and model
                        nsmodel = NsToModel(filename=nsInstance, id_model=idMo)
                        nsmodel.save()

                    for k in range(len(listass)):

                        asspri = listass[k]
                        asssec = listasssec[k]
                        assdesc = listassdesc[k]
                        assref = listassref[k]

                        if len(asspri)<1:
                            asspri = None

                        if len(asssec)<1:
                            asssec = None

                        if len(assdesc)<1:
                            assdesc = None

                        if len(assref) < 1:
                            assref = None

                        if(AssumptionsNs.objects.filter(assumptionsprimary=asspri,
                                                        assumptionssecondary=asssec,
                                                        assumptionsdescription=assdesc,
                                                        assumptionsreferences=assref)):
                            idAs = AssumptionsNs.objects.filter(assumptionsprimary=asspri,
                                                                assumptionssecondary=asssec,
                                                                assumptionsdescription=assdesc,
                                                                assumptionsreferences=assref)
                            idAs=idAs[0]
                        else:
                            assumptions = AssumptionsNs(assumptionsprimary=asspri,
                                                        assumptionssecondary=asssec,
                                                        assumptionsdescription=assdesc,
                                                        assumptionsreferences=assref)
                            assumptions.save()
                            idAs = AssumptionsNs.objects.latest('id_assumptions')

                        # We create the link between ns and assumptions
                        nsass = NsToAssumptions(filename=nsInstance, id_assumptions=idAs)
                        nsass.save()
                    to_insert += 1
                    inserted.append(filename)

                # Message for the user
                mes = "You inserted {} out of {} elements".format(to_insert, len(d))
                messages.success(request, mes)

                if len(inserted) != 0:
                    mes2 = "Element(s) inserted:  {}".format(", ".join(["{}".format(i) for i in inserted]))
                    messages.success(request, mes2)

                if len(not_inserted) != 0:
                    mes3 = "Some element were not inserted:  "
                    for not_in in not_inserted:
                        mes3 += "{} ({})  -  ".format(not_in, not_inserted[not_in])
                    messages.success(request, mes3)

    if (request.FILES.get('filetoload')):

        # We get the name of the file
        datafile = request.FILES['filetoload']

        if datafile:

            # Check file format
            if not datafile.name.endswith(('.txt', '.npy')):
                message = "The file format must be .txt or .npy."
                return HttpResponse(json.dumps(message), content_type='application/json',)

            # Recover file name without extension
            message = os.path.splitext(datafile.name)[0]

            # Check file name without extension
            valid_names = ["MCMCSamples", "ProbaDistrib", "Quantiles", "MeanErrors", "PosteriorSamples", "Contours"]
            if not any(message.endswith(name) for name in valid_names):
                message = "The file does not have the correct nomenclature."
                return HttpResponse(json.dumps(message), content_type='application/json',)

            create_temp_directory()

            destination_path = os.path.join(settings.STATIC_ROOT, 'temp', datafile.name)
            check_path = os.path.join(settings.STATIC_ROOT, 'static', 'data')

            # Get the list of files in the check_path directory
            files_in_check_path = os.listdir(check_path)

            # Check if datafile.name exists in the files_in_check_path list
            if datafile.name in files_in_check_path:
                message = "The file already exists."
                return HttpResponse(json.dumps(message), content_type='application/json',)

            with open(destination_path, 'wb+') as destination:
                for chunk in datafile.chunks():
                    destination.write(chunk)

            # Call the process_data_to_h5 function with the full file path
            process_data_to_h5(destination_path)

    # for insertion manual we check what the user wants to insert
    if (request.POST.get('hid') == 'formAddName' ):

        # verifications of the value
        na = request.POST.get('name')
        classdb = request.POST.get('class')

        if len(na) <= 0 or len(classdb) <= 0:
            messages.error(request, "Name insertion not correct")
        else:
            nameS = request.POST.get('nameS')
            if len(nameS) < 1:
                nameS = None

            classS = request.POST.get('classS')
            if len(classS) < 1:
                classS = None

            r = request.POST.get('ra')
            if len(r) > 1:
                r = Decimal(r)
            else:
                r = None

            dec = request.POST.get('dec')
            if len(dec)>1:
                dec = Decimal(dec)
            else:
                dec = None

            loc = request.POST.get('localisationfile')
            if len(loc) < 1:
                loc = None

            dat = request.POST.get('eventdate')
            if len(dat) < 1:
                dat = None

            if NameNs.objects.filter(namedb=na, classdb=classdb, namesimbad=nameS, classsimbad=classS,
                                        ra=r, declination=dec, localisationfile=loc, eventdate=dat):
                mess = "Name already exists"
                messages.error(request,"Name already exists")
            else:
                # We create the new name
                name = NameNs(namedb=na, classdb=classdb, namesimbad=nameS, classsimbad=classS,
                                ra=r, declination=dec, localisationfile=loc, eventdate=dat)
                name.save()

                #to write in the log file
                fichierlog = open('compare/static/compare/log.txt', "a")
                wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                        str(datetime.datetime.now())+'\n', 'Content:', str(name)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

    # same things for ref
    if (request.POST.get('hid') == 'formAddRef' ):

        auth = request.POST.get('author')
        year = request.POST.get('refyear')
        short = request.POST.get('short')
        bibtex = request.POST.get('bibtex')
        doi = request.POST.get('doi')

        if len(auth) <= 0 or len(year) <= 0 or len(short) <= 0 or len(bibtex) <= 0 or len(doi) <= 0:
            messages.error(request,"Ref insertion not correct")
        else:
            repdoi = request.POST.get('repositorydoi')
            if len(repdoi) < 1:
                repdoi = None

            datal = request.POST.get('datalink')
            if len(datal) < 1:
                datal = None

            if RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex,
                                    doi=doi, repositorydoi=repdoi, datalink=datal):
                messages.error(request,"Ref already exists")
            else:
                ref = RefNs(author=auth, refyear=year, short=short, bibtex=bibtex,
                            doi=doi, repositorydoi=repdoi, datalink=datal)
                ref.save()

                fichierlog = open('compare/static/compare/log.txt', "a")
                wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                       str(datetime.datetime.now())+'\n', 'Content:', str(ref)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

    # When the user validates the insertion
    if (request.POST.get('insert')):

        # We verify all the values
        insert = json.loads(request.POST.get('insert'))

        # TODO:  Fix these conditions:  for ex with:   insert['filename'] is ''
        if (len(insert['filename']) <= 0):
            mess = "ERROR : Please enter a Filename"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif (insert['name'] == "opt") or (insert['ref']== 'opt'):
            mess = "ERROR : Please select a Name or/and a Ref"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif (len(insert['method']['methodS']) <= 0) or \
             (len(insert['method']['methodD']) <=0 ) or \
             (len(insert['method']['methodP']) <=0 ):
            mess = "ERROR : Please enter a valid Method"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif len(insert['constrain']['constrainVer']) <= 0:
            mess = "ERROR : Please enter a valid Constrain"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        else:
            ref = RefNs.objects.get(id_ref=insert['ref'])
            name = NameNs.objects.get(id_name=insert['name'])

            # We check if method and constrain already exist
            if MethodNs.objects.filter(method=insert['method']['methodN'],
                                       method_specific=insert['method']['methodS'],
                                       datadate=insert['method']['methodD'],
                                       processinfinfo=insert['method']['methodP']):

                methodId = MethodNs.objects.filter(method=insert['method']['methodN'],
                                                   method_specific=insert['method']['methodS'],
                                                   datadate=insert['method']['methodD'],
                                                   processinfinfo=insert['method']['methodP'])
            else:
                method = MethodNs(method=insert['method']['methodN'],
                                  method_specific=insert['method']['methodS'],
                                  datadate=insert['method']['methodD'],
                                  processinfinfo=insert['method']['methodP'])
                method.save()
                methodId = MethodNs.objects.latest('id_method')

                fichierlog = open('compare/static/compare/log.txt', "a")
                wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                       str(datetime.datetime.now())+'\n', str(method)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

            if ConstrainNs.objects.filter(constraintype=insert['constrain']['constrainT'],
                                          constrainvariable=insert['constrain']['constrainV'],
                                          constrainversion=insert['constrain']['constrainVer']):

                constrainId = ConstrainNs.objects.filter(constraintype=insert['constrain']['constrainT'],
                                                         constrainvariable=insert['constrain']['constrainV'],
                                                         constrainversion=insert['constrain']['constrainVer'])
            else:
                constrain = ConstrainNs(constraintype=insert['constrain']['constrainT'],
                                        constrainvariable=insert['constrain']['constrainV'],
                                        constrainversion=insert['constrain']['constrainVer'])
                constrain.save()
                constrainId = ConstrainNs.objects.latest('id_constrain')

                fichierlog = open('compare/static/compare/log.txt', "a")
                wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                       str(datetime.datetime.now())+'\n', str(constrain)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

            # We create the new ns with all the field
            ns = Ns(filename=insert['filename'], h5_filename=insert['h5filename'],
                    id_ref=ref, id_name=name,
                    id_method=methodId, id_constrain=constrainId)
            ns.save()

        if len(insert['model']) > 0:

            ns = Ns.objects.get(filename=insert['filename'])
            # for all the model we verify the value and create the object ,
            # if already exist we linked it, same as the others
            for mod in insert['model']:

                if len(insert['model'][mod][0]) < 1:
                    insert['model'][mod][0] = None

                if len(insert['model'][mod][1]) < 1:
                    insert['model'][mod][1] = None

                if len(insert['model'][mod][2]) < 1:
                    insert['model'][mod][2] = None

                if len(insert['model'][mod][3]) < 1:
                    insert['model'][mod][3] = None

                if (ModelNs.objects.filter(dependenciesprimary=insert['model'][mod][0],
                                           dependenciessecondary=insert['model'][mod][1],
                                           dependenciesdescription=insert['model'][mod][2],
                                           dependenciesreferences=insert['model'][mod][3])):

                    modelId = ModelNs.objects.filter(dependenciesprimary=insert['model'][mod][0],
                                                     dependenciessecondary=insert['model'][mod][1],
                                                     dependenciesdescription=insert['model'][mod][2],
                                                     dependenciesreferences=insert['model'][mod][3])
                else:

                    model = ModelNs(dependenciesprimary=insert['model'][mod][0],
                                    dependenciessecondary=insert['model'][mod][1],
                                    dependenciesdescription=insert['model'][mod][2],
                                    dependenciesreferences=insert['model'][mod][3])
                    model.save()
                    modelId = ModelNs.objects.latest('id_model')

                    fichierlog = open('compare/static/compare/log.txt', "a")
                    wri = ['User:', str(request.user.get_username())+'\n',
                           'Date:', str(datetime.datetime.now())+'\n', str(model)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                nsmodel = NsToModel(filename=ns, id_model=modelId)
                nsmodel.save()

        if len(insert['assumptions']) > 0:

            ns = Ns.objects.get(filename=insert['filename'])
            # Same for assumptions
            for ass in insert['assumptions']:

                if len(insert['assumptions'][ass][0]) < 1:
                    insert['assumptions'][ass][0] = None

                if len(insert['assumptions'][ass][1]) < 1:
                    insert['assumptions'][ass][1] = None

                if len(insert['assumptions'][ass][2]) < 1:
                    insert['assumptions'][ass][2] = None

                if len(insert['assumptions'][ass][3]) < 1:
                    insert['assumptions'][ass][3] = None

                if (AssumptionsNs.objects.filter(assumptionsprimary=insert['assumptions'][ass][0],
                                                 assumptionssecondary=insert['assumptions'][ass][1],
                                                 assumptionsdescription=insert['assumptions'][ass][2],
                                                 assumptionsreferences=insert['assumptions'][ass][3])):

                    assumptionsId = AssumptionsNs.objects.filter(assumptionsprimary=insert['assumptions'][ass][0],
                                                                 assumptionssecondary=insert['assumptions'][ass][1],
                                                                 assumptionsdescription=insert['assumptions'][ass][2],
                                                                 assumptionsreferences=insert['assumptions'][ass][3])
                else:

                    assumptions = AssumptionsNs(assumptionsprimary=insert['assumptions'][ass][0],
                                                assumptionssecondary=insert['assumptions'][ass][1],
                                                assumptionsdescription=insert['assumptions'][ass][2],
                                                assumptionsreferences=insert['assumptions'][ass][3])
                    assumptions.save()
                    assumptionsId = AssumptionsNs.objects.latest('id_assumptions')

                    fichierlog = open('compare/static/compare/log.txt', "a")
                    wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', str(assumptions)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                nsass = NsToAssumptions(filename=ns, id_assumptions=assumptionsId)
                nsass.save()

        create_h5_directory()

        temp_path = os.path.join(settings.STATIC_ROOT, 'temp')

        for filename in os.listdir(temp_path):
            if filename.endswith(('.txt', '.npy')):
                txt_npy_filepath = os.path.join(temp_path, filename)
                txt_npy_filename = filename
                data_path = os.path.join(settings.STATIC_ROOT, 'static', 'data', txt_npy_filename)

            if filename.endswith('.h5'):
                h5_filepath = os.path.join(temp_path, filename)
                h5_filename = filename
                h5_path = os.path.join(settings.STATIC_ROOT, 'static', 'h5', h5_filename)

        if os.path.isfile(txt_npy_filepath):
            shutil.move(txt_npy_filepath, data_path)

        if os.path.isfile(h5_filepath):
            shutil.move(h5_filepath, h5_path)

        remove_temp_directory()

        fichierlog = open('compare/static/compare/log.txt', "a")
        wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
               str(datetime.datetime.now())+'\n', 'Content:', str(ns)+'\n\n']
        fichierlog.writelines(wri)
        fichierlog.close()

        redirect = 'add'
        return HttpResponse(json.dumps(redirect), content_type='application/json',)

    queryall = Ns.objects.select_related().all()

    queryref = RefNs.objects.all().distinct()

    queryname = NameNs.objects.all().distinct()
    count_by_classdb = queryname.values('classdb').annotate(distinct_class_db_count=Count('classdb', distinct=True))

    methodoptions = MethodNs.method.field.choices
    listmethod = []
    for mo in methodoptions:
        listmethod.append(mo[0])

    constrainoptions = ConstrainNs.constraintype.field.choices
    listconstrain = []
    for co in constrainoptions:
        listconstrain.append(co[0])

    constrainvar = ConstrainNs.constrainvariable.field.choices
    listconstrainvar = []
    for cov in constrainvar:
        listconstrainvar.append(cov[0])

    query = {"queryall": queryall,
             "queryname": queryname,
             "count_by_name_and_classdb": count_by_classdb,
             'queryref': queryref,
             'listmethod': listmethod,
             'listconstrain': listconstrain,
             'listconstrainvar': listconstrainvar}

    return render(request, "compare/insert.html", query)


def info(request):
    return render(request, "compare/info.html", )