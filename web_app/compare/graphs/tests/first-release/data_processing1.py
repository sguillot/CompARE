import os
import h5py
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# -----| Choice of the file to process and creation of H5 directory |----- #

def create_h5_directory():
    """
    Creates the directory 'web_app/compare/static/h5/' if it doesn't exist already.
    """
    h5_dir = "web_app/compare/static/h5/"
    if not os.path.exists(h5_dir):
        os.makedirs(h5_dir)

def process_data_to_h5(directory):
    """
    This function loops through all files in a given directory and creates HDF5 files for each data set.

    Args:
        directory (str): The path of the directory containing the data files.
    """
    for filename in os.listdir(directory):

        file_path = os.path.join(directory, filename)

        if filename.endswith("ProbaDistrib.txt"):

            print(f"Processing ProbaDistrib file: {file_path}")
            mass_grid, radius_grid, density, density_grid_mass_radius, max_pdf = process_probadistrib(file_path)
            output_h5_file = f"{os.path.splitext(filename)[0]}.h5"
            save_probadistrib_to_h5(mass_grid, radius_grid, density, density_grid_mass_radius, max_pdf, output_h5_file)
            print(f"Saved HDF5 file: {output_h5_file}")

        elif filename.endswith("Contours.txt"):

            print(f"Processing Chi2 Contours file: {file_path}")
            lines = read_text_file(file_path)
            group_titles, data = process_contours(lines)
            h5_file_name = f"{os.path.splitext(filename)[0]}.h5"
            save_contours_to_h5(h5_file_name, group_titles, data)
            print(f"Saved HDF5 file: {h5_file_name}")

        elif filename.endswith("MCMCSamples.txt"):

            print(f"Processing MCMCSamples file: {file_path}")
            contours, x_edges, y_edges, probabilities = process_mcmcsamples(file_path)
            h5 = f"{os.path.splitext(filename)[0]}.h5"
            save_mcmcsamples_to_h5(contours, x_edges, y_edges, probabilities, h5)
            print(f"Saved HDF5 file: {h5}")

# -----| Data Processing - ProbaDistrib |----- #
            
def process_probadistrib(file_path):
    """
    This function loads probability distribution data from a text file and sets parameters for probability density contours.

    Args:
        file_path (str): The path of the text file containing probability distribution data.
    """

    # Load probability distribution data
    data = np.loadtxt(file_path)

    # Extract mass and radius data
    R = data[:, 0]
    M = data[:, 1]
    density = data[:, 2]

    # Create a probability density grid for mass and radius
    mass_grid = np.unique(M)
    radius_grid = np.unique(R)
    density_grid_mass_radius = np.zeros((len(mass_grid), len(radius_grid)))

    # Fill the grid with density values
    for i in range(len(density)):
        mass_index = np.where(mass_grid == M[i])[0][0]
        radius_index = np.where(radius_grid == R[i])[0][0]
        density_grid_mass_radius[radius_index, mass_index] = density[i]

    # Find the maximum density value
    max_pdf = np.max(density)

    return mass_grid, radius_grid, density, density_grid_mass_radius, max_pdf

