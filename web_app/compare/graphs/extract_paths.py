def extract_contour_number(contour_plot_html):
    # Search for the start index of the "collections" section in the HTML string
    start_index = contour_plot_html.find('"edgecolors": [')
    if start_index == -1:
        # Si "edgecolors" n'est pas trouvé, rechercher la présence de "color"
        start_index = contour_plot_html.find('"color": "')
        if start_index != -1:
            # Si "color" est trouvé, récupérer le code hexadécimal suivant
            end_index = contour_plot_html.find('"', start_index + len('"color": "') + 1)
            color_code = contour_plot_html[start_index + len('"color": "'):end_index]
            return color_code
    else:
        start_index += len('"edgecolors": [')

        # Recherche de l'indice de fin de la section "collections" dans la chaîne HTML
        end_index = contour_plot_html.find("]", start_index)

        # Extraction de la sous-chaîne contenant les informations sur les collections de contours
        collections_str = contour_plot_html[start_index:end_index]

        return collections_str