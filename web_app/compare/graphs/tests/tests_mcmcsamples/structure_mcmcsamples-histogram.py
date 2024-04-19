import numpy as np
import matplotlib.pyplot as plt

# Charger les données MCMCSamples
data = np.loadtxt('p:\pCloud Backup\ACER-GAMER\Drive F\Collège-Lycée-Université\Troisième Année\S6\Stage - IRAP\CompARE\web_app\compare\static\data\qLMXB_M30_qLMXB_2020_massradius_helium_1_MCMCSamples.txt')

# Extraire les données de masse et de rayon
masse = data[:, 0]
rayon = data[:, 1]

# Définir le nombre de bins pour l'histogramme 2D
bin_size = [0.1, 0.05]

num_bins_masse = int((max(masse) - min(masse)) / bin_size[0])
num_bins_rayon = int((max(rayon) - min(rayon)) / bin_size[1])

# Générer l'histogramme 2D
hist, x_edges, y_edges = np.histogram2d(masse, rayon, bins=[num_bins_masse, num_bins_rayon])

# Normaliser l'histogramme pour obtenir les probabilités
total_points = np.sum(hist)
probabilities = hist / total_points

# Afficher l'histogramme 2D
plt.figure(figsize=(8, 6))
plt.imshow(probabilities.T, extent=(x_edges[0], x_edges[-1], y_edges[0], y_edges[-1]), origin='lower', cmap='viridis', aspect='auto')
plt.colorbar(label='Probabilités')
plt.xlabel('Masse (Msun)')
plt.ylabel('Rayon (km)')
plt.title('Tableau de probabilités 2D des échantillons MCMC')
plt.show()
