import numpy as np
import matplotlib.pyplot as plt

# Charger les données à partir du fichier
data = np.loadtxt("web_app/compare/static/data/qLMXB_M13_qLMXB_2018_massradius_helium_1_ProbaDistrib.txt", comments='#')

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

print(np.sum(density_grid_mass_radius))
print(68*np.sum(density_grid_mass_radius)/100)
print(95*np.sum(density_grid_mass_radius)/100)
print(99.99*np.sum(density_grid_mass_radius)/100)

# Calcul des seuils de probabilité correspondant aux niveaux de confiance (68%, 95% et 99.99%)
confidence_levels = [0.68, 0.95, 0.9999]
confidence_thresholds = []
for level in confidence_levels:
    threshold = np.percentile(density_grid_mass_radius.flatten(), (1-level)*100)
    print(threshold)
    confidence_thresholds.append(threshold)

# Calcul des contours de confiance
contour_levels = []
for threshold in confidence_thresholds:
    contour = plt.contour(radius_grid, mass_grid, density_grid_mass_radius, levels=[threshold], colors='red')
    contour_levels.append(contour.collections[0].get_paths()[0])

# Plot
plt.figure(figsize=(8, 6))
plt.imshow(density_grid_mass_radius, extent=[radius_grid.min(), radius_grid.max(), mass_grid.min(), mass_grid.max()], cmap='viridis', origin='lower', aspect='auto')
plt.colorbar(label='Probabilité de densité')
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Grille 2D de probabilité de densité pour la masse et le rayon')

plt.show()
