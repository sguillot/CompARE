import os
import h5py

def lire_fichier_texte(nom_fichier):
    """Fonction pour lire les données à partir d'un fichier texte."""
    with open(nom_fichier, 'r') as f:
        lignes = f.readlines()
    return lignes

def extraire_donnees(lignes):
    """Fonction pour extraire les données à partir des lignes."""
    donnees = {}
    titre_groupes = []
    for ligne in lignes:
        if ligne.startswith('#'):
            # Si c'est une ligne de titre, extraire les noms de groupe
            noms_groupes = ligne.strip().split()[1:]
            # Fusionner les noms de groupe
            for i in range(0, len(noms_groupes), 2):
                titre_groupes.append(f"{noms_groupes[i]} {noms_groupes[i+1]}")
                print(titre_groupes)
                donnees[titre_groupes[-1]] = []
            continue
        valeurs = ligne.strip().split()
        if len(valeurs) % 2 != 0:
            raise ValueError("Le nombre de valeurs doit être pair (rayons et masses).")
        nb_entrees = len(valeurs) // 2
        for i in range(nb_entrees):
            donnees[titre_groupes[i]].append([float(valeurs[2*i]), float(valeurs[2*i+1])])
    return titre_groupes, donnees

def enregistrer_donnees_h5(nom_fichier, titre_groupes, donnees):
    """Fonction pour enregistrer les données dans un fichier HDF5."""
    h5_dir = "web_app/compare/static/h5/"
    if not os.path.exists(h5_dir):
        os.makedirs(h5_dir)

    with h5py.File(os.path.join(h5_dir, nom_fichier), 'w') as hf:
        for nom_groupe in titre_groupes:
            nouveau_nom_groupe = nom_groupe.split(" M_")[1]
            groupe = hf.create_group(f"{nouveau_nom_groupe}")
            groupe.create_dataset(nom_groupe, data=donnees[nom_groupe])

def chi2contours_to_h5(directory):
    """
    Cette fonction parcourt tous les fichiers MCMCSamples dans un répertoire donné et crée des fichiers HDF5 pour chaque ensemble de données.

    Args:
        directory (str): Le chemin du répertoire contenant les fichiers MCMCSamples.
    """
    for filename in os.listdir(directory):
        if filename.endswith("Contours.txt"):
            file_path = os.path.join(directory, filename)
            print(f"Creating HDF5 file for {file_path}")
            lines = lire_fichier_texte(file_path)
            titre_groupes, donnees = extraire_donnees(lines)
            nom_fichier_h5 = f"{os.path.splitext(filename)[0]}.h5"
            enregistrer_donnees_h5(nom_fichier_h5, titre_groupes, donnees)

chi2contours_to_h5('web_app/compare/static/data/')

#def tracer_contours(x_rayons, y_masses):
#    """Fonction pour tracer les contours."""
#    plt.figure()
#    plt.xlabel('Rayons')
#    plt.ylabel('Masses')
#    plt.title('Contours')
#    # Tracer les contours en reliant les points de rayons et de masses
#    for x, y in zip(x_rayons, y_masses):
#        plt.plot(x, y)
#    plt.grid(True)
#    plt.show()