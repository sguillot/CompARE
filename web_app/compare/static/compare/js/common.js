window.onload = function() {

    // Function to apply color to subfolder text
    function applyColorToSubfolders() {
        // Apply RGB color to subfolder text
        $('.label-subfolder').each(function(index) {
            var rgbValue = $(this).find('input').val();
            $(this).css('color', 'rgb' + rgbValue);
        });
    }

    // Function to apply color to file name text
    function applyColorToFileNames() {
        // Retrieve all <g> groups from the graph
        var groups = $('#plot-container').find('g.mpld3-paths > g');

        // Browse all groups
        groups.each(function(gIndex, element) {
            var paths = $(element).find('path.mpld3-path');
            
            paths.each(function() {
                var style = $(this).attr('style');
                var colorRegex = /stroke:#([0-9A-Fa-f]{6})/;
                var match = style.match(colorRegex);
                if (match) {
                    var correctMatch = "#" + match[1];
                    var fileNameIndex = gIndex; // Group index corresponds to file
                    $('.label-filename').eq(fileNameIndex).css('color', correctMatch);
                }
            });
        });
    }

    // Call the function to apply colors when the page is fully loaded
    applyColorToFileNames();
    applyColorToSubfolders();
};