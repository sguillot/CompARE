import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

# Charger les données à partir du fichier
data = np.loadtxt("web_app/compare/static/data/qLMXB_M13_qLMXB_2018_massradius_hydrogen_1_ProbaDistrib.txt", comments='#')

# Extraire les valeurs de rayon, de masse et de probabilité de densité
R = data[:, 0]
M = data[:, 1]
density = data[:, 2]

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

# Initialiser une liste pour stocker les coordonnées des contours
contour_coordinates = []

# Calculer les contours de confiance
for i, level in enumerate(confidence_levels):
    sol = optimize.root_scalar(lambda x, pdf, max_pdf, xcl: pdf[pdf > x * max_pdf].sum() - xcl * pdf.sum(),
                               args=(density, max_pdf, level), x0=0.01, x1=1.0, rtol=0.01, maxiter=100)
    xlev = sol.root

    contour = plt.contour(radius_grid, mass_grid, density_grid_mass_radius, levels=[xlev * max_pdf], colors=colors[i], linestyles='dashed')
    
    # Accéder aux chemins des contours
    paths = contour.collections[0].get_paths()
    # Pour chaque chemin, accéder aux coordonnées des points et les ajouter à la liste
    for j, path in enumerate(paths):
        coordinates = path.vertices
        print(f"Writing coordinates of contour {j + 1} to file...")
        filename = f"contour_{i + 1}_{j + 1}.txt"  # Nom du fichier de sortie
        np.savetxt(filename, coordinates, header=f"Coordinates of contour {j + 1} for confidence level {level}")

# Réutiliser contour_coordinates, stocker dans un txt et voir si ce sont les mêmes contours que ceux de la figure

# Plot
plt.figure(figsize=(8, 6))
plt.imshow(density_grid_mass_radius, extent=[radius_grid.min(), radius_grid.max(), mass_grid.min(), mass_grid.max()], cmap='viridis', origin='lower', aspect='auto')
plt.colorbar(label='Probabilité de densité')
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Grille 2D de probabilité de densité pour la masse et le rayon')

plt.show()