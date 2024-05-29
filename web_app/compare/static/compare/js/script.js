// Execute the function once on page load
document.addEventListener("DOMContentLoaded", adjustNavbarDisplay);

// Listen to the window resizing event
window.addEventListener("resize", adjustNavbarDisplay);

/** 
 * When a checkboxes of a side panel is checked 
 * We get checkboxes checked
 * We get all filter 
 * We call the AjaxRequest function 
 */
$(document).ready(function(){
    var checkList = [];
    $(document).on("click", 'input.check[type="checkbox"]', function(){
      var value = $(this).val();
      if($(this).is(":checked")){
        checkList.push(value);
      } else {
        var index = checkList.indexOf(value);
        if (index > -1) {
          checkList.splice(index, 1);
        }
      }  
      var select = getSelect();
      var search = getSearch();
      ajaxRequest(checkList , select , search);
    })
})

/**
 * Adjusts the display of the navigation bar based on the screen size.
 */
function adjustNavbarDisplay() {
  // Retrieves the navigation links element
  var links = document.getElementById("navbar-links");
  // Adjusts display based on screen width
  if (window.innerWidth > 1400) {
      links.style.display = 'flex';
  } else {
      links.style.display = 'none';
  }
}

/**
 * Toggles the visibility of the menu in the navbar.
 */
function toggleMenu() {
  var navbar = document.querySelector('.navbar');
  var links = document.querySelector(".navbar-links");
  var hamburger = document.getElementById("hamburger-menu");

  if (links.style.display === "flex") {
    // Hides the menu and adjusts hamburger position
    links.style.display = "none";
    navbar.insertBefore(hamburger, document.querySelector('.navbar-Compare'));
    hamburger.style.marginLeft = "20px";
  } else {
    // Displays the menu and adjusts hamburger position
    links.insertBefore(hamburger, links.firstChild);
    hamburger.style.margin = "0px 0px 10px 0px";
    links.style.display = "flex";
  }
}

/** 
 * Select all checked checkboxes off the table 
 * Return a list of their values
 */
function getCheckboxesTab(){
  var checkboxes = document.querySelectorAll('input[type="checkbox"].dwnl:checked');
  var values = [];
  checkboxes.forEach((checkbox) => {
    values.push(checkbox.value);
  });
  return(values);
}

/**
 * Select all checked checkboxes off the side panel 
 * Return a list
 */
function getCheckboxesFilter(){
  var checkboxes = document.querySelectorAll('input[type="checkbox"].check:checked');
  var values = [];
  checkboxes.forEach((checkbox) => {
    values.push(checkbox.value);
  });
  return(values);
}

/** 
 * Get the value of the searchBar 
 * Return a string 
 */
function getSearch(){
  var searchString = document.getElementById('Search').value;
  return (searchString);
}

/** 
 * Get the value of all the selectBox
 * Return a list of dictionnary 
 */
function getSelect(){
  var selectorValues = {}
  const ListOptions = ["list_methods","list_variable","list_constrain_type",
                        "list_dep_primary","list_dep_secondary",
                        "list_assumptions_primary","list_assumptions_secondary"];
  ListOptions.forEach(lO => {
    var select = [];
    var selector = document.getElementById(lO);
    var selectorList = selector.selectedOptions;  
    for (let i = 0; i < selectorList.length; i++) {
      select.push(selectorList[i].value);
    }
    selectorValues[lO] = select;
  });
  return(selectorValues);
}


/**
 * Get the value of checkboxes checked
 * We sent to the views the filename and it downloads the selected files
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

/**
 * Initiates the download of a file with the specified filename.
 * Creates an anchor element, sets the download URL and filename, 
 * and triggers a click event to start the download.
 *
 * @param {string} h5_filename - The name of the file to be downloaded.
 */
function downloadFilename(h5_filename) {
  var link = document.createElement('a');
  link.href = '/static/h5/' + h5_filename;
  link.download = h5_filename;
  link.click();
}

/** 
 * Get the value of checkboxes checked
 * We sent to the views the filename 
 * We get bibtex
 * Download the file created
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

/**
 * Show one or more plots depending on the selected files (checkboxes)
 */
function showPlot() {
  var selectedFiles = getCheckboxesTab();
    
  if (selectedFiles.length === 0) {
    alert('Please select at least one file.');
    return;
  }

  var encodedFiles = selectedFiles.map(function(fileName) {
    return encodeURIComponent(fileName);
  });

  $.ajax({
      url: '/generate_plot/',
      type: 'GET',
      data: { files: selectedFiles },
      dataType: 'html',
      success: function(response) {
          url = '/generate_plot/?files[]=' + encodedFiles.join('&files[]=');
          window.open(url, '_blank');
      },
      error: function(xhr, status, error) {
          console.error('Error generating plot:', error);
      }
  });
}

