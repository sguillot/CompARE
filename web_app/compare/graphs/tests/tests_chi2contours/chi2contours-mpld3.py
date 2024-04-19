
import h5py
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

def scatter_plot(file_path):
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
    fig, ax = plt.subplots()

    # Ajouter les données de dispersion
    for i in range(len(x_values)):
        ax.plot(x_values[i], y_values[i], label=f'Dataset {i+1}')

    # Ajouter les titres et les étiquettes des axes
    ax.set_title('Scatter Plot')
    ax.set_xlabel('Radius (km)')
    ax.set_ylabel('Mass (M☉)')
    ax.legend()

    # Ajouter le plugin pour afficher les coordonnées au survol du graphe
    plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))

    mpld3.show()

# Chemins vers les fichiers HDF5
filename = "web_app/compare/static/h5/qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1_Contours.h5"

# Tracer les contours à partir des fichiers HDF5
scatter_plot(filename)