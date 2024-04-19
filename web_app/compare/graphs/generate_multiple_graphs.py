import h5py
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins
import os

def plot_contours_from_checkboxes(selected_filepaths):
    # Create a new matplotlib figure
    fig, ax = plt.subplots()

    #l = []

    # Browse selected file names
    for i, filepath in enumerate(selected_filepaths):

        # Open the HDF5 file in read mode
        with h5py.File(filepath, "r") as hf:
            # Extract data from HDF5 file
            mass = hf["data"]["Mass (M☉)"][:]
            radius = hf["data"]["Radius (km)"][:]
            density = hf["data"]["Proba density"][:]
            contours = hf["data"]["Contours"][:]

            # Create contour plot
            levels = sorted(contours)
            CS = ax.contour(radius, mass, density, levels=levels, colors='C{}'.format(i))

            #h = CS.collections
            #l.append(filename)

    ax.set_title('Contour Plot')
    ax.set_xlabel('Radius (km)')
    ax.set_ylabel('Mass (M☉)')

    #ax.legend(h,l)

    # Add the plugin to display coordinates when hovering over the graph
    plugins.connect(fig, plugins.MousePosition(fontsize=14, fmt=".3f"))

    # Return graph HTML
    return mpld3.fig_to_html(fig)