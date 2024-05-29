import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Charger les données depuis le fichier texte en sautant la première ligne et en spécifiant l'espace comme délimiteur
data = np.loadtxt("p:\pCloud Backup\ACER-GAMER\Drive F\Collège-Lycée-Université\Troisième Année\S6\Stage - IRAP\CompARE\web_app\compare\static\data\qLMXB_M30_qLMXB_2020_massradius_helium_1_MCMCSamples.txt", skiprows=1)

# Estimer la densité avec la méthode de noyau gaussien
kde = gaussian_kde(data.T)

# Créer une grille pour le tracé
x_min, x_max = data[:, 0].min(), data[:, 0].max()
y_min, y_max = data[:, 1].min(), data[:, 1].max()
xx, yy = np.mgrid[x_min:x_max:200j, y_min:y_max:200j]
positions = np.vstack([xx.ravel(), yy.ravel()])

# Évaluer la densité sur la grille
density = kde(positions).reshape(xx.shape)

# Tracer l'histogramme 2D avec les densités de couleur
plt.imshow(np.rot90(density), extent=[x_min, x_max, y_min, y_max], cmap='Blues')
plt.colorbar(label='Density')

# Ajouter les contours de densité à des niveaux de probabilité spécifiques
levels = [0.0001, 0.05, 0.32]
contour = plt.contour(xx, yy, density, levels=levels, colors=['cyan', 'orange', 'green'])

# Ajouter une légende pour les contours de densité
plt.legend([f'{level*100:.2f}%' for level in levels], loc='lower right')

plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('2D Histogram with Density Contours (Using Gaussian KDE)')
plt.show()