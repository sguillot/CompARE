import numpy as np
import matplotlib.pyplot as plt

# Charger les coordonnées à partir du fichier texte
filename = "contour_1_1.txt"  # Mettez le nom de votre fichier ici
coordinates = np.loadtxt(filename)

# Extraire les coordonnées x et y
x = coordinates[:, 0]
y = coordinates[:, 1]

# Tracer le contour
plt.figure()
plt.plot(x, y, linestyle='-', color='blue')  # Vous pouvez personnaliser le style et la couleur du tracé
plt.xlabel('Rayon (km)')
plt.ylabel('Masse (Msun)')
plt.title('Contour de niveau de confiance')
plt.grid(True)
plt.show()
