import os
import numpy as np
import matplotlib.pyplot as plt

# Définir les sous-dossiers contenant les fichiers de données
subfolders = ['Hybrid', 'Hyperon', 'Nucleon', 'Quark']
data_folder = 'web_app/compare/static/eos_radius_mass'

# Créer une figure pour afficher les courbes
plt.figure(figsize=(10, 6))

# Parcourir les sous-dossiers
for i, subfolder in enumerate(subfolders):
    # Construire le chemin d'accès au sous-dossier
    folder_path = os.path.join(data_folder, subfolder)
    
    # Parcourir les fichiers .dat dans le sous-dossier
    for filename in os.listdir(folder_path):
        if filename.endswith('.dat'):
            file_path = os.path.join(folder_path, filename)
            
            # Charger les données depuis le fichier .dat en ignorant les lignes commençant par "#"
            data = np.loadtxt(file_path, comments='#')
            
            # Extraire les colonnes de données (rayon et masse)
            radius = data[:, 0]
            mass = data[:, 1]
            
            # Tracer la courbe
            plt.plot(radius, mass, label=f'{subfolder} - {filename[:-4]}', color='C{}'.format(i))

# Ajouter des étiquettes et une légende
plt.xlabel('Rayon')
plt.ylabel('Masse')
plt.title('Courbes EOS (Equation Of State)')
plt.legend()

# Afficher le graphique
plt.grid(True)
plt.show()