def save_probadistrib_to_h5(mass_grid, radius_grid, density, density_grid_mass_radius, max_pdf, output_h5_file):
    """
    This function computes probability density contours from radius, mass, and density data, then saves them into an HDF5 file.

    Args:
        R (array_like): Radius values.
        M (array_like): Mass values.
        density (array_like): Probability density values.
        output_h5_file (str): The path of the output HDF5 file.
    """

    # Confidence levels
    confidence_levels = [0.68, 0.95, 0.9999]

    # Colors
    colors = ['blue', 'green', 'red']

    # Initialize an HDF5 file to store contour coordinates
    with h5py.File(os.path.join('web_app/compare/static/h5/', output_h5_file), "w") as f:

        # Create a group for data
        data_group = f.create_group("data")
        # Add datasets for mass, radius, and density values
        data_group.create_dataset("Mass (M☉)", data=mass_grid)
        data_group.create_dataset("Radius (km)", data=radius_grid)
        data_group.create_dataset("Proba density", data=density_grid_mass_radius)

        # Create a group for probability density contours
        for i, level in enumerate(confidence_levels):

            # Find the density level corresponding to confidence level
            sol = optimize.root_scalar(lambda x, pdf, max_pdf, xcl: pdf[pdf > x * max_pdf].sum() - xcl * pdf.sum(),
                                    args=(density, max_pdf, level), x0=0.01, x1=1.0, rtol=0.01, maxiter=100)
            
            # Get the density level value
            xlev = sol.root

            # Plot probability density contours
            contour = plt.contour(radius_grid, mass_grid, density_grid_mass_radius, levels=[xlev * max_pdf], colors=colors[i], linestyles='dashed')
            
            # Access contour paths
            paths = contour.collections[0].get_paths()
            
            # Create a group for each confidence level
            confidence_group = f.create_group(f"{i+1}σ")
            
            # For each path, create a subgroup and save coordinates
            for path in paths:
                coordinates = path.vertices
                
                # Create a subgroup for each contour
                confidence_group.create_dataset(f"R_{i+1}σ M_{i+1}σ", data=coordinates) 

# -----| Data Processing - Chi2Contours |----- #
            
