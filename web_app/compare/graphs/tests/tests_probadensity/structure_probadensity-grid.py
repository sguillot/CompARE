import numpy as np
import matplotlib.pyplot as plt

# Charger les données à partir du fichier
data = np.loadtxt("web_app/compare/static/data/qLMXB_M13_qLMXB_2018_massradius_helium_1_ProbaDistrib.txt", comments='#')

# Extraire les valeurs de rayon, de masse et de probabilité de densité
R = data[:, 0]
M = data[:, 1]
density = data[:, 2]

# Calculer la taille des bins
R_gap = np.diff(np.unique(R))[0]
M_gap = np.diff(np.unique(M))[0]

# Calculer le nombre de bins
num_R_bins = len(np.unique(R))
num_M_bins = len(np.unique(M))

# Créer une grille de probabilité de densité
density_grid = np.zeros((num_M_bins, num_R_bins))

# Remplir la grille avec les valeurs de densité
for i in range(len(density)):
    R_index = int((R[i] - R.min()) / R_gap)
    M_index = int((M[i] - M.min()) / M_gap)
    if 0 <= R_index < num_R_bins and 0 <= M_index < num_M_bins:
        density_grid[R_index, M_index] = density[i]

# Plot
plt.figure(figsize=(8, 6))
plt.imshow(density_grid, extent=[R.min(), R.max(), M.min(), M.max()], cmap='viridis', origin='lower', aspect='auto')
plt.colorbar(label='Probabilité de densité')
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Grille 2D de probabilité de densité')
plt.show()
