import numpy as np
import h5py
import os
import matplotlib.pyplot as plt
from scipy import optimize

def compute_contours(R, M, density, output_h5_file):
    """
    Cette fonction calcule les contours de densité de probabilité à partir des données de rayon, de masse et de densité,
    puis les enregistre dans un fichier HDF5.

    Args:
        R (array_like): Les valeurs de rayon.
        M (array_like): Les valeurs de masse.
        density (array_like): Les valeurs de densité de probabilité.
        output_h5_file (str): Le chemin du fichier HDF5 de sortie.
    """

    # Créer une grille de probabilité de densité pour la masse et le rayon
    mass_grid = np.unique(M)
    radius_grid = np.unique(R)
    density_grid_mass_radius = np.zeros((len(mass_grid), len(radius_grid)))

    # Remplir la grille avec les valeurs de densité
    for i in range(len(density)):
        mass_index = np.where(mass_grid == M[i])[0][0]
        radius_index = np.where(radius_grid == R[i])[0][0]
        density_grid_mass_radius[radius_index, mass_index] = density[i]

    # Trouver la valeur maximale de la densité
    max_pdf = np.max(density)

    # Niveaux de confiance
    confidence_levels = [0.68, 0.95, 0.9999]

    # Couleurs
    colors = ['blue', 'green', 'red']

    h5_dir = "web_app/compare/static/h5/"
    if not os.path.exists(h5_dir):
        os.makedirs(h5_dir)

    # Initialiser un fichier HDF5 pour stocker les coordonnées des contours
    with h5py.File(os.path.join(h5_dir, output_h5_file), "w") as f:

        # Créer un groupe pour les données
        data_group = f.create_group("data")
        # Ajouter les ensembles de données pour les valeurs de masse, de rayon et de densité
        data_group.create_dataset("Mass (M☉)", data=mass_grid)
        data_group.create_dataset("Radius (km)", data=radius_grid)
        data_group.create_dataset("Proba density", data=density_grid_mass_radius)

        # Créer un groupe pour les contours de densité de probabilité
        for i, level in enumerate(confidence_levels):

            # Trouver le niveau de densité correspondant au niveau de confiance
            sol = optimize.root_scalar(lambda x, pdf, max_pdf, xcl: pdf[pdf > x * max_pdf].sum() - xcl * pdf.sum(),
                                    args=(density, max_pdf, level), x0=0.01, x1=1.0, rtol=0.01, maxiter=100)
            
            # Récupérer la valeur du niveau de densité
            xlev = sol.root

            # Tracer les contours de densité de probabilité
            contour = plt.contour(radius_grid, mass_grid, density_grid_mass_radius, levels=[xlev * max_pdf], colors=colors[i], linestyles='dashed')
            
            # Accéder aux chemins des contours
            paths = contour.collections[0].get_paths()
            
            # Créer un groupe pour chaque niveau de confiance
            confidence_group = f.create_group(f"{i+1}σ")
            
            # Pour chaque chemin, créer un sous-groupe et enregistrer les coordonnées
            for j, path in enumerate(paths):
                coordinates = path.vertices
                
                # Créer un sous-groupe pour chaque contour
                confidence_group.create_dataset(f"R_{i+1}σ M_{i+1}σ", data=coordinates) 

        plt.show()

def process_probadistrib(file_path):
    """
    Cette fonction charge les données de distribution de probabilité à partir d'un fichier texte et définit les paramètres pour les contours de densité de probabilité.

    Args:
        file_path (str): Le chemin du fichier texte contenant les données de distribution de probabilité.
    """

    # Charger les données de distribution de probabilité
    data = np.loadtxt(file_path)

    # Extraire les données de masse et de rayon
    R = data[:, 0]
    M = data[:, 1]
    density = data[:, 2]

    return R, M, density

def probadistrib_to_h5(directory):
    """
    Cette fonction parcourt tous les fichiers de distribution de probabilité dans un répertoire donné et crée des fichiers HDF5 pour chaque ensemble de données.

    Args:
        directory (str): Le chemin du répertoire contenant les fichiers de distribution de probabilité.
    """
    for filename in os.listdir(directory):
        if filename.endswith("ProbaDistrib.txt"):
            file_path = os.path.join(directory, filename)
            print(f"Creating HDF5 file for {file_path}")
            R, M, density = process_probadistrib(file_path)
            # Enregistrer les données dans un fichier H5
            output_h5_file = f"{os.path.splitext(filename)[0]}.h5"
            compute_contours(R, M, density, output_h5_file)
            print(f"Saved HDF5 file: {output_h5_file}")

probadistrib_to_h5('web_app/compare/static/data/')