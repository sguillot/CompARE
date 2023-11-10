# Description 

This repository aims at providing scripts to setup the data.

To run the script, go to `../tk_sample` and launch:

`$ python3 sample_[script_name].py`

with the following `script_name`:

## 1- `dict_data`:

This script produces the dictionary file data.dict associating a given key to a file name and type (='contour' or 'pdf').
It also associates a color and a line type to a kind of data (for the plot).

## 2- `contours`:

This script read the input files stored in compare/static/data/ and convert it to various output data such as:
  - contour files
  - pdf
For the moment, the output files are stored into compare/static/data_out/ folder and are associated to a given confidence level (CL).

## 3- `read_file`:
  
This script reads ASCII files and store them all in `res` dictionary.  
  
## 4- `create_h5`:

This script puts all the result files into a h5 single file.

## 5- `read_h5_user`:

This script reads the h5 file and store all the data in `res` dictionary.  

## 4- `plot_file`:

This script reads ASCII files and store them all in `res` dictionary (like `read_file`).
and then plots the output files.

For the plot, the user shall provide the list of keys associated to the contours to be plotted (in `skeys`), as well as the confidence levels (in `scls`) and the name pf the plot (in `pname`).


## 4- `plot_h5_user`:

This script reads the h5 file and store them all in `res` dictionary (like `read_h5`).
and then plots the output files.

For the plot, the user shall provide the list of keys associated to the contours to be plotted (in `skeys`), as well as the confidence levels (in `scls`) and the name pf the plot (in `pname`).

## `env`:

This file contains all the names and path to the data necessary for the toolkit.

The two codes with `_user` are script files which will be share to other users in the community to read the h5 file and produce plots. The other codes will be used by us and will not be shared with the community.