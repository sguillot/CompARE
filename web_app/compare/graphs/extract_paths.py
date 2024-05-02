def extract_contour_number(contour_plot_html):
    # Search for the start index of the "collections" section in the HTML string
    start_index = contour_plot_html.find('"edgecolors": [')
    if start_index == -1:
        # If "edgecolors" is not found, check for the presence of "color".
        start_index = contour_plot_html.find('"color": "')
        if start_index != -1:
            # If "color" is found, retrieve the following hexadecimal code
            end_index = contour_plot_html.find('"', start_index + len('"color": "') + 1)
            color_code = contour_plot_html[start_index + len('"color": "'):end_index]
            return color_code
    else:
        start_index += len('"edgecolors": [')

        # Search for the end index of the "collections" section in the HTML string
        end_index = contour_plot_html.find("]", start_index)

        # Extraction of the substring containing contour collection information
        collections_str = contour_plot_html[start_index:end_index]

        return collections_str