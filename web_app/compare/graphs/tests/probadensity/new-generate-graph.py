import h5py
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

def plot_contours_from_h5(h5_files):

    # Liste des couleurs pour les contours
    colors = ['black', 'blue', 'green', 'yellow', 'red']

    # Créer une nouvelle figure matplotlib
    fig, ax = plt.subplots()

    # Ajouter les traces de contour pour chaque fichier
    for h5_file in h5_files:

        # Ouvrir le fichier HDF5 en mode lecture
        with h5py.File(h5_file, "r") as hf:
            # Extraire les données du fichier HDF5
            mass = hf["data"]["Mass (M☉)"][:]

            radius = hf["data"]["Radius (km)"][:]
            density = hf["data"]["Proba density"][:]
            contours = hf["data"]["Contours"][:]

            print(contours)

            # Créer le contour plot
            levels = sorted(contours)
            ax.contour(radius, mass, density, levels=levels, colors=colors)

    # Ajouter le plugin pour afficher les coordonnées au survol du graphe
    plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))

    # Afficher la figure matplotlib avec mpld3 pour l'interactivité
    mpld3.fig_to_html(fig)
    mpld3.show()

# Chemins vers les fichiers HDF5
h5_files = ["web_app/compare/static/h5/qLMXB_M13_qLMXB_2018_massradius_helium_1_ProbaDistrib.h5",
            "web_app/compare/static/h5/qLMXB_M13_qLMXB_2018_massradius_hydrogen_1_ProbaDistrib.h5"]

# Tracer les contours à partir des fichiers HDF5
plot_contours_from_h5(h5_files)
