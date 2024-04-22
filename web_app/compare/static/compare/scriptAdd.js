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
    var iddiv = document.getElementById(div.className);
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

function loadFile(event){

    // Prevents page reloading
    event.preventDefault(); 

    var inputFile = document.getElementById('file-load');

    // Retrieves file and file name + processes file extension
    var selectedFile = inputFile.files[0];
    var selectedFilename = inputFile.files[0].name;
    var h5Filename = selectedFilename.replace(/\.[^/.]+$/, "") + ".h5";

    const csrftoken = getCookie('csrftoken');

    // Stores for a key, the "File" object in a FormData object
    var formData = new FormData();
    formData.append('filetoload', selectedFile);
   
    $.ajax({
        url: '',
        type: 'POST',
        data: formData,
        processData: false,
        contentType: false,
        headers: {'X-CSRFToken': csrftoken},
        success: function(message) {
            if (message.startsWith("The")) {
                // Display the HttpResponse message in the appropriate HTML element
                document.documentElement.scrollTop = 0;
                document.getElementById('test').innerHTML = message;
                document.getElementById('errorInsert').style.display = 'block';
            } else {
                // Update input value with file name
                document.getElementById('filename').value = selectedFilename;
                document.getElementById('h5filename').value = h5Filename;
                // Activate all elements with the enabledinput class
                enableInputs();
            }
        }
    });
}

function enableInputs() {

    document.getElementById('createDep').disabled = false; 
    document.getElementById('deleteDep').disabled = false; 
    document.getElementById('createAss').disabled = false;
    document.getElementById('deleteAss').disabled = false;

    var elements = document.querySelectorAll('.enabledinput');
    elements.forEach(function(element) {
        element.disabled = false;
    });
}

function createNs(){
    insertvalue={}
    insertvalue['filename']=document.getElementById('filename').value
    insertvalue['h5filename']=document.getElementById('h5filename').value
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
                alert('The creation has been completed.');
            } else if (mess) {
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
    datareference =  document.getElementById('assumptionsreferences').value

    let row  = table.insertRow()
        
    let more = row.insertCell(0)
    more.innerHTML = dataprimary
        
    let name = row.insertCell(1)
    name.innerHTML = datasecondary
                    
    let assdesc = row.insertCell(2)
    assdesc.innerHTML = datadescription

    let assref = row.insertCell(3)
    assref.innerHTML = datareference

    document.getElementById('assumptionsprimary').value = ''
    document.getElementById('assumptionssecondary').value = ''
    document.getElementById('assumptionsdescription').value = ''
    document.getElementById('assumptionsreferences').value = ''

}

function inTableMod(){

    let table = document.getElementById("modelTable")

    let dataprimary =  document.getElementById('dependenciesprimary').value
    let datasecondary =  document.getElementById('dependenciessecondary').value
    let datadescription =  document.getElementById('dependenciesdescription').value
    let datareferences = document.getElementById('dependenciesreferences').value

    let row  = table.insertRow()

    let moPri = row.insertCell(0)
    moPri.innerHTML = dataprimary

    let moSec = row.insertCell(1)
    moSec.innerHTML = datasecondary

    let desc = row.insertCell(2)
    desc.innerHTML = datadescription

    let depref = row.insertCell(3)
    depref.innerHTML = datareferences

    document.getElementById('dependenciesprimary').value = ''
    document.getElementById('dependenciessecondary').value = ''
    document.getElementById('dependenciesdescription').value = ''
    document.getElementById('dependenciesreferences').value = ''

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