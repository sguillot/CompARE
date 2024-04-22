   
  /*
  When a checkboxes of a side panel is checked 
  We get checkboxes checked
  We get all filter 
  We call the AjaxRequest function 
  */
$(document).ready(function(){
    var checkList = []
    $(document).on("click", 'input.check[type="checkbox"]', function(){
      var value = $(this).val();
      if($(this).is(":checked")){
        checkList.push(value)
      } else {
        var index = checkList.indexOf(value);
        if (index > -1) {
          checkList.splice(index, 1);
        }
      }  
      var select = getSelect()
      var search = getSearch()
      ajaxRequest(checkList , select , search);
    })
})


/* 
Select all checked checkboxes off the table 
Return a list
*/
function getCheckboxesTab(){
  var checkboxes = document.querySelectorAll('input[type="checkbox"].dwnl:checked');
  var values = [];
  checkboxes.forEach((checkbox) => {
    values.push(checkbox.value);
  });
  return(values)
}

/* 
Select all checked checkboxes off the side panel 
Return a list
*/
function getCheckboxesFilter(){
  var checkboxes = document.querySelectorAll('input[type="checkbox"].check:checked');
  var values = [];
  checkboxes.forEach((checkbox) => {
    values.push(checkbox.value);
  });
  return(values)
}

/*
Get the value of the searchBar 
Return a string 
*/
function getSearch(){
  var searchString = document.getElementById('Search').value
  return (searchString)
}


/*
Get the value of all the selectBox
Return a list of dictionnary 
*/
function getSelect(){
  var selectorValues = {}
  const ListOptions = ["list_methods","list_variable","list_constrain_type",
                        "list_dep_primary","list_dep_secondary",
                        "list_assumptions_primary","list_assumptions_secondary"]
  ListOptions.forEach(lO => {
    var select = []
    var selector = document.getElementById(lO)
    var selectorList = selector.selectedOptions;  
    for (let i = 0; i < selectorList.length; i++) {
      select.push(selectorList[i].value)
    }
    selectorValues[lO] = select
  });
  return(selectorValues)
}


/*
Get the value of checkboxes checked
We sent to the views the filename and it downloads the selected files
*/
function downloadFiles() {
  var checkboxes = document.querySelectorAll('.dwnl:checked');
  if (checkboxes.length === 0) {
      alert('Please select at least one file to download.');
      return;
  }

  var filenames = [];
  checkboxes.forEach(function(checkbox) {
      filenames.push(checkbox.value);
  });

  var filenamesJSON = JSON.stringify(filenames);
  $.ajax({
    url: '/visu/',
    type: 'GET',
    data: { filedwnl: filenamesJSON },
    xhrFields: {
      responseType: 'blob' // To manage binary data (the ZIP file)
    },
    success: function(response) {
      var blob = new Blob([response], { type: 'application/zip' });
      var link = document.createElement('a');
      link.href = window.URL.createObjectURL(blob);
      link.download = 'files.zip';
      link.click();
    },
    error: function(xhr, status, error) {
      alert('Error downloading file(s). Please try again.');
    }
  });
}

/*
Get the filename which allows to download the file
*/
function downloadFilename(filename) {
  var link = document.createElement('a');
  link.href = '/static/data/' + filename;
  link.download = filename;
  link.click();
}

/*
Get the value of checkboxes checked
We sent to the views the filename 
We get bibtex
Download the file created
*/
function bibtexFile() {
  var values = getCheckboxesTab();
  if (values.length === 0) {
      alert('Please select at least one file to download bibtex.');
      return;
  }

  var values2 = JSON.stringify(values);
  $.ajax({
    url: '/visu/',
    type: 'GET',
    data: { bibtexfile: values2 },
    success: function(data) {
      // Create a Blob object containing the data
      var blob = new Blob([data], { type: 'text/plain' });

      // Creating a URL object from a Blob
      var url = window.URL.createObjectURL(blob);

      // Create a <a> element to download the file
      var link = document.createElement('a');
      link.href = url;
      link.download = 'Bibtex.txt';
      // Add the <a> element to the page and click on it to start the download
      document.body.appendChild(link);
      link.click();

      // Clean up after downloading
      window.URL.revokeObjectURL(url);
      document.body.removeChild(link);
    }
  });
}


