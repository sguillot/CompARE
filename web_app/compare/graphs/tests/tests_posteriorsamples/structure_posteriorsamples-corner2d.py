import numpy as np
import matplotlib.pyplot as plt
import corner

# Charger les données MCMCSamples
data = np.loadtxt('web_app/compare/static/data/PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1_PosteriorSamples.txt')

# Extraire les données de masse et de rayon
masse = data[:, 0]
rayon = data[:, 1]

# Définir le nombre de bins pour l'histogramme 2D
bin_size = [0.02, 0.02]

num_bins_masse = int((max(masse) - min(masse)) / bin_size[0])
num_bins_rayon = int((max(rayon) - min(rayon)) / bin_size[1])

contour_colors = ['red', 'green', 'blue']

# Histogramme 2D paramétré via numpy : les valeurs de x_edges et y_edges sont les valeurs minimales et maximales des bins
hist, x_edges, y_edges = np.histogram2d(rayon, masse, bins=[num_bins_masse, num_bins_rayon])

# /!\ Proba density => juste à faire le rapport entre les probabilités trouvées et la masse et le rayon
total_points = np.sum(hist)
print(total_points)
probabilities = hist / total_points
print(probabilities)

# Créer l'histogramme 2D avec Corner
figure = corner.hist2d(rayon, masse, contour_kwargs={'colors': contour_colors}, levels=[0.68, 0.95, 0.9999], bins=[num_bins_masse, num_bins_rayon])

# Ajouter des labels aux axes
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Histogramme 2D des échantillons MCMC avec contours de densité')

# Afficher le plot
plt.show()
