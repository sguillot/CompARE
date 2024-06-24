import matplotlib.pyplot as plt

# Lecture des données à partir du fichier texte
with open('web_app/compare/static/data/qLMXB_M30_qLMXB_2020_massradius_helium_1_MCMCSamples.txt', 'r') as file:
    # Ignorer l'en-tête
    next(file)
    # Initialiser des listes pour stocker la masse et le rayon
    masses = []
    rayons = []
    # Lire chaque ligne du fichier
    for line in file:
        # Séparer les valeurs de masse et de rayon
        masse, rayon = map(float, line.split())
        # Ajouter les valeurs à la liste
        masses.append(masse)
        rayons.append(rayon)

# Création du nuage de points
plt.figure(figsize=(8, 6))
plt.scatter(masses, rayons)
plt.xlabel('Rayon (en kilomètres)')
plt.ylabel('Masse (en masses solaires)')
plt.show()
