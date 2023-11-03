import os
import sys

print('In env.py:')
verb = True
#verb = False
print('   verb:',verb)
#
# Define where is the tk_sample folder
#
here = os.path.dirname(__file__)
print('   here:',here)
web_app= os.path.abspath(os.path.join(here, '..' ))
print('   web_app:',web_app)
#
# Define name of dict_key file
#
dict_data = os.path.abspath(os.path.join( web_app, 'tk_compare', 'dict_data.dict'))
if verb: print('   dict_data:',dict_data)
#
# Define path to the folders
#
path_data_file = os.path.abspath(os.path.join( web_app, 'compare', 'static', 'data'))
path_data_out_file = os.path.abspath(os.path.join( web_app, 'compare', 'static', 'data_out'))
#
if verb: print('   path_data_file:',path_data_file)
if verb: print('   path_data_out_file:',path_data_out_file)
#
# Define name of hd5 file
#
h5file = os.path.abspath(os.path.join( web_app, 'tk_compare', 'h5_file.h5'))
if verb: print('   h5file:',h5file)
#
print('Exit env.py:')
