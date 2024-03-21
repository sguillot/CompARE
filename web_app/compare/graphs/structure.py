import matplotlib.pyplot as plt

# Chemin vers le fichier texte
fichier = "web_app/compare/static/data/qLMXB"

# Listes pour stocker les données du fichier
x = []
y = []

# Lecture du fichier
with open(fichier, 'r') as file:
    for line in file:
        # Séparation des valeurs par une virgule (ou autre délimiteur)
        valeurs = line.strip().split(',')
        
        # Ajout des valeurs aux listes
        x.append(float(valeurs[0]))
        y.append(float(valeurs[1]))

# Création du graphique
plt.plot(x, y)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Graphique à partir d\'un fichier texte')
plt.grid(True)
plt.show()