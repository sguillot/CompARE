import h5py
import matplotlib.pyplot as plt
from matplotlib.colors import to_rgba
import mpld3
import numpy as np
import os
from mpld3 import plugins
from django.conf import settings

import matplotlib
matplotlib.use('agg')

def plot_contours_from_checkboxes(selected_filepaths):
    """
    Plot contours and mean errors from selected HDF5 files.

    This function generates a matplotlib figure displaying contours and mean error lines
    based on selected HDF5 files. Depending on the file type identified in `selected_filepaths`,
    the function performs different plotting tasks:
    - For files ending with "ProbaDistrib.h5" or "MCMCSamples.h5", it extracts and plots contour
      data.
    - For files containing "NS_Mass" and ending with "MeanErrors.h5", it extracts and plots mean
      error data.
    - Additionally, it plots curves from .dat files found in subfolders of a predefined EOS data
      folder.
    
    Args:
        selected_filepaths (list): List of file paths to HDF5 files and .dat files.

    Returns:
        str, list, int: HTML representation of the plot, list of unique RGB colors used for EOS
        data plots, and either 0 or list of unique RGB colors used for mean error plots.

    Notes:
        This function utilizes Matplotlib, MPLD3, and HDF5 data handling via h5py.
        It expects specific data structures and naming conventions in HDF5 files for
        contour and mean error plotting.
    """
    # Create a new matplotlib figure
    fig, ax = plt.subplots()

    # Define subfolders containing data files
    eos_folder = os.path.join(settings.STATIC_ROOT, 'static', 'eos_radius_mass')
    
    # Find all subfolders in the EOS folder
    subfolders = [subfolder for subfolder in os.listdir(eos_folder) if os.path.isdir(os.path.join(eos_folder, subfolder))]

    # Define a counter
    counter, filenames_colors = 0, 0

    # Lists to store colors and contour data
    unique_colors_eos, unique_colors_errors, all_contour_data = [], [], []

    # Lists to store MeanErrors data
    mean_errors_mass_data = []

    # Browse selected file names
    for i, filepath in enumerate(selected_filepaths):

        if selected_filepaths[i].endswith("ProbaDistrib.h5") or selected_filepaths[i].endswith("MCMCSamples.h5"):
            counter += 1
            # Open the HDF5 file in read mode
            with h5py.File(filepath, "r") as hf:
                # Extract data from HDF5 file
                mass = hf["data"]["Mass (M☉)"][:]
                radius = hf["data"]["Radius (km)"][:]
                density = hf["data"]["Proba density"][:]
                contours = hf["data"]["Contours"][:]

                # Store contour data
                all_contour_data.append((radius, mass, density, contours))

        elif "NS_Mass" in selected_filepaths[i] and selected_filepaths[i].endswith("MeanErrors.h5"):
            counter += 1
            # Open the HDF5 file in read mode
            with h5py.File(filepath, "r") as hf:
                # Extract data from HDF5 file
                mass_meanerrors = hf["data"]["Mass (M☉)"][:]
                mean_errors_mass_data.extend([mass_meanerrors])

    if all_contour_data:

        # Determine x and y limits based on contour data
        min_radius = min([min(radius) for radius, _, _, _ in all_contour_data])
        max_radius = max([max(radius) for radius, _, _, _ in all_contour_data])
        min_mass = min([min(mass) for _, mass, _, _ in all_contour_data])
        max_mass = max([max(mass) for _, mass, _, _ in all_contour_data])

        # Set x and y limits
        ax.set_xlim(min_radius, max_radius)
        ax.set_ylim(min_mass, max_mass)

        # Plot contours
        for (radius, mass, density, contours) in all_contour_data:
            levels = sorted(contours)
            ax.contour(radius, mass, density, levels=levels, colors='C{}'.format(filenames_colors))
            filenames_colors += 1
    
    if mean_errors_mass_data:
        # Plot MeanErrors data
        for files in mean_errors_mass_data:
            # Generate x values for plotting horizontal lines
            x_values = np.arange(0, 18, 0.1)

            # Plot each pair of values in mass_data as a separate line
            for pair in files:
                ax.plot(x_values, [pair] * len(x_values), color='C{}'.format(filenames_colors))

                # Store the color used in the plot
                error_color = 'C{}'.format(filenames_colors)
                rgba_color = to_rgba(error_color)

                rgb_color = [int(255 * c) for c in rgba_color[:3]]

                # Check if the color is already in unique_colors_list
                if tuple(rgb_color) not in unique_colors_errors:
                    unique_colors_errors.append(tuple(rgb_color)) # Store RGB color

            filenames_colors += 1

    # Browse subfolders
    for i, subfolder in enumerate(subfolders):
        # Build path to subfolder
        folder_path = os.path.join(eos_folder, subfolder)

        # Browse .dat files in subfolder
        for filename in os.listdir(folder_path):
            if filename.endswith('.dat'):
                file_path = os.path.join(folder_path, filename)

                # Load data from .dat file, ignoring lines beginning with "#".
                data = np.loadtxt(file_path, comments='#')

                # Extract data columns (radius and mass)
                radius = data[:, 0]
                mass = data[:, 1]

                # Draw the curve
                plt.plot(radius, mass, color='C{}'.format(i + counter))

                # Store the color used in the plot
                contour_color = 'C{}'.format(i + counter)
                rgba_color = to_rgba(contour_color)

                rgb_color = [int(255 * c) for c in rgba_color[:3]] 

                # Check if the color is already in unique_colors_list
                if tuple(rgb_color) not in unique_colors_eos:
                    unique_colors_eos.append(tuple(rgb_color)) # Store RGB color

    if len(unique_colors_errors) == 0:
        unique_colors_errors = 0

    ax.set_title('Contour Plot')
    ax.set_xlabel('Radius (km)')
    ax.set_ylabel('Mass (M☉)')

    # Add the plugin to display coordinates when hovering over the graph
    plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))

    # Return graph HTML
    return mpld3.fig_to_html(fig), unique_colors_eos, unique_colors_errors