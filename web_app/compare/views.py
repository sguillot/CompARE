import datetime
import decimal
import json
from django.shortcuts import render , redirect
import numpy as np
from compare.models import Ns , NsToModel , NsToAssumptions , MethodNs , AssumptionsNs , ModelNs , ConstrainNs , NameNs , RefNs
from compare.compare_utils import formatting_csv
from django.http import HttpResponse
from django.db.models import Q
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as logout_user
from decimal import Decimal, InvalidOperation
from django.db import IntegrityError


def home(request):
    return render(request, "compare/home.html")

def visu_data(request):

    #We select all the Ns from the database without models and assumptions but whith "ref" ,"name" ,"constrain" and "method" thanks to the selected related method
    select_ns_all = Ns.objects.select_related().all().order_by('filename')
    
    #we check for GET request
    if request.method == 'GET':

        #In case the user send a Get Request We get the values sent
        
        # We recover the data sent in AJAX
        jsonCheckList = request.GET.get('dataCheckList', '')
        stringSearch = request.GET.get('dataSearch','')
        dictSelect = request.GET.get('dataSelect','')
        fileBibtex = request.GET.get('bibtexfile')
        fileDwnl = request.GET.get('filedwnl')
        
        
        #We retrieve the filenames and return the filepaths of the files to the succes part of the Ajax request 
        #if the variable fileDwnl has a value
        if fileDwnl :  
            dwnl = json.loads(fileDwnl) # python list with the "filenames" that the user has selected
            selectfilepath = select_ns_all.filter(filename__in=dwnl).values('filepath') #We only retrieve the filepaths of the filenames

            #We extract the result in a list thanks to a loop 
            listFilePath = []
            for f in selectfilepath:
                listFilePath.append(f['filepath'])
            #We return the list to the succes part of Ajax request
            return HttpResponse(json.dumps(listFilePath), content_type='application/json')

        #We retrieve the filenames and write the Bibtex in a file
        #if the variable fileBibtex has a value
        if fileBibtex:
             bib = json.loads(fileBibtex) #python list with the filenames that the user has selected
             selectbib = select_ns_all.filter(filename__in=bib).values('id_ref__bibtex')#We recover the Bibtex in connection with our filename list 

             #Writing Bitex to a file
             fichierBib = open('web_app\compare\static\compare\Bibtex.txt', "w") #Open file in write mode (w)

             for b in selectbib:#Loop to write each bibtex of the list
                fichierBib.write(b['id_ref__bibtex'])#Writing the bibtex to the file 
                fichierBib.write('\n\n')
             fichierBib.close() #Closing the file

             #We return the path of the Bibtex file to the succes part off the AJAX request
             return HttpResponse(json.dumps("../static/compare/Bibtex.txt"), content_type='application/json')
        
        #We filter with the result of the search bar if the user has sent a request
        #if the variable stringSearch has a value
        if stringSearch :
            #We filter the select variable that contains all the Ns from the database
            #we check if the fields contain the sent string (case insensitive)
            select_ns_all = select_ns_all.filter(Q(id_name__namedb__icontains = stringSearch) |
                                                 Q(id_name__classdb__icontains = stringSearch) |
                                                 Q(id_method__method__icontains = stringSearch) |
                                                 Q(id_method__datadate__icontains = stringSearch) |
                                                 Q(id_method__processinfinfo__icontains = stringSearch) |
                                                 Q(id_constrain__constraintype__icontains = stringSearch) |
                                                 Q(id_constrain__constrainversion__icontains = stringSearch)|
                                                 Q(id_constrain__constrainvariable__icontains = stringSearch)
                                                 )
        
        #We filter with the result of the side checkbox panel if the user has sent a request  
        #if the variable jsonCheckList has a value   
        if jsonCheckList:
            checkList = json.loads(jsonCheckList) #python list with the checkboxes that are checked
            #if checklist is empty we do like all the checkboxes were checked
            if not checkList:
                checkList = ["NS Spin","Transiently_Accreting_NS","NS Mass","NS-NS mergers","PPM","qLMXB","Cold MSP","Thermal INSs","Type-I X-ray bursts"] #list with all types of sources

            #We filter the select variable that contains all the Ns from the database ( it can be already filter from the above condition )
            #we select the ns who have a values from the list 
            select_ns_all = select_ns_all.filter(id_name__classdb__in=checkList)

        #We filter with the select box selected if the user has sent a request  
        #if the variable dictSelect has a value
        if dictSelect :
            sel = json.loads(dictSelect) #dictionnary python list  whith the values selected (key = the selecte box , value = the selected item )
            
            #We check if the keys have a value if they have we filter the select variable already filtered above with the values 
            if sel['MethList']:
                select_ns_all = select_ns_all.filter(id_method__method__in=sel['MethList'])
            if sel['ConsVList']:
                select_ns_all = select_ns_all.filter(id_constrain__constrainvariable__in=sel['ConsVList'])
            if sel['ConsTList']:
                select_ns_all = select_ns_all.filter(id_constrain__constraintype__in=sel['ConsTList'])

            #For the dependencies and assumptions select box
            #we check if the keys have a value
            if sel['DepList']:
                filListDep = []
                for fil in select_ns_all:#Loop to get all filename from the filtered select 
                    filListDep.append(fil.filename)#We put in a list the filenames 
                # We select the filenames that have the primary dependencies and the filenames
                selectDep = NsToModel.objects.select_related().filter(Q(filename__in=filListDep) &
                                                                      Q(id_model__dependenciesprimary__in = sel['DepList'])).values_list('filename',flat=True).distinct()
                depList = list(selectDep) # We put in a list the filenames of the select
                depFilter = Ns.objects.select_related().filter(filename__in = depList)#We select the NS who have the filenames 
                select_ns_all = depFilter # we change our main select variable

            # We do the same for these 3 select box
            if sel['DepSList']:
                fil2ListDep = []
                for fil2 in select_ns_all:
                    fil2ListDep.append(fil2.filename)
                selectDepS = NsToModel.objects.select_related().filter(Q(filename__in=fil2ListDep)
                                                                & Q(id_model__dependenciessecondary__in = sel['DepSList'])).values_list('filename',flat=True).distinct()
                depListS = list(selectDepS)
                depSFilter = Ns.objects.select_related().filter(filename__in = depListS)
                select_ns_all = depSFilter

            if sel['AssList']:
                filListAss = []
                for fil in select_ns_all:
                    filListAss.append(fil.filename)
                selectMod = NsToAssumptions.objects.select_related().filter(Q(filename__in=filListAss)
                                                                & Q(id_assumptions__assumptionsprimary__in = sel['AssList'])).values_list('filename',flat=True).distinct()
                assList = list(selectMod)
                assFilter = Ns.objects.select_related().filter(filename__in = assList)
                select_ns_all = assFilter

            if sel['Ass2List']:
                fil2ListAss = []
                for fil2 in select_ns_all:
                    fil2ListAss.append(fil2.filename)
                
                selectModS = NsToAssumptions.objects.select_related().filter(Q(filename__in=fil2ListAss)
                                                                & Q(id_assumptions__assumptionssecondary__in = sel['Ass2List'])).values_list('filename',flat=True).distinct()
                assListS = list(selectModS)
                assSFilter = Ns.objects.select_related().filter(filename__in = assListS)
                select_ns_all = assSFilter


            #we are out the if statements 
            #we put in a list all the NS with the model and assumptions
            listFilt = []

            for all in select_ns_all:
                #we put in the list only the elements that we show in the table in a dictionnary
                loop = {}    
                
                #we get the name and put it in the dictionaray of the NS
                namedb = all.id_name.namedb 
                loop['namedb']=namedb

                #we get the filename and put it in the dictionaray of the NS
                filens = all.filename
                loop['filename']=filens

                #we get the filepath and put it in the dictionaray of the NS
                filpath = all.filepath
                loop['filpath']=filpath

                #we get the class and put it in the dictionaray of the NS
                namecla = all.id_name.classdb
                loop['classdb']=namecla

                #we get the method and put it in the dictionaray of the NS
                method = all.id_method.method
                loop['method']=method

                #we get the method specific and put it in the dictionaray of the NS
                methodspe = all.id_method.method_specific
                loop['method_specific']=methodspe

                #we get the constrain type and put it in the dictionaray of the NS
                constrainty = all.id_constrain.constraintype
                loop['constraintype']=constrainty

                #we get the constrain version  and put it in the dictionaray of the NS
                constrainver = all.id_constrain.constrainversion
                loop['constrainversion']=constrainver
                
                #we get the constrain variable and put it in the dictionaray of the NS
                constrainvar = all.id_constrain.constrainvariable
                loop['constrainvariable']= str(constrainvar)

                #we get the DOI and put it in the dictionaray of the NS
                refdoi = all.id_ref.doi
                loop['doi']= refdoi

                #we get the author and put it in the dictionaray of the NS
                refauthor = all.id_ref.author
                loop['author']= refauthor

                #we get the year and put it in the dictionaray of the NS
                refyear = all.id_ref.refyear
                loop['year']= refyear

                #We select the filenames linked to models 
                select_ns_model =  NsToModel.objects.select_related().filter(filename = all.filename)

                # We put in a list all the models linked to a filename
                list_temp = []
                for snm in select_ns_model:
                    #we get the model and put it in a list and after the dictionaray of the NS
                    # TODO - see if this can be returned as a tuple to be used by AJAX (script.js:line193)
                    list_temp.append("{}: {}".format(snm.id_model.dependenciesprimary, snm.id_model.dependenciessecondary))
                    loop['model'] = list_temp

                #We select the filenames linked to assumptions 
                select_ns_ass = NsToAssumptions.objects.select_related().filter(filename = all.filename)

                #we put in a list all the assumptions linked to a filename 
                list_temp2 = []
                for snm in select_ns_ass:
                    # we get the assumption (prim. and sec.) and put it in a list and after the dictionaray of the NS
                    # TODO - see if this can be returned as a tuple to be used by AJAX (script.js:line193)
                    list_temp2.append("{}: {}".format(snm.id_assumptions.assumptionsprimary, snm.id_assumptions.assumptionssecondary))
                    loop['assumptions'] = list_temp2

                # We add the dictionary to the list
                listFilt.append(loop)

            # We return the list with the ns
            return HttpResponse(json.dumps(listFilt), content_type='application/json',)
        
        else:
            # We add the models to each NS
            list_ns_model = []
            list_ns_assumptions = []

            for n in select_ns_all:
                # We select the filenames linked to models
                select_ns_model = NsToModel.objects.select_related().filter(filename = n.filename)
                # We select the filenames linked to assumptions
                select_ns_ass = NsToAssumptions.objects.select_related().filter(filename = n.filename)

                list_temp_prim = []
                list_temp_sec  = []
                for snm in select_ns_model:
                    list_temp_prim.append(snm.id_model.dependenciesprimary)
                    list_temp_sec.append(snm.id_model.dependenciessecondary)
                list_ns_model.append(zip(list_temp_prim, list_temp_sec))

                list_temp_prim = []
                list_temp_sec  = []
                for sass in select_ns_ass:
                    list_temp_prim.append(sass.id_assumptions.assumptionsprimary)
                    list_temp_sec.append(sass.id_assumptions.assumptionssecondary)
                list_ns_assumptions.append(zip(list_temp_prim, list_temp_sec))

            #we select the data who will be in the select box
            selectMethod = MethodNs.objects.values('method').distinct()
            selectConstrainV = ConstrainNs.objects.values('constrainvariable').distinct()
            selectConstrainT = ConstrainNs.objects.values('constraintype').distinct()
            selectModel = ModelNs.objects.values('dependenciesprimary').distinct()
            selectModelSec = ModelNs.objects.values('dependenciessecondary').distinct()
            selectAssumptions = AssumptionsNs.objects.values('assumptionsprimary').distinct()
            selectAssumptions2 = AssumptionsNs.objects.values('assumptionssecondary').distinct()

            #compact in one object all the data
            select_ns_all_zip = zip(select_ns_all,
                                    list_ns_model,
                                    list_ns_assumptions)

            selectAll = {"queryall":select_ns_all_zip,
                         "queryMeth":selectMethod,
                         "queryAss":selectAssumptions,
                         "queryDep":selectModel,
                         "queryConV":selectConstrainV,
                         "queryConT":selectConstrainT,
                         "queryDepS":selectModelSec,
                         "queryAssS":selectAssumptions2}

            #send to the template
            return render(request, "compare/visu_data.html",selectAll)

