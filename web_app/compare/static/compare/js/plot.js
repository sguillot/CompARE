// Event manager for checkboxes
$('.color-checkbox').each(function(index) {
    // Assign current index to checkbox value
    $(this).val(index);
    
}).change(function() {
    // Retrieve checkbox index
    var index = parseInt($(this).val());

    // Retrieve all <g> groups from the graph
    var groups = $('#plot-container').find('g.mpld3-paths > g');

    // Check if the checkbox is checked
    var isChecked = $(this).is(':checked');

    // Browse all groups
    groups.each(function() {
        // Retrieve paths within this group
        var paths = $(this).find('path.mpld3-path');

        // List the path indexes in this group
        paths.each(function() {

            var pathIndex = $(this).index();

            if(pathIndex === index) {
                var style = $(this).attr('style');
                var colorRegex = /stroke:#([0-9A-Fa-f]{6})/;

                var match = style.match(colorRegex);
                var correctMatch = "#" + match[1];

                if (!isChecked) {
                    // Comment the corresponding part in the path style
                    style = style.replace(colorRegex, '/* stroke:' + correctMatch + ' */');
                    
                    // Apply modified style to path
                    $(this).attr('style', style);
                } else {
                    // Remove the comment from the corresponding part in the path style
                    style = style.replace('/* stroke:' + correctMatch + ' */', 'stroke:' + correctMatch);
                    
                    // Apply modified style to path
                    $(this).attr('style', style);
                }
            }

        });
    });
});

$('.file-checkbox').each(function(index) {
    // Assign current index to checkbox value
    $(this).val(index);
    
}).change(function() {
    // Retrieve checkbox index
    var index = parseInt($(this).val());

    // Retrieve all <g> groups from the graph
    var groups = $('#plot-container').find('g.mpld3-paths > g');

    // Check if the checkbox is checked
    var isChecked = $(this).is(':checked');

    // Browse all groups
    groups.each(function(gIndex, element) {

        if(gIndex === index) {
            
            var paths = $(element).find('path.mpld3-path');
            
            paths.each(function() {

                var style = $(this).attr('style');
                var colorRegex = /stroke:#([0-9A-Fa-f]{6})/;

                var match = style.match(colorRegex);
                var correctMatch = "#" + match[1];

                if (!isChecked) {
                    // Comment the corresponding part in the path style
                    style = style.replace(colorRegex, '/* stroke:' + correctMatch + ' */');
                    
                    // Apply modified style to path
                    $(this).attr('style', style);
                } else {
                    // Remove the comment from the corresponding part in the path style
                    style = style.replace('/* stroke:' + correctMatch + ' */', 'stroke:' + correctMatch);
                    
                    // Apply modified style to path
                    $(this).attr('style', style);
                }
            })
        }
    });
});

// Function to manage checkbox changes
$('.sigma-errors-checkbox').change(function() {
    // Retrieve the selected sigma value
    var sigma = $(this).val();

    // Check if the checkbox is checked
    var isChecked = $(this).is(':checked');

    // Retrieve all <g> groups from the graph
    var groups = $('#plot-container').find('g.mpld3-paths');

    // Récupérer tous les chemins
    var pathsInGroup = $('#plot-container').find('g.mpld3-paths > g path.mpld3-path').length;

    // Initialize total paths count
    var totalPaths = 0;

    // Browse all groups
    groups.each(function() {
        // Retrieve paths within this group
        var paths = $(this).find('path.mpld3-path');

        // List the path indexes in this group
        paths.each(function(index) {
            // Increment total paths count
            totalPaths++;

            if(totalPaths > paths.length - pathsInGroup - 21) {
                console.log('return');
                return;
            }

            // Calculate the index of the path relative to the current sigma value
            var sigmaIndex = Math.floor((index % 10) / 2) + 1;

            if(sigmaIndex == sigma) {

                var style = $(this).attr('style');
                var colorRegex = /stroke:\s*rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)/;

                var match = style.match(colorRegex);
                var red = match[1];
                var green = match[2];
                var blue = match[3];

                if (!isChecked) {
                    
                    // Comment the corresponding part in the path style
                    style = style.replace(colorRegex, '/* stroke:rgb(' + red + ', ' + green + ', ' + blue +  ') */');

                    // Apply modified style to path
                    $(this).attr('style', style);
                } else {
                    // Remove the comment from the corresponding part in the path style
                    style = style.replace('/* stroke:rgb(' + red + ', ' + green + ', ' + blue +  ') */', 'stroke:rgb(' + red + ', ' + green + ', ' + blue + ')');

                    // Apply modified style to path
                    $(this).attr('style', style);
                }
            }

        });
    });
});

/**
 * Returns a function to handle the change event of checkboxes.
 * Modifies the stroke color of paths in SVG groups based on checkbox values.
 *
 * @param {string} selector - The selector for the checkboxes to be handled.
 * @returns {Function} A function to handle the change event of checkboxes.
 */
function handleCheckboxChange(selector) {
    return function() {
        // Retrieve RGB color from the checkbox value
        var rgbValue = 'rgb' + $(this).val();

        // Check if the checkbox is checked
        var isChecked = $(this).is(':checked');

        // Retrieve all <g> groups from the graph
        var groups = $('#plot-container').find('g.mpld3-paths');

        // Browse all groups
        groups.each(function() {
            // Retrieve paths within this group
            var paths = $(this).find('path.mpld3-path');

            // List the path indexes in this group
            paths.each(function() {
                var style = $(this).attr('style');
                var colorRegex = /stroke:\s*rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)/;

                var match = style.match(colorRegex);
                var red = match[1];
                var green = match[2];
                var blue = match[3];

                // Compare RGB values with checkbox RGB value
                if (rgbValue === 'rgb(' + red + ', ' + green + ', ' + blue + ')') {
                    if (!isChecked) {
                        // Comment the corresponding part in the path style
                        style = style.replace(colorRegex, '/* stroke:rgb(' + red + ', ' + green + ', ' + blue +  ') */');
                    } else {
                        // Remove the comment from the corresponding part in the path style
                        style = style.replace('/* stroke:rgb(' + red + ', ' + green + ', ' + blue +  ') */', 'stroke:rgb(' + red + ', ' + green + ', ' + blue + ')');
                    }
                    // Apply modified style to path
                    $(this).attr('style', style);
                }
            });
        });
    };
}

// Event manager for file error checkboxes
$('.file-error-checkbox').change(handleCheckboxChange('.file-error-checkbox'));

// Event manager for subfolder checkboxes
$('.subfolder-checkbox').change(handleCheckboxChange('.subfolder-checkbox'));