def read_text_file(filename):
    """
    Function to read data from a text file.
    
    Args:
        filename (str): The name of the text file to read.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    return lines

def process_contours(lines):
    """
    Function to extract data from lines.
    
    Args:
        lines (list): A list of lines from a text file.
    """
    data = {}
    group_titles = []
    for line in lines:
        if line.startswith('#'):
            # If it's a title line, extract group names
            group_names = line.strip().split()[1:]
            # Merge group names
            for i in range(0, len(group_names), 2):
                group_titles.append(f"{group_names[i]} {group_names[i+1]}")
                data[group_titles[-1]] = []
            continue
        values = line.strip().split()
        if len(values) % 2 != 0:
            raise ValueError("The number of values must be even (radii and masses).")
        num_entries = len(values) // 2
        for i in range(num_entries):
            data[group_titles[i]].append([float(values[2*i]), float(values[2*i+1])])
    return group_titles, data

def save_contours_to_h5(file_name, group_titles, data):
    """
    Function to save data into an HDF5 file.
    
    Args:
        file_name (str): The name of the output HDF5 file.
        group_titles (list): A list of group titles.
        data (dict): A dictionary containing data for each group.
    """
    # Create H5 directory if necessary
    create_h5_directory()

    with h5py.File(os.path.join('web_app/compare/static/h5/', file_name), 'w') as hf:
        for group_title in group_titles:
            new_group_title = group_title.split(" M_")[1]
            group = hf.create_group(f"{new_group_title}")
            group.create_dataset(group_title, data=data[group_title])

# -----| Data Processing - MCMCSamples |----- #
            
def process_mcmcsamples(file_path):
    """
    This function loads MCMCSamples data from a text file and sets parameters for probability density contours.

    Args:
        file_path (str): The path of the text file containing MCMCSamples data.
    """
    # Load MCMCSamples data
    data = np.loadtxt(file_path)

    # Extract mass and radius data
    mass = data[:, 0]
    radius = data[:, 1]

    # Set the number of bins for 2D histogram
    bin_size = [0.1, 0.05]
    num_bins_mass = int((max(mass) - min(mass)) / bin_size[0])
    num_bins_radius = int((max(radius) - min(radius)) / bin_size[1])

    # Compute 2D histogram: x_edges and y_edges are bin edges; hist is histogram containing the number of points in each bin
    hist, x_edges, y_edges = np.histogram2d(mass, radius, bins=[num_bins_mass, num_bins_radius])

    # Normalize histogram to get probabilities
    total_points = np.sum(hist)
    probabilities = hist / total_points

    levels=[0.68, 0.95, 0.9999]

    # Compute contours

    # Flatten histogram and sort values
    Hflat = hist.flatten()
    # Sort histogram values in descending order
    inds = np.argsort(Hflat)[::-1]
    # Arrange histogram values according to sorted indices
    Hflat = Hflat[inds]
    # Compute cumulative sum of histogram values
    sm = np.cumsum(Hflat)
    # Normalize cumulative sum values
    sm /= sm[-1]
    # Empty array to store computed contour values
    V = np.empty(len(levels))
    # For each contour level
    for i, v0 in enumerate(levels):
        try:
            # Find histogram value corresponding to contour level
            V[i] = Hflat[sm <= v0][-1]
        except IndexError:
            V[i] = Hflat[0]
    # Sort contour values
    V.sort()
    m = np.diff(V) == 0
    # If contour values are equal, multiply them by 1 - 1e-4
    if np.any(m):
        V[np.where(m)[0][0]] *= 1.0 - 1e-4
    V.sort()

    # Compute bin centers
    X1, Y1 = np.meshgrid(x_edges[:-1] + 0.5 * np.diff(x_edges), y_edges[:-1] + 0.5 * np.diff(y_edges))

    # Extend the array for the sake of the contours at the plot edges.
    H2 = np.zeros((hist.shape[0] + 4, hist.shape[1] + 4))
    H2[2:-2, 2:-2] = hist
    H2[2:-2, 1] = hist[:, 0]
    H2[2:-2, -2] = hist[:, -1]
    H2[1, 2:-2] = hist[0]
    H2[-2, 2:-2] = hist[-1]
    H2[1, 1] = hist[0, 0]
    H2[1, -2] = hist[0, -1]
    H2[-2, 1] = hist[-1, 0]
    H2[-2, -2] = hist[-1, -1]

    X2 = np.concatenate(
        [
            X1[0, 0] + np.array([-2, -1]) * (X1[0, 1] - X1[0, 0]),
            X1[0],
            X1[0, -1] + np.array([1, 2]) * (X1[0, -1] - X1[0, -2]),
        ]
    )
    Y2 = np.concatenate(
        [
            Y1[0, 0] + np.array([-2, -1]) * (Y1[1, 0] - Y1[0, 0]),
            Y1[:, 0],
            Y1[-1, 0] + np.array([1, 2]) * (Y1[-1, 0] - Y1[-2, 0]),
        ]
    )

    # Plot contours
    contours = plt.contour(X2, Y2, H2.T, V, colors=['blue', 'green', 'red'])

    return contours, x_edges, y_edges, probabilities

def save_mcmcsamples_to_h5(contours, x_edges, y_edges, probabilities, file_path):
    """
    Saves probability density contours into an HDF5 file.

    Args:
        contours: Probability density contours.
        x_edges (array_like): Bin edges in x.
        y_edges (array_like): Bin edges in y.
        probabilities (array_like): Probabilities associated with each bin.
        output_h5_file (str): The path of the output HDF5 file.
    """
    # Create a dictionary to store coordinates for each color
    contour_coords = {}
    colors_titles = {'00_00_255': '3σ', '00_128_00': '2σ', '255_00_00': '1σ'}

    # Collecting coordinates for each color
    for collection in contours.collections:
        color = collection.get_edgecolor()[0][:3]
        color_str = "_".join([f"{int(x * 255):02d}" for x in color[:3]])
        if color_str not in contour_coords:
            contour_coords[color_str] = []

        for path in collection.get_paths():
            contour_coords[color_str].append(path.vertices)

    # Create H5 directory if necessary
    create_h5_directory()

    with h5py.File(os.path.join('web_app/compare/static/h5/', file_path), "w") as hf:
        # Create a group for data
        data_group = hf.create_group("data")
        
        # Store bin coordinates
        data_group.create_dataset("Radius (km)", data=x_edges)
        data_group.create_dataset("Mass (M☉)", data=y_edges)
        
        # Store probabilities
        data_group.create_dataset("Proba density", data=probabilities)

        for color, coords_list in contour_coords.items():

            # Creating a group for each color
            main_group_name = colors_titles[color]
            grp = hf.create_group(main_group_name)

            # Storing coordinates for each contour
            for coords in coords_list:
                grp.create_dataset(f"R_{main_group_name} M_{main_group_name}", data=coords)

    return contour_coords