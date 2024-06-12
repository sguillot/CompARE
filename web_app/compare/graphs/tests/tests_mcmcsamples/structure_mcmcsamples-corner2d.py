import numpy as np
import matplotlib.pyplot as plt
import corner

# Charger les données MCMCSamples
data = np.loadtxt('web_app/compare/static/data/qLMXB_M30_qLMXB_2020_massradius_helium_1_MCMCSamples.txt')

# Extraire les données de masse et de rayon
masse = data[:, 0]
rayon = data[:, 1]

# Définir le nombre de bins pour l'histogramme 2D
bin_size = [0.3, 0.2]

num_bins_masse = int((max(masse) - min(masse)) / bin_size[0])
num_bins_rayon = int((max(rayon) - min(rayon)) / bin_size[1])

contour_colors = ['red', 'green', 'blue']

# Histogramme 2D paramétré via numpy : les valeurs de x_edges et y_edges sont les valeurs minimales et maximales des bins
hist, x_edges, y_edges = np.histogram2d(masse, rayon, bins=[num_bins_masse, num_bins_rayon])

# /!\ Proba density => juste à faire le rapport entre les probabilités trouvées et la masse et le rayon
total_points = np.sum(hist)
probabilities = hist / total_points

# Créer l'histogramme 2D avec Corner
figure = corner.hist2d(masse, rayon, contour_kwargs={'colors': contour_colors}, levels=[0.68, 0.95, 0.9999], bins=[num_bins_masse, num_bins_rayon])

# Ajouter des labels aux axes
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Histogramme 2D des échantillons MCMC avec contours de densité')

# Afficher le plot
plt.show()
