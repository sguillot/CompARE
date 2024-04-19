def extract_contour_number(contour_plot_html):
    # Search for the start index of the "collections" section in the HTML string
    start_index = contour_plot_html.find('"edgecolors": [') + len('"edgecolors": [')

    # Search for the end index of the "collections" section in the HTML string
    end_index = contour_plot_html.find("]", start_index)

    # Extract the substring containing information on contour collections
    collections_str = contour_plot_html[start_index:end_index]

    return collections_str