from matplotlib import pyplot as plt
import numpy as np
import h5py
import os

def compute_contours_and_save(x, y, file_path, bins=None, levels=None):
    """
    Cette fonction calcule les contours en fonction de la densité des points.
    
    Args:
        x (array_like): Les valeurs x des données.
        y (array_like): Les valeurs y des données.
        bins (int or array_like): Le nombre de bins ou les limites des bins.
        levels (array_like): Les niveaux de contour à calculer.
        
    Returns:
        contours: Les coordonnées des contours.
    """

    # Créer le répertoire 'h5' s'il n'existe pas
    h5_dir = "web_app/compare/static/h5/"
    if not os.path.exists(h5_dir):
        os.makedirs(h5_dir)

    # Calculer l'histogramme 2D : x_edges et y_edges sont les limites des bins ; hist est l'histogramme contenant le nombre de points dans chaque bin
    hist, x_edges, y_edges = np.histogram2d(x, y, bins=bins)

    # Normaliser l'histogramme pour obtenir les probabilités
    total_points = np.sum(hist)
    probabilities = hist / total_points

    # Calculer les niveaux de contour par défaut si non spécifiés
    if levels is None:
        levels = 1.0 - np.exp(-0.5 * np.arange(0.5, 2.1, 0.5) ** 2)

    # Calculer les contours
        
    # Aplatir l'histogramme et trier les valeurs
    Hflat = hist.flatten()
    # Trie les valeurs de l'histogramme en ordre décroissant
    inds = np.argsort(Hflat)[::-1]
    # Arrange les valeurs de l'histogramme selon les indices triés
    Hflat = Hflat[inds]
    # Calcule la somme cumulée des valeurs de l'histogramme
    sm = np.cumsum(Hflat)
    # Normalise les valeurs de la somme cumulée
    sm /= sm[-1]
    # Tableau vide pour stocker les valeurs des contours calculés
    V = np.empty(len(levels))
    # Pour chaque niveau de contour
    for i, v0 in enumerate(levels):
        try:
            # Trouver la valeur de l'histogramme qui correspond au niveau de contour
            V[i] = Hflat[sm <= v0][-1]
        except IndexError:
            V[i] = Hflat[0]
    # Trie les valeurs de contour
    V.sort()
    m = np.diff(V) == 0
    # Si les valeurs de contour sont égales, les multiplier par 1 - 1e-4
    if np.any(m):
        V[np.where(m)[0][0]] *= 1.0 - 1e-4
    V.sort()

    # Calculer les bin centers
    X1, Y1 = np.meshgrid(x_edges[:-1] + 0.5 * np.diff(x_edges), y_edges[:-1] + 0.5 * np.diff(y_edges))

    # Extend the array for the sake of the contours at the plot edges.
    H2 = np.zeros((hist.shape[0] + 4, hist.shape[1] + 4))
    H2[2:-2, 2:-2] = hist
    H2[2:-2, 1] = hist[:, 0]
    H2[2:-2, -2] = hist[:, -1]
    H2[1, 2:-2] = hist[0]
    H2[-2, 2:-2] = hist[-1]
    H2[1, 1] = hist[0, 0]
    H2[1, -2] = hist[0, -1]
    H2[-2, 1] = hist[-1, 0]
    H2[-2, -2] = hist[-1, -1]

    X2 = np.concatenate(
        [
            X1[0, 0] + np.array([-2, -1]) * (X1[0, 1] - X1[0, 0]),
            X1[0],
            X1[0, -1] + np.array([1, 2]) * (X1[0, -1] - X1[0, -2]),
        ]
    )
    Y2 = np.concatenate(
        [
            Y1[0, 0] + np.array([-2, -1]) * (Y1[1, 0] - Y1[0, 0]),
            Y1[:, 0],
            Y1[-1, 0] + np.array([1, 2]) * (Y1[-1, 0] - Y1[-2, 0]),
        ]
    )

    # Créer un fichier HDF5 pour stocker les coordonnées des contours
    contours = plt.contour(X2, Y2, H2.T, V, colors=['blue', 'green', 'red'])
    contour_coords = {}
    colors_titles = {'00_00_255': '3σ', '00_128_00': '2σ', '255_00_00': '1σ'}

    # Collecting coordinates for each color
    for collection in contours.collections:
        color = collection.get_edgecolor()[0][:3]
        color_str = "_".join([f"{int(x * 255):02d}" for x in color[:3]])
        if color_str not in contour_coords:
            contour_coords[color_str] = []

        for path in collection.get_paths():
            contour_coords[color_str].append(path.vertices)

    with h5py.File(os.path.join(h5_dir, f"{os.path.splitext(os.path.basename(file_path))[0]}.h5"), "w") as hf:
        # Création d'un groupe pour les données
        data_group = hf.create_group("data")
        
        # Stockage des coordonnées des bins
        data_group.create_dataset("Radius (km)", data=x_edges)
        data_group.create_dataset("Mass (M☉)", data=y_edges)
        
        # Stockage des probabilités
        data_group.create_dataset("Proba density", data=probabilities)

        for color, coords_list in contour_coords.items():

            # Creating a group for each color
            main_group_name = colors_titles[color]
            grp = hf.create_group(main_group_name)

            # Storing coordinates for each contour
            for idx, coords in enumerate(coords_list):
                grp.create_dataset(f"R_{main_group_name} M_{main_group_name}", data=coords)

    print(f"Saved HDF5 file: {os.path.join(h5_dir, os.path.splitext(os.path.basename(file_path))[0])}.h5")

    return contour_coords

def process_mcmcsamples(file_path):
    """
    Cette fonction charge les données MCMCSamples à partir d'un fichier texte et définit les paramètres pour les contours de densité de probabilité.

    Args:
        file_path (str): Le chemin du fichier texte contenant les données MCMCSamples.
    """

    # Charger les données MCMCSamples
    data = np.loadtxt(file_path)

    # Extraire les données de masse et de rayon
    masse = data[:, 0]
    rayon = data[:, 1]

    # Définir le nombre de bins pour l'histogramme 2D
    bin_size = [0.1, 0.05]
    num_bins_masse = int((max(masse) - min(masse)) / bin_size[0])
    num_bins_rayon = int((max(rayon) - min(rayon)) / bin_size[1])

    # Calculer les contours et enregistrer les résultats dans un fichier HDF5
    compute_contours_and_save(masse, rayon, file_path, bins=[num_bins_masse, num_bins_rayon], levels=[0.68, 0.95, 0.9999])

def mcmcsamples_to_h5(directory):
    """
    Cette fonction parcourt tous les fichiers MCMCSamples dans un répertoire donné et crée des fichiers HDF5 pour chaque ensemble de données.

    Args:
        directory (str): Le chemin du répertoire contenant les fichiers MCMCSamples.
    """
    for filename in os.listdir(directory):
        if filename.endswith("MCMCSamples.txt"):
            file_path = os.path.join(directory, filename)
            print(f"Creating HDF5 file for {file_path}")
            process_mcmcsamples(file_path)

            plt.show()

mcmcsamples_to_h5('web_app/compare/static/data/')