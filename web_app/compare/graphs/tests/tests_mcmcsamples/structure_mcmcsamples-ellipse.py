import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
from matplotlib.patches import Ellipse

def plot_with_confidence_ellipses(file_path):
    # Charger les données à partir du fichier texte
    data = np.loadtxt(file_path)

    # Séparer les données de masse et de rayon
    masse = data[:, 0]
    rayon = data[:, 1]

    # Calculer le centre du nuage de points
    centre_masse = np.mean(masse)
    print('Centre masse :', centre_masse)
    centre_rayon = np.mean(rayon)
    print('Centre rayon :', centre_rayon)

    # Calculer la matrice de covariance
    cov_matrix = np.cov(masse, rayon, rowvar=False)
    print('Matrice de covariance :', cov_matrix)

    # Calculer les valeurs propres et vecteurs propres de la matrice de covariance
    values, vectors = np.linalg.eig(cov_matrix)
    print('Valeurs :', values)
    print('Vecteurs :', vectors)

    # Déterminer les angles d'inclinaison des ellipses
    angle = np.degrees(np.arctan2(*vectors[::-1, 0]))
    print('Angle :', angle)

    # Paramètres pour les contours de confiance
    conf_levels = [0.68, 0.95, 0.9999]
    sigmas = np.sqrt(chi2.ppf(conf_levels, df=2))
    print('Sigma :', sigmas)

    # Calculer la masse minimale et maximale ainsi que le rayon minimale et maximale
    masse_min, masse_max = np.min(masse), np.max(masse)
    print('Masse minimale :', masse_min)
    print('Masse maximale :', masse_max)
    rayon_min, rayon_max = np.min(rayon), np.max(rayon)
    print('Rayon minimal :', rayon_min)
    print('Rayon maximal :', rayon_max)

    # Créer le scatter plot
    plt.figure(figsize=(8, 6))
    plt.scatter(masse, rayon, s=5, c='b', alpha=0.5, label='Données')

    # Placer le centre du nuage de points
    #plt.scatter(centre_masse, centre_rayon, c='r', marker='o', s=50, label='Centre du nuage de points')

    # Tracer les ellipses de confiance
    colors = ['g', 'm', 'c']  # Couleurs pour les contours
    for i, sigma in enumerate(sigmas):
        width, height = 2 * sigma * np.sqrt(values)
        print(f'Largeur ellipse {conf_levels[i]*100:.2f}% :', width)
        print(f'Hauteur ellipse {conf_levels[i]*100:.2f}% :', height)
        ellipse = Ellipse(xy=(centre_masse, centre_rayon), width=width, height=height, angle=angle, edgecolor=colors[i], lw=2, fill=False, label=f'{conf_levels[i]*100:.2f}%')
        print('Ellipse :', ellipse)
        # Ne tracer l'ellipse que dans les limites des données
        ellipse.set_clip_box(plt.gca().bbox)
        plt.gca().add_patch(ellipse)

    plt.xlabel('Rayon (km)')
    plt.ylabel('Masse (Msun)')
    plt.title('Nuage de points')
    plt.legend()

    # Définir les limites du graphe en fonction des données
    plt.xlim(masse_min, masse_max)
    plt.ylim(rayon_min, rayon_max)

    # Afficher le plot
    plt.grid(True)
    plt.show()

def plot_confidence_ellipses_for_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith("MCMCSamples.txt"):
            file_path = os.path.join(directory, filename)
            print(f"Plotting confidence ellipses for {file_path}")
            plot_with_confidence_ellipses(file_path)

# Exemple d'utilisation
plot_confidence_ellipses_for_files('web_app/compare/static/data/')
