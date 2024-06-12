import h5py
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.integrate import trapezoid

def process_meanerrors_nsmass(filename):
    """
    Traite les données de masse et d'erreur à partir d'un fichier texte.

    Args:
        filename (str): Le chemin vers le fichier texte.

    Returns:
        numpy.ndarray: Les données lues à partir du fichier.
        numpy.ndarray: Les valeurs de densité de probabilité gaussienne.
        numpy.ndarray: Les valeurs de masse pour le graphique.
        numpy.ndarray: Les valeurs de sigma de 1 à 5.
    """
    
    data = np.loadtxt(filename, skiprows=1)
    mass, error = data
    sigma_values = np.array([[mass - error * i, mass + error * i] for i in range(1, 6)])

    last_sigma_values = sigma_values[-1]
    min_mass = last_sigma_values[0]
    max_mass = last_sigma_values[1]

    mass_scale = np.linspace(max(0, min_mass), max_mass, 1000)
    pdf = norm.pdf(mass_scale, loc=mass, scale=error)

    area = trapezoid(pdf, mass_scale)
    print(area)

    return data, pdf, mass_scale, sigma_values

def process_meanerrors_nsspin(filename):
    """
    Traite les données de fréquence et d'erreur à partir d'un fichier texte.

    Args:
        filename (str): Le chemin vers le fichier texte.

    Returns:
        numpy.ndarray: Les données lues à partir du fichier.
        numpy.ndarray: Les valeurs de densité de probabilité gaussienne.
        numpy.ndarray: Les valeurs de fréquence pour le graphique.
        numpy.ndarray: Les valeurs de sigma de 1 à 5.
    """
    
    data = np.loadtxt(filename, skiprows=1)
    frequency, error = data
    sigma_values = np.array([[frequency - error * i, frequency + error * i] for i in range(1, 6)])

    last_sigma_values = sigma_values[-1]
    min_frequency = last_sigma_values[0]
    max_frequency = last_sigma_values[1]

    frequency_scale = np.linspace(max(0, min_frequency), max_frequency, 1000)
    pdf = norm.pdf(frequency_scale, loc=frequency, scale=error)

    area = trapezoid(pdf, frequency_scale)
    print(area)

    return data, pdf, frequency_scale, sigma_values

def save_meanerrors_nsmass_to_h5(filename, pdf, sigma_values, mass_scale):
    """
    Écrit les données de densité de probabilité gaussienne, de sigma et de masse dans un fichier HDF5.

    Args:
        filename (str): Le nom du fichier HDF5.
        pdf (numpy.ndarray): Les valeurs de densité de probabilité gaussienne.
        sigma_values (numpy.ndarray): Les valeurs de sigma de 1 à 5.
        mass_scale (numpy.ndarray): Les valeurs de masse pour le graphique.

    Returns:
        None
    """
    with h5py.File(filename, 'w') as hf:
        data_group = hf.create_group("data")
        data_group.create_dataset('Proba density', data=pdf)
        data_group.create_dataset('Mass (M☉)', data=sigma_values)
        data_group.create_dataset('Mass scale', data=mass_scale)

def save_meanerrors_nsspin_to_h5(filename, pdf, sigma_values, frequency_scale):
    """
    Écrit les données de densité de probabilité gaussienne, de sigma et de fréquence dans un fichier HDF5.

    Args:
        filename (str): Le nom du fichier HDF5.
        pdf (numpy.ndarray): Les valeurs de densité de probabilité gaussienne.
        sigma_values (numpy.ndarray): Les valeurs de sigma de 1 à 5.
        frequency_scale (numpy.ndarray): Les valeurs de fréquence pour le graphique.

    Returns:
        None
    """
    with h5py.File(filename, 'w') as hf:
        data_group = hf.create_group("data")
        data_group.create_dataset('Proba density', data=pdf)
        data_group.create_dataset('Sigma errors', data=sigma_values)
        data_group.create_dataset('Frequency scale', data=frequency_scale)

def generate_plot_nsmass(pdf, mass_scale, mass, error):
    """
    Génère et affiche un graphique de densité de probabilité gaussienne.

    Args:
        pdf (numpy.ndarray): Les valeurs de densité de probabilité gaussienne.
        mass_scale (numpy.ndarray): Les valeurs de masse pour le graphique.
        mass (float): La valeur de masse.
        error (float): L'erreur associée à la masse.

    Returns:
        None
    """
    plt.figure(figsize=(8, 6))
    plt.plot(mass_scale, pdf, label=f'Mass: {mass}, Error: {error:.3f}')
    plt.fill_between(mass_scale, pdf, color='skyblue', alpha=0.3)
    plt.xlabel('Mass (Msun)')
    plt.ylabel('Probability Density')
    plt.title('Gaussian Probability Density')
    plt.legend()
    plt.grid(True)
    plt.show()

# Exemple d'utilisation des fonctions
filename_nsmass = 'web_app/compare/static/data/NS_Mass_PSRJ1614-2230_NANOgrav11yr_mass_shapiro_1_MeanErrors.txt'
#filename_nsspin = 'web_app/compare/static/data/NS_Spin_PSRJ1748-2446ad_2005_spin_1_MeanErrors.txt'

# Traitement des données
data, pdf, mass_scale, sigma_values = process_meanerrors_nsmass(filename_nsmass)
#data, pdf, frequency_scale, sigma_values = process_meanerrors_nsspin(filename_nsspin)

# Sauvegarde des données dans un fichier HDF5
save_meanerrors_nsmass_to_h5(filename_nsmass.replace('.txt', '.h5'), pdf, sigma_values, mass_scale)
#save_meanerrors_nsspin_to_h5(filename_nsspin.replace('.txt', '.h5'), pdf, sigma_values, frequency_scale)

# Génération et affichage du graphique
generate_plot_nsmass(pdf, mass_scale, data[0], data[1])
