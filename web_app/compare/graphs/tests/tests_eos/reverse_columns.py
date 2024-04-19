import numpy as np

data = np.loadtxt('web_app/compare/static/eos_radius_mass/Quark/Q138.dat')

# Inverser les colonnes
colonne1 = 0  # Indice de la première colonne à échanger
colonne2 = 1  # Indice de la deuxième colonne à échanger
data[:, [colonne1, colonne2]] = data[:, [colonne2, colonne1]]

# Sauvegarder le fichier inversé si nécessaire
np.savetxt('fichier_inverse.dat', data, delimiter='\t')  # ajustez le format et le délimiteur selon vos besoins