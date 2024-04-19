import h5py
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

def plot_contours_from_h5(file_path):

    if file_path.endswith("ProbaDistrib.h5") or file_path.endswith("MCMCSamples.h5"):

        # List of outline colors
        colors = ['black', 'blue', 'green', 'yellow', 'red']

        # Create a new matplotlib figure
        fig, ax = plt.subplots()

        # Open the HDF5 file in read mode
        with h5py.File(file_path, "r") as hf:
            # Extract data from HDF5 file
            mass = hf["data"]["Mass (M☉)"][:]
            radius = hf["data"]["Radius (km)"][:]
            density = hf["data"]["Proba density"][:]
            contours = hf["data"]["Contours"][:]

            # Create contour plot
            levels = sorted(contours)
            ax.contour(radius, mass, density, levels=levels, colors=colors)

        ax.set_title('Contour Plot')
        ax.set_xlabel('Radius (km)')
        ax.set_ylabel('Mass (M☉)')
        ax.legend()

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

    return mpld3.fig_to_html(fig)