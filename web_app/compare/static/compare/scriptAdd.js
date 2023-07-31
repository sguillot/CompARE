function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function showHide(div){
    var iddiv = document.getElementById(div.className)
    if (iddiv.style.display !== 'block') {
        iddiv.style.display = 'block';
    }
    else {
        iddiv.style.display = 'none';
    }

}

  function returndep(){
    document.getElementById('modelTable').deleteRow(-1)
  }

  function returnass(){
    document.getElementById('assumptionTable').deleteRow(-1)
  }


function changeFuncName(value){
    if(value === 'opt'){
        return
    }else{
        $.ajax({
            url: '',
            type: 'GET',
            data:{idname: value},
            success: function(querynametab) {

                $("#nameTable tr").remove() 
                data = querynametab[0]
                let table = document.getElementById("nameTable")

                let row  = table.insertRow()

                let name = row.insertCell(0)
                name.innerHTML = data.namedb

                let classns = row.insertCell(1)
                classns.innerHTML = data.classdb
                    
                let namesim = row.insertCell(2)
                namesim.innerHTML = data.namesimbad

                let classim = row.insertCell(3)
                classim.innerHTML = data.classsimbad

                let r = row.insertCell(4)
                r.innerHTML = data.ra

                let dec = row.insertCell(5)
                dec.innerHTML = data.declination

                let loc = row.insertCell(6)
                loc.innerHTML = data.localisationfile

                let event = row.insertCell(7)
                event.innerHTML = data.eventdate
            }
        })
    }
}

function changeFuncRef(value){
    if(value === 'opt'){
        return
    }else{
        $.ajax({
            url: '',
            type: 'GET',
            data:{idref: value},
            success: function(queryconstab) {
                $("#refTable tr").remove() 
                data = queryconstab[0]
                let table = document.getElementById("refTable")

                let row  = table.insertRow()

                let authorref = row.insertCell(0)
                authorref.innerHTML = data.author

                let year = row.insertCell(1)
                year.innerHTML = data.refyear
                    
                let shortref = row.insertCell(2)
                shortref.innerHTML = data.short

                let rep = row.insertCell(3)
                rep.innerHTML = data.repositorydoi

                let link = row.insertCell(4)
                link.innerHTML = data.datalink
            }
        })
    }
}

function createNs(){
    insertvalue={}
    insertvalue['filename']=document.getElementById('filename').value
    insertvalue['filepath']=document.getElementById('filepath').value
    insertvalue['name']=document.getElementById('nList').value
    insertvalue['method']=getMethod()
    insertvalue['constrain']=getConstrain()
    insertvalue['ref']=document.getElementById('rList').value
    insertvalue['model']= selecttab('modelTable')
    insertvalue['assumptions']= selecttab('assumptionTable')
    const csrftoken = getCookie('csrftoken');
   
    $.ajax({
        url: '',
        type: 'POST',
        data:{insert:JSON.stringify(insertvalue)},
        headers: {'X-CSRFToken': csrftoken},
        success: function(mess) {
            if (mess === 'add'){
                window.location.replace('')
            }else{
                document.documentElement.scrollTop = 0;
                document.getElementById('test').innerHTML = mess
                document.getElementById('errorInsert').style.display = 'block';
            }
        }
    })

}

function selecttab(tab){
    
    var tabdict = {}
    for (let i = 0; i <document.getElementById(tab).rows.length; i++) {
        var select = []
        for (let j = 0; j <document.getElementById(tab).rows[i].cells.length; j++){
            select.push(document.getElementById(tab).rows[i].cells[j].innerHTML)
        }
        tabdict[i]=select
    }
    return tabdict
}

function inTableAss(){

    let table = document.getElementById("assumptionTable")

    dataprimary =  document.getElementById('assumptionsprimary').value
    datasecondary =  document.getElementById('assumptionssecondary').value
    datadescription =  document.getElementById('assumptionsdescription').value


    let row  = table.insertRow()
        
    let more = row.insertCell(0)
    more.innerHTML = dataprimary
        
    let name = row.insertCell(1)
    name.innerHTML = datasecondary
                    
    let classdb = row.insertCell(2)
    classdb.innerHTML = datadescription
 
    document.getElementById('assumptionsprimary').value = ''
    document.getElementById('assumptionssecondary').value = ''
    document.getElementById('assumptionsdescription').value = ''

}

function inTableMod(){

    let table = document.getElementById("modelTable")

    let dataprimary =  document.getElementById('dependenciesprimary').value
    let datasecondary =  document.getElementById('dependenciessecondary').value
    let datadescription =  document.getElementById('dependenciesdescription').value
    let MoCaveatsRef = document.getElementById('MocaveatsReferences').value

    let row  = table.insertRow()
        
    let moPri = row.insertCell(0)
    moPri.innerHTML = dataprimary
        
    let moSec = row.insertCell(1)
    moSec.innerHTML = datasecondary
                    
    let desc = row.insertCell(2)
    desc.innerHTML = datadescription

    let MoCaveats = row.insertCell(3)
    MoCaveats.innerHTML = MoCaveatsRef
 
    document.getElementById('dependenciesprimary').value = ''
    document.getElementById('dependenciessecondary').value = ''
    document.getElementById('dependenciesdescription').value = ''
    document.getElementById('MocaveatsReferences').value = ''

}

function getConstrain(){
    var conslist = {}
    conslist['constrainT']=document.getElementById('selConsT').value
    conslist['constrainV']=document.getElementById('selConsV').value
    conslist['constrainVer']=document.getElementById('consVers').value
    return conslist
}

function getMethod() {
    var methlist = {}
    methlist['methodN']=document.getElementById('selMethN').value
    methlist['methodS']=document.getElementById('methSpe').value
    methlist['methodD']=document.getElementById('methodD').value
    methlist['methodP']=document.getElementById('methodP').value
    return methlist
}