/**
 * Resets the display of previously selected filters
 * Returns the table display to its initial state
 */
function resetFilters() {
  // Reset checkboxes
  var checkboxes = document.querySelectorAll('input[type="checkbox"].check:checked');
  checkboxes.forEach((checkbox) => {
      checkbox.checked = false;
  });

  // Reset selectors
  const ListOptions = ["list_methods", "list_variable", "list_constrain_type", "list_dep_primary", "list_dep_secondary", "list_assumptions_primary", "list_assumptions_secondary"];
  ListOptions.forEach((lO) => {
      var selector = document.getElementById(lO);
      selector.selectedIndex = -1; // Reset to first option
  });

  // Reset search area
  document.getElementById('Search').value = '';

  // Click on the validation button to reset the table
  document.getElementById('vld').click();
}


/**
 * When user click on the magnifier
 * Select all filter
 * We call the ajaxRequest function
 */
function searchFilter(){
  var searchCheck = getCheckboxesFilter();
  var select = getSelect();
  var search = getSearch();
  ajaxRequest(searchCheck , select , search);
}

/**
 * Populates a <select> element with unique options.
 * Checks each option for duplicates and adds them if they don't already exist.
 *
 * @param {HTMLSelectElement} select - The <select> element to fill.
 * @param {Array<string>} options - The array of options to be added.
 */
function populateSelect(select, options) {

  // Then add the sorted options to the selector
  options.forEach(option => {
    // Check if the option already exists in the selector
    if (!select.querySelector("option[value='" + option + "']")) {
      select.innerHTML += "<option value='" + option + "'>" + option + "</option>";
    }
  });
}

/**
 * Sorts the options of a given <select> element in alphabetical order.
 * The sorting is done based on locale comparison with French settings.
 *
 * @param {HTMLSelectElement} select - The <select> element whose options need to be sorted.
 */
function sortSelect(select) {
  var options = Array.from(select.options).map(option => option.value);
  options.sort((a, b) => a.localeCompare(b, 'fr', { sensitivity: 'base' }));
  select.innerHTML = '';
  options.forEach(option => {
    select.innerHTML += "<option value='" + option + "'>" + option + "</option>";
  });
}

/**
 * Loads a specific page via an AJAX request.
 * Updates the content of the table and pagination elements based on the response.
 *
 * @param {number} page - The page number to be loaded.
 */
function loadPage(page) {
  $.ajax({
      url: '', 
      data: {
          'page': page
      },
      success: function(data) {

          if(data.table != null) {
              $('#firstTable').html($(data.table).find('#firstTable').html());
              $('.pagination').html($(data.table).find('.pagination').html());
          }
      }
  });
}

/**
 * Sends an AJAX GET request with the provided checklist, selected options, and search string.
 * Updates the table and pagination elements based on the response data.
 *
 * @param {Array} checkList - An array of selected checkbox values.
 * @param {Object} select - The selected options.
 * @param {string} search - The search string.
 */
