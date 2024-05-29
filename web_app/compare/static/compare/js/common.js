window.onload = function() {

    /**
     * Applies color to elements with the specified class name.
     *
     * @param {string} className - The class name of elements to which color will be applied.
     */
    function applyColorToElements(className) {
        $('.' + className).each(function(index) {
            var rgbValue = $(this).find('input').val();
            $(this).css('color', 'rgb' + rgbValue);
        });
    }

    /**
     * Applies color to contour filenames based on the stroke color of corresponding paths.
     * Retrieves all <g> groups from the graph and sets the color of label-filename elements accordingly.
     */
    function applyColorToContourFilenames() {
        // Retrieve all <g> groups from the graph
        var groups = $('#plot-container').find('g.mpld3-paths > g');

        if(groups.length > 0) {
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
    }

    // Call the function to apply colors when the page is fully loaded
    applyColorToContourFilenames();
    applyColorToElements('label-subfolder');
    applyColorToElements('label-filename-errors');
};