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

// Event manager for checkboxes
$('.subfolder-checkbox').change(function() {
    // Retrieve checkbox index
    var index = $(this).index();

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
            if(match) {

                var red = match[1];
                var green = match[2];
                var blue = match[3];

                // Compare RGB values with checkbox RGB value
                if (rgbValue === 'rgb(' + red + ', ' + green + ', ' + blue + ')') {
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
            }
        });
    });
});