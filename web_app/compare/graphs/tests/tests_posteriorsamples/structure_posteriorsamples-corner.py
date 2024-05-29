import numpy as np
import matplotlib.pyplot as plt
import corner

# Charger les données MCMCSamples
data = np.loadtxt('web_app/compare/static/data/PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1_PosteriorSamples.txt')

masse = data[:, 0]
rayon = data[:, 1]
data_subset = np.vstack((rayon, masse)).T

# Définir le nombre de bins pour chaque axe
bin_size_masse = 0.03
bin_size_rayon = 0.05

num_bins_masse = int((max(masse) - min(masse)) / bin_size_masse)
num_bins_rayon = int((max(rayon) - min(rayon)) / bin_size_rayon)

# Utiliser un dictionnaire pour passer des bins spécifiques pour chaque axe
bins = [num_bins_masse, num_bins_rayon]

# Générer le nuage de points avec corner.py et spécifier les niveaux de confiance
figure = corner.corner(data_subset, bins=bins, quantiles=(0.16, 0.84), levels=(0.68, 0.95, 0.9999), contour_kwargs={"colors":['red', 'green', 'blue']})
print(figure)

print(figure.get_axes())

contour_coords_list = []

# Parcourir les axes du graphique
for ax in figure.get_axes():
    contours = ax.collections
    for contour in contours:
        # Obtenir les coordonnées du contour
        contour_coords = contour.get_paths()[0].vertices
        # Ajouter les coordonnées à la liste
        print(contour_coords)

# Afficher le nuage de points
plt.show()
