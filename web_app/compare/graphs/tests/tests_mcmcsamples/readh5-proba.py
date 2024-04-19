import h5py

# Ouvrir le fichier HDF5 en mode lecture
with h5py.File("bins_and_probabilities.h5", "r") as file:
    # Afficher les clés de chaque groupe et dataset dans le fichier HDF5
    print("Keys in the HDF5 file:")
    for key in file.keys():
        print(key)
        if isinstance(file[key], h5py.Group):
            for subkey in file[key].keys():
                print(f"    {subkey}")

    # Lire les données du dataset "Radium (km)"
    x_edges_dataset = file["data"]["Radium (km)"]
    x_edges_data = x_edges_dataset[()]

    print("Contenu du dataset 'Radium (km)':")
    print(x_edges_data)

    # Lire les données du dataset "Mass (M☉)"
    y_edges_dataset = file["data"]["Mass (M☉)"]
    y_edges_data = y_edges_dataset[()]

    print("Contenu du dataset 'Mass (M☉)':")
    print(y_edges_data)

    # Lire les données du dataset "Proba density"
    probabilities_dataset = file["data"]["Proba density"]
    probabilities_data = probabilities_dataset[()]

    print("Contenu du dataset 'Proba density':")
    print(probabilities_data)

