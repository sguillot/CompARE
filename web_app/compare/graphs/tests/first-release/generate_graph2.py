import h5py
import os
import plotly.graph_objects as go
import numpy as np

def plot_contours_from_h5(file_path):

    if file_path.endswith("ProbaDistrib.h5") or file_path.endswith("MCMCSamples.h5"):

        # Ouvrir le fichier HDF5 en mode lecture
        with h5py.File(file_path, "r") as hf:
            # Extraire les données du fichier HDF5
            mass = hf["data"]["Mass (M☉)"][:]
            radius = hf["data"]["Radius (km)"][:]
            density = hf["data"]["Proba density"][:]
            contours = hf["data"]["Contours"][()]

            # Couleurs pour les contours
            colors = ['blue', 'green', 'red']
            colorscale = [[0.68, 'blue'], [0.95, 'green'], [0.9999, 'red']]

            # Créer un traceur de contour avec plotly
            fig = go.Figure()

            # Ajouter les traces de contour pour chaque niveau
            for i, level in enumerate(contours):
                color = colors[i] 
                contour_trace = go.Contour(z=density, 
                                        x=radius, 
                                        y=mass,
                                        showscale=False,
                                        colorscale=colorscale,
                                        contours=dict(start=level, 
                                                    end=level, 
                                                    size=0.05,
                                                    coloring='lines',
                                                    showlabels=True))

                fig.add_trace(contour_trace)
                
                # Récupérer les coordonnées pour placer l'annotation sur le côté droit du graphe
                x_coord = max(radius) - 0.50
                y_coord = max(mass) - 0.05 - i * 0.05
                
                # Ajouter l'annotation avec la valeur du niveau de contour
                fig.add_annotation(
                    x=x_coord, 
                    y=y_coord,  
                    text=f"Level {level}",  
                    showarrow=False, 
                    font=dict(color=color) 
                )
                
                fig.add_trace(contour_trace)
    
    elif file_path.endswith("Contours.h5"):

        x_values = []
        y_values = []

        # Extraire les données du fichier H5
        with h5py.File(file_path, 'r') as hf:
            # Parcourir tous les groupes 
            for group_name, group in hf.items():
                # Parcourir les ensembles de données dans le groupe
                for subgroup_name, dataset in group.items():
                    # Vérifier les noms de sous-groupes pour extraire les données de masse et de rayon
                    if subgroup_name.startswith('R_'):
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
            # Ajouter le contour avec les données x, y
            fig.add_trace(go.Scatter(
                x=x_values[i], # Coordonnées de rayons
                y=y_values[i], # Coordonnées de masses
                line=dict(width=2),  # Largeur de la ligne du contour
            ))

        # Définir les limites des axes x et y en fonction des valeurs maximales
        fig.update_xaxes(range=[min_x, max_x])
        fig.update_yaxes(range=[min_y, max_y])

        # Ajouter les titres et les étiquettes des axes
        fig.update_layout(
            title='Contour Plot',
            xaxis_title='Radius (km)',
            yaxis_title='Mass (M☉)',
        )

    return fig.to_html(full_html=False)