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

def plot_contours_from_h5(file_path):

    if file_path.endswith("ProbaDistrib.h5") or file_path.endswith("MCMCSamples.h5"):

        # Create a new matplotlib figure
        fig, ax = plt.subplots()

        # Define subfolders containing data files
        eos_folder = os.path.join(settings.STATIC_ROOT, 'static', 'eos_radius_mass')
        
        # Find all subfolders in the EOS folder
        subfolders = [subfolder for subfolder in os.listdir(eos_folder) if os.path.isdir(os.path.join(eos_folder, subfolder))]

        # Lists to store colors
        unique_colors = []

        # Lists to store contour data
        all_contour_data = []

        # Open the HDF5 file in read mode
        with h5py.File(file_path, "r") as hf:
            # Extract data from HDF5 file
            mass = hf["data"]["Mass (M☉)"][:]
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
            ax.contour(radius, mass, density, levels=levels, colors='#000000')

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
                    plt.plot(radius, mass, label=f'{subfolder} - {filename[:-4]}', color='C{}'.format(i))

                    # Store the color used in the plot
                    contour_color = 'C{}'.format(i)
                    rgba_color = to_rgba(contour_color)

                    rgb_color = [int(255 * c) for c in rgba_color[:3]]

                    # Check if the color is already in the list
                    if tuple(rgb_color) not in unique_colors:
                        unique_colors.append(tuple(rgb_color))

        ax.set_title('Contour Plot')
        ax.set_xlabel('Radius (km)')
        ax.set_ylabel('Mass (M☉)')

        # Add the plugin to display coordinates when hovering over the graph
        plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))
        
    #elif file_path.endswith("Contours.h5"):
    #
    #    x_values = []
    #    y_values = []
    #
    #    # Extract data from H5 file
    #    with h5py.File(file_path, 'r') as hf:
    #        # Browse all groups 
    #        for group_name, group in hf.items():
    #            # Browse data sets in the group
    #            for subgroup_name, dataset in group.items():
    #                # Check subgroup names to extract mass and radius data
    #                if subgroup_name.startswith('R_'):
    #                    x_values.append(dataset[:, 0])
    #                    y_values.append(dataset[:, 1])
    #
    #    # Create a new matplotlib figure
    #    fig, ax = plt.subplots()
    #
    #    # Add dispersion data
    #    for i in range(len(x_values)):
    #        ax.plot(x_values[i], y_values[i], label=f'Dataset {i+1}')
    #
    #    # Add axis titles and labels
    #    ax.set_title('Scatter Plot')
    #    ax.set_xlabel('Radius (km)')
    #    ax.set_ylabel('Mass (M☉)')
    #    ax.legend()
    #
    #    # Add the plugin to display coordinates when hovering over the graph
    #    plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))

    return mpld3.fig_to_html(fig), unique_colors