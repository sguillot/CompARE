import h5py
import matplotlib.pyplot as plt

# Lecture du fichier HDF5
with h5py.File('web_app/compare/static/h5/NS_Mass_PSRJ1614-2230_NANOgrav11yr_mass_shapiro_1_MeanErrors.h5', 'r') as hf:
    # Afficher les clés de chaque groupe et dataset dans le fichier HDF5
    print("Keys in the HDF5 file:")
    for key in hf.keys():
        print(key)
        if isinstance(hf[key], h5py.Group):
            for subkey in hf[key].keys():
                print(f"    {subkey}")

    # Parcourir tous les groupes 
    for group_name, group in hf.items():
        print(f"Group: {group_name}")
        # Parcourir  les ensembles de données dans le groupe (chaque ensemble de données représente les coordonnées d'un contour)
        for subgroup_name, dataset in group.items():
            print(f"Subgroup {subgroup_name}:")
            # Afficher les coordonnées du contour
            print(dataset[:])  # Utilisez [:] pour accéder aux valeurs du dataset