function ajaxRequest(checkList , select , search){
  var jsonCheckList = JSON.stringify(checkList);
  var stringSearch = search;
  var jsonSelect = JSON.stringify(select);
  $.ajax({
    url: '',
    type: 'GET',
    data:{dataCheckList:jsonCheckList,
          dataSearch:stringSearch,
          dataSelect:jsonSelect},
    success: function(data) {

      $("#firstTable tr").remove();

      if(data.length !== data[0].countns) {
        document.querySelector('.pagination').style.display = 'none';
      } else {
        document.querySelector('.pagination').style.display = 'block';
      }

      // Get all the elements that we need
      let table = document.getElementById("firstTable");
      
      let selectIds = ["list_methods", "list_variable", "list_constrain_type", "list_dep_primary", "list_dep_secondary", "list_assumptions_primary", "list_assumptions_secondary"];

      selectIds.forEach(id => {
        let select = document.getElementById(id);
        while (select.firstChild) {
          select.removeChild(select.firstChild);
        }
      });

      // Filter dynamically the values
      data.forEach(d => {
        // For the "more filters" menu
        populateSelect(list_methods, [d.method]);
        populateSelect(list_variable, [d.constrainvariable]);
        populateSelect(list_constrain_type, [d.constraintype]);
        populateSelect(list_dep_primary, d.modelprimary);
        populateSelect(list_dep_secondary, d.modelsecondary);
        populateSelect(list_assumptions_primary, d.assumptionsprimary);
        populateSelect(list_assumptions_secondary, d.assumptionssecondary);

        // Sort the select options alphabetically
        sortSelect(list_methods);
        sortSelect(list_variable);
        sortSelect(list_constrain_type);
        sortSelect(list_dep_primary);
        sortSelect(list_dep_secondary);
        sortSelect(list_assumptions_primary);
        sortSelect(list_assumptions_secondary);

        // For the table
        let row  = table.insertRow();
        let more = row.insertCell(0);
        // We generate the part of the static URL before the specified path
        more.innerHTML = "<a href=detail/" + d.filename + " target='_blank'><img src='" + baseStaticURL + "compare/images/plus.svg' alt='icon more' width='30em' /></a>";

        let name = row.insertCell(1);
        name.innerHTML = d.namedb;
              
        let classdb = row.insertCell(2);
        classdb.innerHTML = d.classdb;

        let method = row.insertCell(3);
        method.innerHTML = d.method;

        let methodspe = row.insertCell(4);
        methodspe.innerHTML = d.method_specific;

        let constrainty = row.insertCell(5);
        constrainty.innerHTML = d.constraintype;

        let constrainver = row.insertCell(6);
        constrainver.innerHTML = d.constrainversion;

        let constrainvar = row.insertCell(7);
        constrainvar.innerHTML = d.constrainvariable;

        let model = row.insertCell(8);
        if (typeof d.model !== 'undefined') {
          d.model.forEach(mod_text => {
          model.insertAdjacentHTML("beforeend",mod_text);
        });
        }
        
        let assump = row.insertCell(9);
        if (typeof d.assumptions !== 'undefined') {
          d.assumptions.forEach(ass_text => {
            assump.insertAdjacentHTML("beforeend", ass_text);
          });
        }

        let ref = row.insertCell(10);
        ref.innerHTML = "<a href=https://doi.org/"+d.doi+" target='_blank'>"+ d.author +" "+ d.year +"</a>";

        let download = row.insertCell(11);
      
        if(d.result_h5 === true) {
          // We also generate the part of the static URL before the specified path
          download.innerHTML = "<a href='" + baseStaticURL + "h5/" + d.h5_filename + "' download='" + d.h5_filename + "'>" + "<img src='" + baseStaticURL + "compare/images/download.svg' alt='icon download' width='30em' />" + "</a>";
        }

        let checkdo = row.insertCell(12);
        checkdo.innerHTML = "<td><input type='checkbox' value="+ d.h5_filename+" class='dwnl' name='che'> </td>";

      })
    }
  })
}

/**
 * Toggles the display of a div element between 'block' and 'none'.
 * The target div is identified by its class name.
 *
 * @param {HTMLElement} div - The div element whose display is to be toggled.
 */
function hideShow(div) {
  var iddiv = document.getElementById(div.className)
    if (iddiv.style.display !== 'block') {
        iddiv.style.display = 'block';
    }
    else {
        iddiv.style.display = 'none';
    }
}

/**
 * Selects all checkboxes with the name 'che'.
 * Sets their checked property to true.
 */
function selectall(){
  var tabcheck = document.getElementsByName("che")
  for (var i = 0; i < tabcheck.length; i++) {
    tabcheck[i].checked = true;
  }
}

/**
 * Unselects all checkboxes with the name 'che'.
 * Sets their checked property to false.
 */
function unselectall(){
  var tabcheck = document.getElementsByName("che")
  for (var i = 0; i < tabcheck.length; i++) {
    tabcheck[i].checked = false;
  }
}

// Details

/**
 * Retrieves the value of a specified cookie by name.
 * Searches through the document's cookies and returns the value if found.
 *
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} The value of the cookie if found, or null if not found.
 */
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

/**
 * Confirms the deletion of a file and sends an AJAX POST request to delete it.
 * Prompts the user for confirmation, retrieves the CSRF token, and sends the filename for deletion.
 * If the deletion is successful, redirects the user to the parent directory.
 */
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

// Modify

/**
 * Enables all input elements with the same class name as the provided element.
 *
 * @param {HTMLElement} id - An element whose class name is used to select inputs to be enabled.
 */
function enable(id) {
  var inp =document.getElementsByClassName(id.className);
  for (let index = 0; index < inp.length; index++) {
    inp[index].disabled = false;
  }
}