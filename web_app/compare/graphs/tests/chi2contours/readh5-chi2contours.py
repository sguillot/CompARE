import h5py

x_rayons = []
y_masses = []

with h5py.File('web_app/compare/static/h5/qLMXB_47TucX5_qLMXB_2016_massradius_hydrogen_1_Contours.h5', 'r') as hf:
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