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
    # Create a new matplotlib figure
    fig, ax = plt.subplots()

    # Define subfolders containing data files
    eos_folder = os.path.join(settings.STATIC_ROOT, 'static', 'eos_radius_mass')
    
    # Find all subfolders in the EOS folder
    subfolders = [subfolder for subfolder in os.listdir(eos_folder) if os.path.isdir(os.path.join(eos_folder, subfolder))]

    # Define a counter
    counter = 0

    # Lists to store colors ans contour data
    unique_colors, all_contour_data = [], []

    # Browse selected file names
    for i, filepath in enumerate(selected_filepaths):

        if selected_filepaths[i].endswith("ProbaDistrib.h5") or selected_filepaths[i].endswith("MCMCSamples.h5"):

            counter += 1
            # Open the HDF5 file in read mode
            with h5py.File(filepath, "r") as hf:
                # Extract data from HDF5 file
                mass = hf["data"]["Mass (M☉)"][:]
                print(mass)
                radius = hf["data"]["Radius (km)"][:]
                density = hf["data"]["Proba density"][:]
                contours = hf["data"]["Contours"][:]

                # Store contour data
                all_contour_data.append((radius, mass, density, contours))

    # Determine x and y limits based on contour data
    min_radius = min([min(radius) for radius, _, _, _ in all_contour_data])
    max_radius = max([max(radius) for radius, _, _, _ in all_contour_data])
    min_mass = min([min(mass) for _, mass, _, _ in all_contour_data])
    max_mass = max([max(mass) for _, mass, _, _ in all_contour_data])

    # Set x and y limits
    ax.set_xlim(min_radius, max_radius)
    ax.set_ylim(min_mass, max_mass)

    # Plot contours
    for i, (radius, mass, density, contours) in enumerate(all_contour_data):
        # Create contour plot
        levels = sorted(contours)
        ax.contour(radius, mass, density, levels=levels, colors='C{}'.format(i))

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
                plt.plot(radius, mass, label=f'{subfolder} - {filename[:-4]}', color='C{}'.format(i + counter))

                # Store the color used in the plot
                contour_color = 'C{}'.format(i + counter)
                rgba_color = to_rgba(contour_color)

                rgb_color = [int(255 * c) for c in rgba_color[:3]] 

                # Check if the color is already in unique_colors_list
                if tuple(rgb_color) not in unique_colors:
                    unique_colors.append(tuple(rgb_color)) # Store RGB color

    ax.set_title('Contour Plot')
    ax.set_xlabel('Radius (km)')
    ax.set_ylabel('Mass (M☉)')

    # Add the plugin to display coordinates when hovering over the graph
    plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))

    # Return graph HTML
    return mpld3.fig_to_html(fig), unique_colors