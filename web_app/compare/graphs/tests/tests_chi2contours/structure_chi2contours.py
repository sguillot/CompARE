import os
import matplotlib.pyplot as plt

def lire_fichier_texte(nom_fichier):
    """Fonction pour lire les données à partir d'un fichier texte."""
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    return lignes

def extraire_donnees(lignes):
    """Fonction pour extraire les données à partir des lignes."""
    x_rayons = [[] for _ in range(5)]  # Pour permettre jusqu'à 5 ensembles de données de rayons
    y_masses = [[] for _ in range(5)]  # Pour permettre jusqu'à 5 ensembles de données de masses
    nb_entrees = None
    for ligne in lignes:
        if ligne.startswith('#'):
            continue
        valeurs = ligne.strip().split()
        if nb_entrees is None:
            nb_entrees = len(valeurs) // 2
        else:
            if len(valeurs) // 2 != nb_entrees:
                raise ValueError("Le nombre de valeurs ne correspond pas au nombre attendu.")
        for i, valeur in enumerate(valeurs):
            if i % 2 == 0:  # Les indices pairs correspondent aux valeurs de rayons
                x_rayons[i // 2].append(float(valeur))
            else:  # Les indices impairs correspondent aux valeurs de masses
                y_masses[i // 2].append(float(valeur))
    return x_rayons, y_masses

def tracer_contours(x_rayons, y_masses):
    """Fonction pour tracer les contours."""
    plt.figure()
    plt.xlabel('Rayons')
    plt.ylabel('Masses')
    plt.title('Contours')
    # Tracer les contours en reliant les points de rayons et de masses
    for x, y in zip(x_rayons, y_masses):
        plt.plot(x, y)
    plt.grid(True)
    plt.show()


lines = lire_fichier_texte('contour_coords.txt')
x_rayons, y_masses = extraire_donnees(lines)
tracer_contours(x_rayons, y_masses)
