import numpy as np
import matplotlib.pyplot as plt

# Charger les données à partir du fichier
data = np.loadtxt("web_app/compare/static/data/qLMXB_M13_qLMXB_2018_massradius_helium_1_ProbaDistrib.txt", comments='#')

# Extraire les valeurs de rayon, de masse et de probabilité de densité
R = data[:, 0]
M = data[:, 1]
density = data[:, 2]

# Reshape des données pour les tracer en 2D
num_unique_R = len(np.unique(R))
num_unique_M = len(np.unique(M))
R_grid = R.reshape(num_unique_R, num_unique_M)
M_grid = M.reshape(num_unique_R, num_unique_M)
density_grid = density.reshape(num_unique_R, num_unique_M)

# Plot
plt.figure(figsize=(8, 6))
contour = plt.contourf(R_grid, M_grid, density_grid, cmap='viridis')
plt.colorbar(label='Probabilité de densité')
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Grille 2D de probabilité de densité')

# Contours de niveaux de confiance à 68%, 95% et 99%
confidence_levels = [0.001, 0.05, 0.32]
for level in confidence_levels:
    plt.contour(R_grid, M_grid, density_grid, levels=[np.max(density_grid)*level], colors='white', linestyles='dashed')

plt.show()
