from all_data_processing import process_data_to_h5

if __name__ == "__main__":
    # Définir le répertoire contenant les fichiers de données
    data_directory = "web_app/compare/static/data/"

    # Data processing and storage in HDF5 files
    process_data_to_h5(data_directory)