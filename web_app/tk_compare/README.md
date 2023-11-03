# Description 

This repository aims at providing scripts to setup the data.

To run the script, go to `../tk_sample` and launch:

`$ python3 sample_[script_name].py`

with the following `script_names`:

## 1- `dict_data.py`:

This script produces the dictionary file data.dict associating a given key to a file name and type (='contour' or 'pdf').

## 2- `contours.py`:

This script read the input files stored in data and convert it to various output data such as:
  - contour files
  - pdf
For the moment, the output files are stored into data_out folder and have an extension corresponding to the type of data.
  
## 3- `h5_file.py`:

This script puts all the result files into a h5 single file.

This script also reads the h5 file and provide results visible by users.

## 4- `plot.py`:

This script plots the output files.

## `env.py`:

This file contains all the names and path to the data necessary for the toolkit.