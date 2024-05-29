import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from getdist import MCSamples, plots

# Charger les données à partir du fichier texte
data = np.loadtxt('web_app/compare/static/data/PPM_PSRJ0030+0451_2019_massradius_STPDT_Riley_1_PosteriorSamples.txt', skiprows=1)  # skiprows=1 pour sauter la première ligne contenant les en-têtes

# Extraire les valeurs de masse et de rayon
masses = data[:, 0]
rayons = data[:, 1]

# Concaténer les valeurs de masse et de rayon pour former les échantillons
samples = np.column_stack((rayons, masses))

# Estimation de la densité de probabilité à l'aide de KernelDensity
kde = gaussian_kde(samples.T)

# Évaluation de la densité de probabilité aux points où elle atteint son maximum
max_density = kde.evaluate(kde.dataset)

# Trouver l'indice du maximum de densité
max_index = np.argmax(max_density)

# Valeurs de masse et de rayon correspondant au maximum de densité
masse_max_density = masses[max_index]
rayon_max_density = rayons[max_index]

print("Valeur maximale de densité : ", max_density[max_index])
print("Masse correspondant à la valeur maximale de densité : ", masse_max_density)
print("Rayon correspondant à la valeur maximale de densité : ", rayon_max_density)

# Création de l'objet MCSamples à partir des échantillons
mcsamples = MCSamples(samples=samples, names=['Rayons', 'Masses'])

# Tracé des contours de densité
g = plots.get_subplot_plotter()
g.triangle_plot(mcsamples)  # Tracé des contours
plt.show()