def detail(request, id):
    if request.method == 'POST':
        filename = json.loads(request.POST.get('filename'))
        file = Ns.objects.get(filename = filename)

        fichierlog = open('web_app\compare\static\compare\log.txt', "a")
        wri = ['Delete:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(file)+'\n\n']
        fichierlog.writelines(wri)
        fichierlog.close()

        file.delete()

        truc='yes'
        return HttpResponse(json.dumps(truc), content_type='application/json',)
         
    #We recup all the data(ref ,constrain ,name ,method ) linked to the id(filename) of the NS in a query set 
    ns_list = Ns.objects.select_related().get(filename = id)

    #We recup all the Models linked to the id(filename) of the NS
    ns_Mo = NsToModel.objects.select_related('id_model').filter(filename = id)

    #We recup all the Assumptions linked to the id(filename) of the NS
    ns_As = NsToAssumptions.objects.select_related('id_assumptions').filter(filename = id)

    # Trick to link to ADS page (need to replace the &, for ex in A&A)
    ns_list.id_ref.shortlink = ns_list.id_ref.short.replace("&","%26")

    for mo in ns_Mo:
        if mo.id_model.dependenciesreferences is not None:
            mo.id_model.reflist = zip(mo.id_model.dependenciesreferences.split(", "),
                                      mo.id_model.dependenciesreferences.replace("&","%26").split(", "))
        else:
            mo.id_model.reflist = None

    for ass in ns_As:
        if ass.id_assumptions.assumptionsreferences is not None:
            ass.id_assumptions.reflist = zip(ass.id_assumptions.assumptionsreferences.split(", "),
                                             ass.id_assumptions.assumptionsreferences.replace("&","%26").split(", "))
        else:
            ass.id_assumptions.reflist = None

    #We put in a dictionary the querysets with a key . The keys will allow us to display the data of the queryset in the template 
    select = {"queryall": ns_list,
              "queryMo": ns_Mo,
              "queryAs": ns_As}
    return render(request, 'compare/detail.html', select)

@login_required 
def modify(request,id):  

    ns_list = Ns.objects.select_related().get(filename = id)

    #We recup all the Models linked to the id(filename) of the NS
    ns_Mo = NsToModel.objects.select_related('id_model').filter(filename = id)

    #We recup all the Assumptions linked to the id(filename) of the NS
    ns_As = NsToAssumptions.objects.select_related('id_assumptions').filter(filename = id)

    #We recup the Name linked to the id(filename) of the NS
    name_file = Ns.objects.filter(id_name = ns_list.id_name)

    #We recup the Ref linked to the id(filename) of the NS
    ref_file = Ns.objects.filter(id_ref = ns_list.id_ref)

    #We recup the method linked to the id(filename) of the NS
    method_file = Ns.objects.filter(id_method = ns_list.id_method)

    #We recup the constrain linked to the id(filename) of the NS
    constrain_file = Ns.objects.filter(id_constrain = ns_list.id_constrain)

    #We put in a list the filenames linked to this Model
    molist = []
    for mo in ns_Mo:
        molist.append(ModelNs.objects.filter(id_model = mo.id_model.id_model))

    filemo = {}
    for m in molist:
        for i in m:
            filemo[i.id_model]=NsToModel.objects.filter(id_model = i.id_model)

    #We put in a list the filenames linked to this assumptions
    asslist = []
    for ass in ns_As:
        asslist.append(AssumptionsNs.objects.filter(id_assumptions = ass.id_assumptions.id_assumptions))

    fileass = {}
    for a in asslist:
        for j in a:
            fileass[j.id_assumptions]=NsToAssumptions.objects.filter(id_assumptions = j.id_assumptions)


    #We get the value off the method enum in a list
    methodoptions = MethodNs.method.field.choices
    listmethod =[]
    for mo in methodoptions:
        listmethod.append(mo[0])

    #We get the value off the constraintype enum in a list
    constrainoptions = ConstrainNs.constraintype.field.choices
    listconstrain =[]
    for co in constrainoptions:
        listconstrain.append(co[0])

    #We get the value off the constrain variable enum in a list
    constrainvar = ConstrainNs.constrainvariable.field.choices
    listconstrainvar =[]
    for cov in constrainvar:
        listconstrainvar.append(cov[0])

    #We check for Post request 
    if request.method == 'POST':
        #We check what table the user want to modify 
        if 'name' in request.POST:

            # We get all the field and verify if they are correct
            nameNS = NameNs.objects.get(id_name=ns_list.id_name.id_name)
            
            name = request.POST.get('namens')
            classNs = nameNS.classdb
            name = request.POST.get('namens')


            if len(name) <= 0 or len(classNs) <= 0:
                messages.error(request,"No")
            else:
                nameSin = request.POST.get('namesin')
                if (nameSin is not None) and (len(nameSin) < 1 ):
                    nameSin = None

                classSin = request.POST.get('classsin')
                if (classSin is not None) and (len(classSin) < 1): 
                    classSin = None

                ra = request.POST.get('r')
                if (ra is not None) and (len(ra)>1):
                    ra = Decimal(ra)
                else:
                    ra = None

                dec = request.POST.get('dec')
                if (dec is not None) and (len(dec)>1):
                    dec = Decimal(dec)
                else:
                    dec = None

                loc = request.POST.get('localisation')
                if (loc is not None) and (len(loc)<1):
                    loc = None

                event = request.POST.get('event')
                if (event is not None) and (len(event)<1):
                    event = None
            
                #if the user clic on the update button we change the name of the ns 
                if 'update' in request.POST :
                    nameNS.namedb = name
                    nameNS.classdb = classNs
                    nameNS.namesimbad = nameSin
                    nameNS.classsimbad = classSin
                    nameNS.ra = ra
                    nameNS.declination = dec
                    nameNS.localisationfile = loc
                    nameNS.eventdate = event
                    nameNS.save()
                    messages.success(request,"Yes")

                    #to write in the log file
                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Modify:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(nameNS)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                #if the user clic on the add button 
                elif 'add' in request.POST :
                    #We check if the name alreday exist  and linked it if its the case
                    if (NameNs.objects.filter(namedb=name,classdb=classNs,namesimbad=nameSin,classsimbad=classSin,ra=ra,declination=dec,localisationfile=loc)):
                        nameExist =NameNs.objects.filter(namedb=name,classdb=classNs,namesimbad=nameSin,classsimbad=classSin,ra=ra,declination=dec,localisationfile=loc)
                        nameExist= nameExist[0]
                        ns_list.id_name = nameExist
                        ns_list.save()
                        messages.success(request,"jajajaja")
                    #we add the name 
                    else:
                        nameAdd = NameNs(namedb=name, classdb=classNs, namesimbad=nameSin, classsimbad=classSin, ra=ra, declination=dec, localisationfile=loc, eventdate=event)
                        nameAdd.save()
                        ns_list.id_name = nameAdd
                        ns_list.save()
                        messages.success(request,"Yes")

                    #to write in the logo file
                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content: Name ',str(ns_list.id_name)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

            return redirect('modify',id)       

        #We do the same things for all field of the table 

        if 'ref' in request.POST:

            RefNS = RefNs.objects.get(id_ref=ns_list.id_ref.id_ref)
            
            auth = request.POST.get('author')

            year = request.POST.get('refyear')

            short = request.POST.get('short')

            bibtex = request.POST.get('bibtex')

            doi = request.POST.get('doi')

            if len(auth)<= 0 or len(year)<=0 or len(short)<=0 or len(bibtex)<=0 or len(doi)<=0:
                messages.error(request,"NO")
            else:
                repdoi = request.POST.get('repdoi')
                if (repdoi is not None) and (len(repdoi)<1):
                    repdoi = None
                datal = request.POST.get('datalink')
                if (datal is not None) and (len(datal)<1):
                    datal = None
                if(datal == "None"):
                    datal = None
                if 'update' in request.POST :
                    RefNS.author = auth
                    RefNS.refyear = year
                    RefNS.short = short
                    RefNS.bibtex = bibtex
                    RefNS.doi = doi
                    RefNS.repositorydoi = repdoi
                    RefNS.datalink = datal
                    RefNS.save()
                    messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Modify:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(RefNS)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                elif 'add' in request.POST :
                    if(RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)):
                        refExist = RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)
                        refExist = refExist[0]
                        ns_list.id_ref = refExist
                        ns_list.save()
                        messages.success(request,"jojojojo")
                    else:   
                        ref = RefNs(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)
                        ref.save()
                        ns_list.id_ref = ref
                        ns_list.save()
                        messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content: Ref ',str(ns_list.id_ref)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

            return redirect('modify',id) 

        if 'method' in request.POST:

            MethNS = MethodNs.objects.get(id_method=ns_list.id_method.id_method)

            meth = request.POST.get('methodns')

            methS = request.POST.get('methodspe')

            datad = request.POST.get('datadate')

            proceInfo = request.POST.get('processinfinfo')

            if len(meth)<= 0 or len(methS)<=0 or len(datad)<=0 or len(proceInfo)<=0:
                messages.error(request,"L'insertion de Method n'est pas correct")
            else :
                if 'update' in request.POST :
                    MethNS.method = meth
                    MethNS.method_specific = methS
                    MethNS.datadate = datad
                    MethNS.processinfinfo = proceInfo
                    MethNS.save()
                    messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Modify:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(MethNS)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                elif 'add' in request.POST :
                    if (MethodNs.objects.filter(method =meth, method_specific =methS,datadate = datad,processinfinfo =proceInfo)):
                        methodExist = MethodNs.objects.filter(method =meth, method_specific =methS,datadate = datad,processinfinfo =proceInfo)
                        methodExist = methodExist[0]
                        ns_list.id_method = methodExist
                        ns_list.save()
                        messages.success(request,"Yes")
                    else:   

                        method = MethodNs(method=meth, method_specific=methS, datadate=datad, processinfinfo=proceInfo)
                        method.save()
                        ns_list.id_method = method
                        ns_list.save()
                        messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:Method ',str(ns_list.id_method)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

            return redirect('modify',id) 

        if 'constrain' in request.POST:

            Constrainns = ConstrainNs.objects.get(id_constrain=ns_list.id_constrain.id_constrain)

            constrainT = request.POST.get('constrainT')

            constrainV = request.POST.get('constrainV')

            constrainVar = request.POST.get('constrainVar')

            if len(constrainT)<= 0 or len(constrainV)<=0 or len(constrainVar)<=0:
                messages.error(request,"L'insertion de Cons n'est pas correct")
            else :
                if 'update' in request.POST :
                    Constrainns.constraintype = constrainT
                    Constrainns.constrainvariable = constrainVar
                    Constrainns.constrainversion = constrainV
                    Constrainns.save()

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content: ',str(Constrainns)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                    messages.success(request,"Yes")

                elif 'add' in request.POST :
                    if(ConstrainNs.objects.filter(constraintype =constrainT , constrainvariable = constrainVar,constrainversion = int(constrainV))):

                        constrainExist = ConstrainNs.objects.filter(constraintype =constrainT , constrainvariable = constrainVar,constrainversion = int(constrainV))
                        constrainExist = constrainExist[0]
                        ns_list.id_constrain = constrainExist
                        ns_list.save()
                        messages.success(request,"Yes")

                    else:

                        constrain = ConstrainNs(constraintype=constrainT, constrainvariable=constrainVar, constrainversion=constrainV)
                        constrain.save()
                        ns_list.id_constrain = constrain
                        ns_list.save()
                        messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content: ',str(ns_list.id_constrain)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

            return redirect('modify',id) 

        if 'model' in request.POST:

            model = ModelNs.objects.get(id_model=request.POST.get('model'))

            depP = request.POST.get('dependenciesprimary')
            if len(depP)<1:
                depP = None

            depS = request.POST.get('dependenciessecondary')
            if len(depS)<1:
                depS = None

            depD = request.POST.get('dependenciesdescription')
            if len(depD)<1:
                depD = None

            depR = request.POST.get('dependenciesreferences')
            if len(depR)<1:
                depR = None

            else:
                if 'update' in request.POST :
                    model.dependenciesprimary = depP
                    model.dependenciessecondary = depS
                    model.dependenciesdescription = depD
                    model.dependenciesreferences = depR
                    model.save()
                    messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Modify:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(model)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                elif 'add' in request.POST :
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

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content: ',str(model)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

            return redirect('modify',id) 

        if 'assumption' in request.POST:

            assumption = AssumptionsNs.objects.get(id_assumptions=request.POST.get('assumption'))

            AssP = request.POST.get('assumptionsprimary')
            if len(AssP)<1:
                AssP = None

            AssS = request.POST.get('assumptionssecondary')
            if len(AssS)<1:
                AssS = None

            AssD = request.POST.get('assumptionsdescription')
            if len(AssD)<1:
                AssD = None

            AssR = request.POST.get('assumptionsreferences')
            if len(AssR)<1:
                AssR = None

            else:
                if 'update' in request.POST :
                    assumption.assumptionsprimary = AssP
                    assumption.assumptionssecondary = AssS
                    assumption.assumptionsdescription = AssD
                    assumption.assumptionsreferences = AssR
                    assumption.save()
                    messages.success(request,"Yes")

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Modify:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(assumption)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                elif 'add' in request.POST :
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

                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['Add:\n','User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:Assumptions ',str(assumption)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()
                        
            return redirect('modify',id) 

    #We put in a dictionary the querysets with a key . The keys will allow us to display the data of the queryset in the template modify.html 
    select = {"queryall":ns_list,
                 "queryMo":ns_Mo,
                 "queryAs":ns_As,
                 "queryName":name_file,
                 "queryRef":ref_file,
                 "queryMethod":method_file,
                 "queryConstrain":constrain_file,
                 "queryModel":molist,
                 "queryAssumption":asslist,
                 "queryModellinked":filemo,
                 "queryAssumptionlinked":fileass,
                 'listmethod' :listmethod,
                 'listconstrain':listconstrain,
                 'listconstrainvar':listconstrainvar}  
    
    return render(request, "compare/modify.html",select)

def login(request):
    #We check if a POST request is send
    if request.method == 'POST':
            
            #We get the username and the password of the inputs fields
            username = request.POST['username']
            psw = request.POST['password']

            # We check if the username and the password are of a user 
            user = authenticate(username=username, password=psw)
            if user is not None:

                #We logged in the user and redirect to the Add page 
                auth_login(request,user)
                return redirect('insert')
            else :

                #We send a error message to inform the user that he missed 
                messages.success(request, "incorrect Username or Password")
                return redirect('login')
    else:
        return render(request, "compare/login.html")  

def logout(request):
    #We logged out and redirect to the Visualisation page
    logout_user(request)
    return redirect('visu')

@login_required
def insert_data(request):

    datafolder = {"NS spin": "fastest",
                  "NS mass": "masses",
                  "NS-NS mergers": "gw",
                  "PPM": "msps",
                  "qLMXB": "qlmxb",
                  "Cold MSP": "coldmsps",
                  "Thermal INSs": "ins",
                  "Type-I X-ray bursts": "bursts",
                  "Transiently_Accreting_NS": "cooling"}

    #We check if a Get request is sent from the user (get for the selectlist for nama and ref)
    if request.method == 'GET':
         idName = request.GET.get('idname', '')
         idRef = request.GET.get('idref', '')

         #we get the id of the name selected and select the information of this name
         if idName:
             queryTabName = NameNs.objects.filter(pk=idName)
             querylistName = list(queryTabName.values())
             jsonName = json.dumps((querylistName),default=str)
             return HttpResponse(jsonName, content_type='application/json',)
         
         #we get the id of the ref selected and select the information of this ref
         if idRef :
             queryTabRef = RefNs.objects.filter(pk=idRef)
             querylistRef = list(queryTabRef.values())
             jsonRef = json.dumps((querylistRef),default=str)
             return HttpResponse(jsonRef, content_type='application/json',)
         
    #We check if its a Post request      
    if request.method == 'POST':

        #we check if ist a file send 
        if 'myfile' in request.FILES:
            if(request.FILES['myfile']):  
                input_csv_filename = request.FILES['myfile']
                #we put in a dataframe the value of the file
                d= pd.DataFrame(pd.read_csv(input_csv_filename))
                d = formatting_csv(d)

                #list with type of sources
                NsClass = ["NS spin","Transiently_Accreting_NS","NS mass","NS-NS mergers",
                           "PPM","qLMXB","Cold MSP","Thermal INSs","Type-I X-ray bursts"]

                #we get the enum types in lists
                me =[]
                for m in MethodNs.method.field.choices:
                    me.append(m[0])

                ct =[]
                for c in ConstrainNs.constraintype.field.choices:
                    ct.append(c[0])

                cv =[]
                for v in ConstrainNs.constrainvariable.field.choices:
                    cv.append(v[0])

                nbinsert=0   
                inserted = []
                notinserted = {}           

                #for each row of the dataframe
                for i in range(1,len(d)+1):
                    
                    #we put in list the models and assumptions
                    filename = d['FileName'][i]

                    listmo = d['ModelDependenciesPrimary'][i].split(",")

                    listmosec = d['ModelDependenciesSecondary'][i].split(",")

                    listmodesc = d['ModelDependencyDescription'][i].split("\n")
                    listmodesc = [i for i in listmodesc if i]
                    if (len(listmodesc)==0):
                        listmodesc = ['']  # Just a hack to avoid an empty list if there are no description provided

                    listmodepref = d['ModelDependencyReferences'][i].split("\n")
                    listmodepref = [i for i in listmodepref if i]
                    if (len(listmodepref)==0):
                        listmodepref = ['']  # Just a hack to avoid an empty list if there are no description provided

                    listass = d['AssumptionsPrimary'][i].split(",")

                    listasssec = d['AssumptionsSecondary'][i].split(",")

                    listassdesc = d['AssumptionsDescription'][i].split("\n")
                    listassdesc = [i for i in listassdesc if i]
                    if (len(listassdesc)==0):
                        listassdesc = ['']  # Just a hack to avoid an empty list if there are no description provided

                    listassref = d['AssumptionsReferences'][i].split("\n")
                    listassref = [i for i in listassref if i]
                    if (len(listassref)==0):
                        listassref = ['']  # Just a hack to avoid an empty list if there are no description provided

                    #we verify if the filename do not alreday exist
                    if Ns.objects.filter(filename = d['FileName'][i]):
                        notinserted[filename] = " already in"
                        continue
                    #we verify the non null field
                    elif ((len(d['NameDB'][i]) <= 0  or
                           len(d['ClassDB'][i]) <= 0 or
                           len(d['Method'][i]) <= 0) or
                          (len(d['MethodSpecific'][i])<=0) or
                          (len(d['DataDate'][i])<=0) or
                          (len(d['ProcessingInfo'][i])<=0) or
                          (len(d['ConstrainVariable'][i])<= 0) or
                          (len(d['ConstrainType'][i])<=0) or
                          (len(d['Ref1stAuthor'][i])<= 0) or
                          (len(d['RefYear'][i])<=0) or
                          (len(d['RefShort'][i])<=0) or
                          #(len(d['RefBibtex'][i])<=0) or
                          (len(d['RefDOI'][i])<=0)):
                        notinserted[filename] = " missing mandatory elements"
                        continue

                    #more verifications

                    #elif( (len(d['AssumptionsPrimary'][i])<=0) and (len(d['AssumptionsSecondary'][i])<=0) and (len(d['AssumptionsDescription'][i])<=0)):
                    #     notinserted[filename] = " assumptions have to have minimum one field "
                    #     continue
                    #
                    # elif((len(d['ModelDependenciesPrimary'][i])<=0) and (len(d['ModelDependenciesSecondary'][i])<=0) and (len(d['ModelDependencyDescription'][i])<=0)):
                    #     notinserted[filename] = " model have to have minimum one field"
                    #     continue

                    elif( (len(listmo)!= len(listmosec)) or
                          (len(listmo)!= len(listmodesc)) or
                          (len(listmo) != len(listmodepref))
                        ):
                        notinserted[filename] = " has a mismatch in input model dependencies " \
                                                "( {} primary, {} secondary, {} descriptions, and {} references)".format(len(listmo),
                                                                                                                         len(listmosec),
                                                                                                                         len(listmodesc),
                                                                                                                         len(listassref))
                        continue

                    elif( (len(listass)!= len(listasssec)) or
                          (len(listass)!= len(listassdesc))or
                          (len(listass) != len(listassdesc))
                        ):
                        notinserted[filename] = " has a mismatch in input assumptions " \
                                                "( {} primary, {} secondary, {} descriptions, and {} references)".format(len(listass),
                                                                                                                         len(listasssec),
                                                                                                                         len(listassdesc),
                                                                                                                         len(listassdesc))
                        continue
                    
                    elif str(d['Method'][i]) not in me :
                        notinserted[filename] = d['Method'][i] + " can not be a method (choose among {})".format(me)
                        continue

                    elif d['ConstrainType'][i] not in ct :
                        notinserted[filename] = d['ConstrainType'][i] + " can not be a constrain type (choose among {})".format(ct)
                        continue

                    elif d['ConstrainVariable'][i] not in cv :
                        notinserted[filename] = d['ConstrainVariable'][i] + " can not be a constrain variable (choose among {})".format(cv)
                        continue

                    elif d['ClassDB'][i] not in NsClass :
                        notinserted[filename] = d['ClassDB'][i] + " can not be a name class (choose among {})".format(NsClass)
                        continue

                    elif(len(d['RA'][i])>1):
                        try:
                            Decimal(d['RA'][i])
                        except decimal.InvalidOperation:
                            notinserted[filename] = d['RA'][i] + " can not be a converted in decimal"
                            continue

                    elif(len(d['DEC'][i])>1):
                        try:
                            Decimal(d['DEC'][i])
                        except decimal.InvalidOperation:
                            notinserted[filename] = d['DEC'][i] + " can not be a converted in decimal"
                            continue

                    elif(len(d['RefYear'][i])>1):
                        try:
                            int(d['RefYear'][i])
                        except ValueError:
                            notinserted[filename] = d['RefYear'][i] + " can not be a converted in integer"
                            continue       
                    
                    #we get the value of the name 
                    namen=d['NameDB'][i]
                    classn = d['ClassDB'][i]
                    nameS = d['NameSimbad'][i]
                    classS=d['ClassSimbad'][i]
                    r = d['RA'][i]
                    dec = d['DEC'][i]
                    dat = d['EventDate'][i]
                    loc = d['LocalisationFile'][i]

                    #verifications in case

                    if len(nameS) < 1:
                        nameS = None

                    if len(classS) < 1 : 
                        classS = None

                    if len(r)>1:
                        r = Decimal(r)
                    else:
                        r = None
                        
                    if len(dec)>1 :
                        dec = Decimal(dec)
                    else:
                        dec = None
                    
                    if len(loc)<1:
                        loc = None

                    if len(dat)<1:
                        dat = None

                    #if the name alreday exist we select it 
                    if (NameNs.objects.filter(namedb=namen,classdb=classn,namesimbad=nameS,classsimbad=classS,ra=r,
                                            declination=dec,localisationfile=loc)):
                            
                        idN = NameNs.objects.filter(namedb=namen,classdb=classn,namesimbad=nameS,classsimbad=classS,ra=r,
                                            declination=dec,localisationfile=loc)
                        idN= idN[0]
                    #else We add the new name
                    else:
                        name = NameNs(namedb=namen, classdb=classn, namesimbad=nameS, classsimbad=classS, ra=r, declination=dec, localisationfile=loc, eventdate=dat)
                        name.save()
                        idN =NameNs.objects.latest('id_name') # we store the object that we insert to link it after

                    #we do the same for the other columns of the dataframe

                    methodN = d['Method'][i]
                    methodS = d['MethodSpecific'][i]
                    dDate = d['DataDate'][i]
                    ProcInfo = d['ProcessingInfo'][i]

                    if (MethodNs.objects.filter(method =methodN, method_specific =methodS,datadate = dDate,processinfinfo=ProcInfo)):
                        idM = MethodNs.objects.filter(method =methodN, method_specific =methodS,datadate = dDate,processinfinfo =ProcInfo)
                        idM = idM[0]
                    else:
                        method = MethodNs(method =methodN, method_specific =methodS,datadate = dDate,processinfinfo=ProcInfo)
                        method.save()
                        idM =MethodNs.objects.latest('id_method')

                    consV=d['ConstrainVariable'][i]
                    consT=d['ConstrainType'][i]

                    # TODO: Add check that constrain version is an integer
                    consVe =d['ConstrainVersion'][i]
                                
                
                    if (ConstrainNs.objects.filter(constraintype =consT , constrainvariable = consV,
                                            constrainversion = int(consVe))):
                        idC = ConstrainNs.objects.filter(constraintype =consT , constrainvariable = consV,
                                            constrainversion = int(consVe))
                        idC = idC[0]
                    else:                    
                        constrain=ConstrainNs(constraintype =consT , constrainvariable = consV,
                                            constrainversion = int(consVe))
                        constrain.save()
                        idC =ConstrainNs.objects.latest('id_constrain')

                    auth = d['Ref1stAuthor'][i]
                    year = d['RefYear'][i]
                    short =d['RefShort'][i]
                    bibtex = d['RefBibtex'][i]
                    doi = d['RefDOI'][i]
                    repdoi =d['DataRepositoryDOI'][i]
                    datal = d['DataLink'][i]

                    if len(repdoi)<1:
                        repdoi = None

                    if len(datal)<1:
                        datal = None

                    if(RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)):
                        idR = RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)
                        idR = idR[0]
                    else:
                        ref = RefNs(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)
                        ref.save()   
                        idR =RefNs.objects.latest('id_ref')


                    # we create the new NS (filepath have to change)
                    file = Ns(filename=filename,filepath="qdsdsqdsqdsq.txt",id_ref=idR,id_name=idN,id_method=idM,id_constrain=idC)  
                    file.save()
                    nsInstance = Ns.objects.get(filename=filename) # we store the ns for the assumptions and models

                    for j in range(len(listmo)):
                        modelpri = listmo[j]
                        modelsec = listmosec[j]
                        modeldesc = listmodesc[j]
                        modelref = listmodepref[j]

                        if len(modelpri)<1:
                            modelpri = None

                        if len(modelsec)<1:
                            modelsec = None

                        if len(modeldesc)<1:
                            modeldesc = None

                        if len(modelref)<1:
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
                        #we create the link between ns and model
                        nsmodel = NsToModel(filename=nsInstance, id_model=idMo)
                        nsmodel.save()
                    
                    for k in range(len(listass)) :

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
                        #we create the link between ns and assumptions
                        nsass = NsToAssumptions(filename=nsInstance,id_assumptions=idAs)
                        nsass.save()
                    nbinsert +=  1
                    inserted.append(filename)
                #message for the user 
                mes = "You inserted "+str(nbinsert)+"/"+str(len(d)-1)+" elements"
                mes2 = "Element inserted :"+str(inserted)
                mes3 = "Element not inserted: "+str(notinserted)
                messages.success(request, mes)
                messages.success(request, mes2)
                messages.success(request, mes3)
        #for insertion manual we check the what the user wants to insert
        elif (request.POST.get('hid') == 'formAddName' ):
            
            #verifications of the value
            na =  request.POST.get('name')
            classdb = request.POST.get('class')

            if len(na) <= 0  or len(classdb) <= 0 :
                messages.error(request,"L'insertion de Name n'est pas correcte")
            else:
                nameS = request.POST.get('nameS')
                if len(nameS) < 1:
                    nameS = None

                classS = request.POST.get('classS')
                if len(classS) < 1 : 
                    classS = None

                r = request.POST.get('ra')
                if len(r)>1:
                    r = Decimal(r)
                else:
                    r = None

                dec = request.POST.get('dec')
                if len(dec)>1:
                    dec = Decimal(dec)
                else:
                    dec = None

                loc = request.POST.get('localisationfile')
                if len(loc)<1:
                    loc = None

                dat = request.POST.get('eventdate')
                if len(dat)<1:
                    dat = None

                if (NameNs.objects.filter(namedb=na, classdb=classdb, namesimbad=nameS, classsimbad=classS, ra=r, declination=dec, localisationfile=loc, eventdate=dat)):  
                
                    mess = "Name already exists"
                    messages.error(request,"Name already exists")
                else:
                    #we create the new name
                    name = NameNs(namedb=na, classdb=classdb, namesimbad=nameS, classsimbad=classS, ra=r, declination=dec, localisationfile=loc, eventdate=dat)
                    name.save()

                    #to write in the log file
                    fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                    wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(name)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()
                
     #same things for ref
    if (request.POST.get('hid') == 'formAddRef' ):

        auth = request.POST.get('author')

        year = request.POST.get('refyear')

        short = request.POST.get('short')

        bibtex = request.POST.get('bibtex')

        doi = request.POST.get('doi')

        if len(auth)<= 0 or len(year)<=0 or len(short)<=0 or len(bibtex)<=0 or len(doi)<=0:
            messages.error(request,"L'insertion de Ref n'est pas correct")
        else:
            repdoi = request.POST.get('repositorydoi')
            if len(repdoi)<1:
                repdoi = None

            datal = request.POST.get('datalink')
            if len(datal)<1:
                datal = None
            
            if (RefNs.objects.filter(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)):  
                messages.error(request,"Ref already exists")
            else:
                ref = RefNs(author=auth, refyear=year, short=short, bibtex=bibtex, doi=doi,repositorydoi=repdoi ,datalink=datal)
                ref.save()

                fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(ref)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()

    #when the user validete the insertion 
    if (request.POST.get('insert')):

        #we verify all the values
        insert = json.loads(request.POST.get('insert'))

        # TODO:  Fix these conditions:  for ex with:   insert['filepath'] is ''
        if((len(insert['filename'])<= 0) or (len(insert['filepath'])<=0 )):
            mess = "/!\ ERROR /!\ : Please enter a Filename or/and a Filepath"
            return HttpResponse(json.dumps(mess), content_type='application/json',)

        elif((insert['name'] == "opt") or (insert['ref']== 'opt')) :
            mess = "/!\ ERROR /!\ : Please select a Name or/and a Ref"
            return HttpResponse(json.dumps(mess), content_type='application/json',)
        
        elif((len(insert['method']['methodS'])<= 0) or (len(insert['method']['methodD'])<=0 ) or (len(insert['method']['methodP'])<=0 ) ):
            mess = "/!\ ERROR /!\ : Please enter a valid Method"
            return HttpResponse(json.dumps(mess), content_type='application/json',)
        
        elif((len(insert['constrain']['constrainVer'])<= 0)):
            mess = "/!\ ERROR /!\ : Please enter a valid Constrain"     
            return HttpResponse(json.dumps(mess), content_type='application/json',)
            
        else:

            ref = RefNs.objects.get(id_ref=insert['ref'])
            name = NameNs.objects.get(id_name=insert['name'])
            
            #we check if method and constrain already exist
            if (MethodNs.objects.filter(method =insert['method']['methodN'], method_specific =insert['method']['methodS'],
                               datadate = insert['method']['methodD'],processinfinfo =insert['method']['methodP'])):  
                
                methodId=MethodNs.objects.filter(method =insert['method']['methodN'], method_specific =insert['method']['methodS'],
                               datadate = insert['method']['methodD'],processinfinfo =insert['method']['methodP'])
            else:
                method = MethodNs(method =insert['method']['methodN'], method_specific =insert['method']['methodS'],
                               datadate = insert['method']['methodD'],processinfinfo =insert['method']['methodP'])
                method.save()
                methodId = MethodNs.objects.latest('id_method')

                fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n',str(method)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()


            if (ConstrainNs.objects.filter(constraintype =insert['constrain']['constrainT'] , constrainvariable = insert['constrain']['constrainV'],
                                    constrainversion = insert['constrain']['constrainVer'])):  
                    
                constrainId=ConstrainNs.objects.filter(constraintype =insert['constrain']['constrainT'] , constrainvariable = insert['constrain']['constrainV'],
                                    constrainversion = insert['constrain']['constrainVer'])
            else:
                constrain = ConstrainNs(constraintype =insert['constrain']['constrainT'] , constrainvariable = insert['constrain']['constrainV'],
                                    constrainversion = insert['constrain']['constrainVer'])
                constrain.save()
                constrainId = ConstrainNs.objects.latest('id_constrain')

                fichierlog = open('web_app\compare\static\compare\log.txt', "a")
                wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n',str(constrain)+'\n\n']
                fichierlog.writelines(wri)
                fichierlog.close()
        
            #we create the new ns with all the field
            ns = Ns(filename=insert['filename'],filepath=insert['filepath'], id_ref = ref, id_name = name, id_method = methodId, id_constrain = constrainId)
            ns.save()

        if(len(insert['model']) > 0):

            ns = Ns.objects.get(filename=insert['filename'])
            #for all the model we verify the value and create the object , if alreday exiqt we linked it , same as the others
            for mod in insert['model']:

                if(len(insert['model'][mod][0]) < 1 ):
                    insert['model'][mod][0] = None

                if(len(insert['model'][mod][1]) < 1 ):
                    insert['model'][mod][1] = None

                if(len(insert['model'][mod][2]) < 1 ):
                    insert['model'][mod][2] = None

                if(len(insert['model'][mod][3]) < 1 ):
                    insert['model'][mod][3] = None


                if (ModelNs.objects.filter(dependenciesprimary=insert['model'][mod][0],
                                           dependenciessecondary=insert['model'][mod][1],
                                           dependenciesdescription=insert['model'][mod][2],
                                           dependenciesreferences=insert['model'][mod][3])):
                    
                    modelId=ModelNs.objects.filter(dependenciesprimary=insert['model'][mod][0],
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
                    wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n',str(model)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                nsmodel = NsToModel(filename = ns , id_model = modelId)
                nsmodel.save()
    
        if(len(insert['assumptions']) > 0):

            ns = Ns.objects.get(filename=insert['filename'])
            #Same for assumptions
            for ass in insert['assumptions']:

                if(len(insert['assumptions'][ass][0]) < 1 ):
                    insert['assumptions'][ass][0] = None

                if(len(insert['assumptions'][ass][1]) < 1 ):
                    insert['assumptions'][ass][1] = None
                
                if(len(insert['assumptions'][ass][2]) < 1 ):
                    insert['assumptions'][ass][2] = None

                if(len(insert['massumptionsodel'][ass][3]) < 1 ):
                    insert['assumptions'][ass][3] = None

                if (AssumptionsNs.objects.filter(assumptionsprimary=insert['assumptions'][ass][0],
                                                 assumptionssecondary=insert['assumptions'][ass][1],
                                                 assumptionsdescription=insert['assumptions'][ass][2],
                                                 assumptionsreferences=insert['assumptions'][ass][3])):
                    
                    assumptionsId=AssumptionsNs.objects.filter(assumptionsprimary=insert['assumptions'][ass][0],
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
                    wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n',str(assumptions)+'\n\n']
                    fichierlog.writelines(wri)
                    fichierlog.close()

                nsass = NsToAssumptions(filename=ns, id_assumptions=assumptionsId)
                nsass.save()

        fichierlog = open('web_app\compare\static\compare\log.txt', "a")
        wri = ['User:',str(request.user.get_username())+'\n','Date:',str(datetime.datetime.now())+'\n','Content:',str(ns)+'\n\n']
        fichierlog.writelines(wri)
        fichierlog.close()   

        redirect = 'add'
        return HttpResponse(json.dumps(redirect), content_type='application/json',)
                    
    #we select the value for the dropdown list 
    group = request.user.groups.values_list('name',flat = True)
    groupList = list(group)

    queryall = Ns.objects.select_related().all()

    queryname = NameNs.objects.filter(classdb__in = group)

    queryref = RefNs.objects.all().distinct()

    methodoptions = MethodNs.method.field.choices
    listmethod =[]
    for mo in methodoptions:
        listmethod.append(mo[0])

    constrainoptions = ConstrainNs.constraintype.field.choices
    listconstrain =[]
    for co in constrainoptions:
        listconstrain.append(co[0])

    constrainvar = ConstrainNs.constrainvariable.field.choices
    listconstrainvar =[]
    for cov in constrainvar:
        listconstrainvar.append(cov[0])

    query = {
        "queryall":queryall,
        "queryname":queryname ,
        'queryref':queryref,
        'groupList' : groupList,
        'listmethod' :listmethod,
        'listconstrain':listconstrain,
        'listconstrainvar':listconstrainvar
                 }
    return render(request, "compare/insert.html", query)  

def info(request):  
    return render(request, "compare/info.html",)