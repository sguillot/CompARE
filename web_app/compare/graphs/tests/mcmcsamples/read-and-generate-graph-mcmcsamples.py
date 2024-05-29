import h5py
import numpy as np
import plotly.graph_objs as go

def generate_contour_plot_from_mcmcsamples(file_path):
    x_values = []
    y_values = []

    # Extraire les données du fichier H5
    with h5py.File(file_path, 'r') as hf:
        # Parcourir tous les groupes 
        for group_name, group in hf.items():
            # Parcourir les ensembles de données dans le groupe
            for subgroup_name, dataset in group.items():
                # Vérifier les noms de sous-groupes pour extraire les données de masse et de rayon
                if(subgroup_name.startswith('R_')):
                    x_values.append(dataset[:, 0])
                    y_values.append(dataset[:, 1])
                    
    # Trouver les valeurs maximales de x et y
    max_x = np.max([np.max(x) for x in x_values])
    max_y = np.max([np.max(y) for y in y_values])

    # Trouver les valeurs minimales de x et y
    min_x = np.min([np.min(x) for x in x_values])
    min_y = np.min([np.min(y) for y in y_values])

    # Créer la figure du graphe de contours
    fig = go.Figure()

    # Ajouter les contours
    for i in range(len(x_values)):
        # Ajouter le contour avec les données x et y
        fig.add_trace(go.Scatter(
            x=x_values[i],  # Coordonnées de rayons
            y=y_values[i],  # Coordonnées de masses
            mode='lines',
            line=dict(width=2),  # Largeur de la ligne du contour
        ))

    # Définir les limites des axes x et y en fonction des valeurs maximales
    fig.update_xaxes(range=[min_x, max_x])
    fig.update_yaxes(range=[min_y, max_y])

    # Ajouter les titres et les étiquettes des axes
    fig.update_layout(
        title='MCMC Samples Plot',
        xaxis_title='Radius (km)',
        yaxis_title='Mass (M☉)',
    )

    # Afficher le graphe
    fig.show()

# Utilisation de la fonction pour extraire les données et générer le graphe de contours à partir du fichier H5
generate_contour_plot_from_mcmcsamples('web_app/compare/static/h5/qLMXB_M30_qLMXB_2020_massradius_hydrogen_1_MCMCSamples.h5')
