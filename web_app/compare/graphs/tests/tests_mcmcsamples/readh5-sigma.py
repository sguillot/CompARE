import h5py

# Ouvrir le fichier HDF5 en mode lecture
with h5py.File("contour_coords.h5", "r") as hf:
    # Parcourir tous les groupes (chaque groupe représente une couleur de contour)
    for color, group in hf.items():
        print(f"Color: {color}")
        # Parcourir tous les ensembles de données dans le groupe (chaque ensemble de données représente les coordonnées d'un contour)
        for contour_id, dataset in group.items():
            print(f"Contour {contour_id}:")
            # Afficher les coordonnées du contour
            print(dataset[:])  # Utilisez [:] pour accéder aux valeurs du dataset
