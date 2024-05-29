import h5py
import plotly.graph_objects as go
import numpy as np

def plot_contours_from_h5(h5_file):
    # Ouvrir le fichier HDF5 en mode lecture
    with h5py.File(h5_file, "r") as hf:
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

        # Afficher le traceur
        fig.show()

# Chemin vers le fichier HDF5
h5_file = "web_app/compare/static/h5/qLMXB_M30_qLMXB_2020_massradius_helium_1_MCMCSamples.h5"

# Tracer les contours à partir du fichier HDF5
plot_contours_from_h5(h5_file)
