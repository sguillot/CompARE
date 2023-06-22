   
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
  const ListOptions = ["MethList","ConsVList","ConsTList","DepList","DepSList","AssList","Ass2List"]
  ListOptions.forEach(lO => {
    var select = []
    var selector = document.getElementById(lO)
    var selectorList = selector.selectedOptions;  
    for (let i = 0; i < selectorList.length; i++) {
      select.push(selectorList[i].value)
    }
    selectorValues[lO] = select
  });
  console.log(selectorValues)
  return(selectorValues)
}


/*
Get the value of checkboxes checked
We sent to the views the filename 
We get  the filepath
Download selected files
*/
function downloadFile(){
  var check = getCheckboxesTab();
  var checkString = JSON.stringify(check);  
  $.ajax({
    url: '',
    type: 'GET',
    data:{filedwnl: checkString},
    success: function(data) {
      data.forEach(path => {
        let linkpath = document.createElement("a");
        linkpath.href = path
        linkpath.download=""
        linkpath.click()
        linkpath.remove();
      });
    }
  })
}


/*
Get the value of checkboxes checked
We sent to the views the filename 
We get bibtex
Download the file created
*/
function bibtexFile(){
  var values = getCheckboxesTab()
  if(values.length >0){
    var values2 = JSON.stringify(values);  
    $.ajax({
      url: '',
      type: 'GET',
      data:{bibtexfile: values2},
      success: function(data) {
        var linkbib = document.createElement("a");
        linkbib.href = data;
        linkbib.download = "";
        linkbib.click();
        linkbib.remove()
      }
    })
}}


/* 
when user click on the loop
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
        more.innerHTML = "<a href=detail/"+d.filename+" target='_blank'><img src='../static/compare/plus.svg' alt='icon more' width='30em' /></a>"

        let name = row.insertCell(1)
        name.innerHTML = d.namedb
              
        let classdb = row.insertCell(2)
        classdb.innerHTML = d.classdb

        let method = row.insertCell(3)
        method.innerHTML = d.method

        let methodspe = row.insertCell(4)
        methodspe.innerHTML = d.method_specific

        let constrainty = row.insertCell(5)
        constrainty.innerHTML = d.constraintype

        let constrainver = row.insertCell(6)
        constrainver.innerHTML = d.constrainversion

        let constrainvar = row.insertCell(7)
        constrainvar.innerHTML = d.constrainvariable

        let model = row.insertCell(8)
        if (typeof d.model !== 'undefined') {
          d.model.forEach(mod => {
          model.insertAdjacentHTML("beforeend","<li>"+ mod +"</li>");
        });
        }
         
        
        let assump = row.insertCell(9)
        if (typeof d.assumptions !== 'undefined') {
          d.assumptions.forEach(ass => {
            assump.insertAdjacentHTML("beforeend", "<li>"+ ass +"</li>");
          });
        }

        let ref = row.insertCell(10)
        ref.innerHTML = "<a href="+d.doi+" target='_blank'>"+ d.author +" "+ d.year +"</a>"

        let download = row.insertCell(11)
        download.innerHTML = "<a href="+ d.filpath+" download> <img src='../static/compare/download.svg' alt='icon download' width='30em' /></a>"
        
        let checkdo = row.insertCell(12)
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