/* 
when user click on the magnifier
Select all filter
We call the ajaxRequest function
*/
function searchFilter(){
  var searchCheck = getCheckboxesFilter()
  var select = getSelect()
  var search = getSearch()
  ajaxRequest(searchCheck , select , search);
}


function ajaxRequest(checkList , select , search){
  var jsonCheckList = JSON.stringify(checkList);   
  var stringSearch = search
  var jsonSelect = JSON.stringify(select);
  $.ajax({
    url: '',
    type: 'GET',
    data:{dataCheckList:jsonCheckList,
          dataSearch:stringSearch,
          dataSelect:jsonSelect},
    success: function(data) {
      $("#firstTable tr").remove()
      $("#secondTable tr").remove()

      let table = document.getElementById("secondTable")
      data.forEach(d => {
        let row  = table.insertRow()

        let more = row.insertCell(0)
        // We generate the part of the static URL before the specified path
        more.innerHTML = "<a href=detail/" + d.filename + " target='_blank'><img src='" + baseStaticURL + "compare/plus.svg' alt='icon more' width='30em' /></a>"

        let name = row.insertCell(1)
        name.innerHTML = d.namedb
              
        let classdb = row.insertCell(2)
        classdb.innerHTML = d.classdb

        let method = row.insertCell(3)
        method.innerHTML = d.method

        let methodspe = row.insertCell(4)
        methodspe.innerHTML = d.method_specific

        let constrainvar = row.insertCell(5)
        constrainvar.innerHTML = d.constrainvariable + "<br>(v. " + d.constrainversion + ")"

        let model = row.insertCell(6)
        if (typeof d.model !== 'undefined') {
          d.model.forEach(mod_text => {
          model.insertAdjacentHTML("beforeend",mod_text);
        });
        }

        let assump = row.insertCell(7)
        if (typeof d.assumptions !== 'undefined') {
          d.assumptions.forEach(ass_text => {
            // assump.insertAdjacentHTML("beforeend", "<li><u>"+ass1+"</u>: "+ass2+"</li>");
            assump.insertAdjacentHTML("beforeend", ass_text);
          });
        }

        let ref = row.insertCell(8)
        ref.innerHTML = "<a href=https://doi.org/"+d.doi+" target='_blank'>"+ d.author +" "+ d.year +"</a>"

        let download = row.insertCell(9)
      
        // We also generate the part of the static URL before the specified path
        download.innerHTML = "<a href='" + baseStaticURL + "data/" + d.filename + "' download='" + d.filename + "'>" + "<img src='" + baseStaticURL + "compare/download.svg' alt='icon download' width='30em' />" + "</a>";

        let checkdo = row.insertCell(10)
        checkdo.innerHTML = "<td><input type='checkbox' value="+ d.filename+" class='dwnl' name='che'> </td>"

      })
    }
  })
}

function hideShow(div) {
  var iddiv = document.getElementById(div.className)
    if (iddiv.style.display !== 'block') {
        iddiv.style.display = 'block';
    }
    else {
        iddiv.style.display = 'none';
    }
}

function selectall(){
  var tabcheck = document.getElementsByName("che")
  for (var i = 0; i < tabcheck.length; i++) {
    tabcheck[i].checked = true;
  }
}

function unselectall(){
  var tabcheck = document.getElementsByName("che")
  for (var i = 0; i < tabcheck.length; i++) {
    tabcheck[i].checked = false;
  }
}


//details

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

function confirmDelete(){
  const csrftoken = getCookie('csrftoken');
  var filename = document.getElementById('btnremove').value
  var message = confirm("Are you sure to delete "+ filename)
  if (message === true ){
    $.ajax({
      url: '',
      type: 'POST',
      data:{filename:JSON.stringify(filename)},
      headers: {'X-CSRFToken': csrftoken},
      success: function(response) {
        if (response ==='yes'){
          window.location.replace('..');
        }
      }
    })
  }
}

//modify

function enable(id) {
  var inp =document.getElementsByClassName(id.className)
  for (let index = 0; index < inp.length; index++) {
    inp[index].disabled = false 
  }
}
