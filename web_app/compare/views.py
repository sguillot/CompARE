import datetime
import json
import pandas as pd
import decimal
from decimal import Decimal

from compare.models import Ns, NsToModel, NsToAssumptions, MethodNs, AssumptionsNs, ModelNs, ConstrainNs, NameNs, RefNs
from compare.compare_utils import formatting_csv

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q
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


def visu_data(request):

    # We select all the Ns from the database without models and assumptions but
    # with "ref" ,"name" ,"constrain" and "method" with method select_related
    select_ns_all = Ns.objects.select_related().all().order_by('filename')

    class_list = ["NS Spin", "Transiently_Accreting_NS", "NS Mass", "NS-NS mergers",
                  "PPM", "qLMXB", "Cold MSP", "Thermal INSs", "Type-I X-ray bursts"]

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
            # List with the "filenames" that the user has selected
            to_download = json.loads(download_select)

            # We only retrieve the filepaths of the filenames
            # TODO: CRITICAL: May need to change if filepath are removed from DB
            selected_filepath = select_ns_all.filter(filename__in=to_download).values('filepath')

            # We put these filepath in a list (instead of DjangoRequest)
            list_filepaths = []
            for f in selected_filepath:
                list_filepaths.append(f['filepath'])

            # We return the list of filepaths to the success part of Ajax request
            return HttpResponse(json.dumps(list_filepaths), content_type='application/json')

        # For the selection of BibTex info to download
        if bibtex_select:
            # List with the "filenames" that the user has selected
            list_bibtex = json.loads(bibtex_select)

            # We retrieve the Bibtex info of the selected filenames
            selected_bibtex = select_ns_all.filter(filename__in=list_bibtex).values('id_ref__bibtex')

            # We create the output bibtex file (opening in write mode)
            # TODO: CRITICAL: check if this is not a security issue!!!
            output_bibtex = open('web_app\compare\static\compare\Bibtex.txt', "w")

            # We sequentially write them in the output file, then close the file
            for b in selected_bibtex:
                output_bibtex.write("{}/n/n".format(b['id_ref__bibtex']))
            output_bibtex.close()

            # We return the path of the Bibtex file to the success part off the AJAX request
            return HttpResponse(json.dumps("../static/compare/Bibtex.txt"), content_type='application/json')

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

            # Once the filtering is done, we put the necessary info of selected NS (select_ns_all) in a filtered_list
            filtered_list = []
            for ns in select_ns_all:
                # We put in the list only the attributes shown in the table into a dictionary
                ns_info = {'namedb': ns.id_name.namedb,
                           'filename': ns.filename,
                           'filpath': ns.filepath,
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
                list_model_dependencies = []
                for snm in select_ns_model:
                    # We pre-format the string of model dependencies (prim. and sec.)
                    list_model_dependencies.append("<li><u>{}</u>: {}</li>".format(snm.id_model.dependenciesprimary,
                                                                                   snm.id_model.dependenciessecondary))
                    # The pre-formatted list is added to the dictionary
                    ns_info['model'] = list_model_dependencies

                # We select the filenames linked to assumptions and add all the models to a list
                select_ns_ass = NsToAssumptions.objects.select_related().filter(filename=ns.filename)
                list_assumptions = []
                for snm in select_ns_ass:
                    # we get the assumption (prim. and sec.) and put it in a string and after the dictionary of the NS
                    list_assumptions.append("<li><u>{}</u>: {}</li>".format(snm.id_assumptions.assumptionsprimary,
                                                                            snm.id_assumptions.assumptionssecondary))
                    # The pre-formatted list is added to the dictionary
                    ns_info['assumptions'] = list_assumptions

                # We add the dictionary of the ns to the filtered_list of all ns
                filtered_list.append(ns_info)

            # We return the filtered_list of all ns back to the HTML
            return HttpResponse(json.dumps(filtered_list), content_type='application/json',)

        else:
            # We add the model dependencies, assumptions and filepath of all NS
            list_ns_model_dependencies = []
            list_ns_assumptions = []
            list_ns_filepaths = []

            for ns in select_ns_all:
                # We make the file paths from the filenames (to be used by the django template)
                list_ns_filepaths.append("data/"+ns.filename)

                # We select the filenames linked to models
                select_ns_model_dependencies = NsToModel.objects.select_related().filter(filename=ns.filename)
                # We select the filenames linked to assumptions
                select_ns_assumptions = NsToAssumptions.objects.select_related().filter(filename=ns.filename)

                list_temp_prim = []
                list_temp_sec = []
                for s in select_ns_model_dependencies:
                    list_temp_prim.append(s.id_model.dependenciesprimary)
                    list_temp_sec.append(s.id_model.dependenciessecondary)
                list_ns_model_dependencies.append(zip(list_temp_prim, list_temp_sec))

                list_temp_prim = []
                list_temp_sec = []
                for s in select_ns_assumptions:
                    list_temp_prim.append(s.id_assumptions.assumptionsprimary)
                    list_temp_sec.append(s.id_assumptions.assumptionssecondary)
                list_ns_assumptions.append(zip(list_temp_prim, list_temp_sec))

            # Zip all the data into a tuple
            select_ns_all_zip = zip(select_ns_all,
                                    list_ns_model_dependencies,
                                    list_ns_assumptions,
                                    list_ns_filepaths)

            # We select the data that will appear in the table, and put into a dictionary
            select_all_ns = {"queryall": select_ns_all_zip,
                             "queryMeth": MethodNs.objects.values('method').distinct(),
                             "queryConV": ConstrainNs.objects.values('constrainvariable').distinct(),
                             "queryConT": ConstrainNs.objects.values('constraintype').distinct(),
                             "queryDep": ModelNs.objects.values('dependenciesprimary').distinct(),
                             "queryDepS": ModelNs.objects.values('dependenciessecondary').distinct(),
                             "queryAss": AssumptionsNs.objects.values('assumptionsprimary').distinct(),
                             "queryAssS": AssumptionsNs.objects.values('assumptionssecondary').distinct()
                             }

            # Send the dictionary to the template
            return render(request, "compare/visu_data.html", select_all_ns)


def detail(request, id):

    # For deletion of entry (button "Remove" in details.html)
    if request.method == 'POST':
        filename = json.loads(request.POST.get('filename'))
        file = Ns.objects.get(filename=filename)

        logfile = open('web_app\compare\static\compare\log.txt', "a")
        wri = ['Delete:\n', 'User:', str(request.user.get_username())+'\n',
               'Date:', str(datetime.datetime.now())+'\n', 'Content:', str(file)+'\n\n']
        logfile.writelines(wri)
        logfile.close()

        # Removing the file from the database
        file.delete()
        return HttpResponse(json.dumps('yes'), content_type='application/json',)

    # We retrieve all the data linked to the id(filename) of the NS in a query set
    ns_list = Ns.objects.select_related().get(filename=id)

    # We retrieve all the models dependencies linked to the id(filename) of the NS
    ns_model_dependencies = NsToModel.objects.select_related('id_model').filter(filename=id)

    # We retrieve all the assumptions linked to the id(filename) of the NS
    ns_assumptions = NsToAssumptions.objects.select_related('id_assumptions').filter(filename=id)

    # Trick to link to ADS page (need to replace the &, for ex in A&A)
    ns_list.id_ref.shortlink = ns_list.id_ref.short.replace("&", "%26")

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
              "queryAs": ns_assumptions}

    return render(request, 'compare/detail.html', select)


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
            name = request.POST.get('namens')

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
                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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
                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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

                    logfile = open('web_app\compare\static\compare\log.txt', "a")
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


                    # we create the new NS (filepath have to change)
                    file = Ns(filename=filename,
                              ## TODO: filepath could be removed from MySQL database
                              filepath="qdsdsqdsqdsq.txt",
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

        # for insertion manual we check the what the user wants to insert
        elif (request.POST.get('hid') == 'formAddName' ):

            # verifications of the value
            na =  request.POST.get('name')
            classdb = request.POST.get('class')

            if len(na) <= 0  or len(classdb) <= 0:
                messages.error(request, "L'insertion de Name n'est pas correcte")
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
                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
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
            messages.error(request,"L'insertion de Ref n'est pas correct")
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

                fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                       str(datetime.datetime.now())+'\n', 'Content:', str(ref)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

    # When the user validete the insertion
    if (request.POST.get('insert')):

        # We verify all the values
        insert = json.loads(request.POST.get('insert'))

        # TODO:  Fix these conditions:  for ex with:   insert['filepath'] is ''
        if (len(insert['filename']) <= 0) or (len(insert['filepath']) <= 0):
            mess = "/!\ ERROR /!\: Please enter a Filename or/and a Filepath"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif (insert['name'] == "opt") or (insert['ref']== 'opt'):
            mess = "/!\ ERROR /!\: Please select a Name or/and a Ref"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif (len(insert['method']['methodS']) <= 0) or \
             (len(insert['method']['methodD']) <=0 ) or \
             (len(insert['method']['methodP']) <=0 ):
            mess = "/!\ ERROR /!\: Please enter a valid Method"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif len(insert['constrain']['constrainVer']) <= 0:
            mess = "/!\ ERROR /!\: Please enter a valid Constrain"
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

                fichierlog = open('web_app\compare\static\compare\log.txt', "a")
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

                fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                       str(datetime.datetime.now())+'\n', str(constrain)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

            # We create the new ns with all the field
            ns = Ns(filename=insert['filename'], filepath=insert['filepath'],
                    id_ref=ref, id_name=name,
                    id_method=methodId, id_constrain=constrainId)
            ns.save()

        if len(insert['model']) > 0:

            ns = Ns.objects.get(filename=insert['filename'])
            # for all the model we verify the value and create the object ,
            # if alreday exiqt we linked it , same as the others
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

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
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

                if len(insert['massumptionsodel'][ass][3]) < 1:
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

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
                           str(datetime.datetime.now())+'\n', str(assumptions)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                nsass = NsToAssumptions(filename=ns, id_assumptions=assumptionsId)
                nsass.save()

        fichierlog = open('web_app\compare\static\compare\log.txt', "a")
        wri = ['User:', str(request.user.get_username())+'\n', 'Date:',
               str(datetime.datetime.now())+'\n', 'Content:', str(ns)+'\n\n']
        fichierlog.writelines(wri)
        fichierlog.close()

        redirect = 'add'
        return HttpResponse(json.dumps(redirect), content_type='application/json',)

    # We select the value for the dropdown list
    group = request.user.groups.values_list('name', flat=True)
    groupList = list(group)

    queryall = Ns.objects.select_related().all()
    queryname = NameNs.objects.filter(classdb__in=group)
    queryref = RefNs.objects.all().distinct()

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
             'queryref': queryref,
             'groupList': groupList,
             'listmethod': listmethod,
             'listconstrain': listconstrain,
             'listconstrainvar': listconstrainvar}
    return render(request, "compare/insert.html", query)


def info(request):
    return render(request, "compare/info.html", )
