import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# Charger les données des posterior samples
data = np.loadtxt('web_app/compare/static/data/PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1_PosteriorSamples.txt')
mass = data[:, 0]
radius = data[:, 1]

# Estimation par noyau (KDE) de la densité de probabilité
kde = gaussian_kde([mass, radius])
mass_grid, radius_grid = np.mgrid[min(mass):max(mass):100j, min(radius):max(radius):100j]
positions = np.vstack([mass_grid.ravel(), radius_grid.ravel()])
density = kde(positions).reshape(mass_grid.shape)

# Tracer les contours de confiance
fig, ax = plt.subplots()
ax.imshow(np.rot90(density), cmap=plt.cm.viridis)
contour_levels = [0.68, 0.95, 0.997]
ax.contour(mass_grid, radius_grid, density, levels=contour_levels, colors='white')
plt.xlabel('Masse')
plt.ylabel('Rayon')
plt.title('Contours de Confiance des Posterior Samples')
plt.show()
