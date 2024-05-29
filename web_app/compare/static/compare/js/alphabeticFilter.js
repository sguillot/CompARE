/**
 * Resets the sorting icons for all table columns except the one currently sorted.
 *
 * @param {HTMLElement} currentIcon - The icon element representing the currently sorted column.
 */
function resetSortIcons(currentIcon) {
    var sortIcons = document.querySelectorAll('.sort-icon');
    sortIcons.forEach(function(icon) {
        if (icon !== currentIcon) {
            icon.textContent = '↕';
        }
    });
}

/**
 * Sorts the table rows based on the content of the specified column.
 * Toggles between ascending and descending sorting order on successive clicks.
 *
 * @param {number} columnIndex - The index of the column to be sorted.
 * @param {HTMLElement} iconElement - The icon element representing the sorting state of the column.
 */
function sortTable(columnIndex, iconElement) {

    var table, rows, switching, i, x, y, shouldSwitch, dir, switchcount = 0;
    table = document.querySelector(".tab table");
    switching = true;

    // Set the sorting direction to ascending:
    dir = "asc"; 

    // Reset all sort icons except the current one
    resetSortIcons(iconElement);
    
    /* Make a loop that will continue until
    no switching has been done: */
    while (switching) {
        // Start by saying: no switching is done:
        switching = false;
        rows = table.rows;
        /* Loop through all table rows (except the
        first, which contains table headers): */
        for (i = 1; i < (rows.length - 1); i++) {
            // Start by saying there should be no switching:
            shouldSwitch = false;
            /* Get the two elements you want to compare,
            one from current row and one from the next: */
            x = rows[i].getElementsByTagName("TD")[columnIndex];
            y = rows[i + 1].getElementsByTagName("TD")[columnIndex];
            /* Check if the two rows should switch place,
            based on the direction, asc or desc: */
            if (dir == "asc") {
                if (x.innerHTML.toLowerCase() > y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            } else if (dir == "desc") {
                if (x.innerHTML.toLowerCase() < y.innerHTML.toLowerCase()) {
                    // If so, mark as a switch and break the loop:
                    shouldSwitch = true;
                    break;
                }
            }
        }
        if (shouldSwitch) {
            /* If a switch has been marked, make the switch
            and mark that a switch has been done: */
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
            // Each time a switch is done, increase this count by 1:
            switchcount ++; 
        } else {
            /* If no switching has been done AND the direction is "asc",
            set the direction to "desc" and run the while loop again. */
            if (switchcount == 0 && dir == "asc") {
                dir = "desc";
                switching = true;
            }
        }
    }

    // Toggle arrow icons
    var arrowUp = '↑';
    var arrowDown = '↓';
    var currentArrow = iconElement.textContent.trim();
    var newArrow = currentArrow === arrowUp ? arrowDown : arrowUp;
    iconElement.textContent = newArrow;
}