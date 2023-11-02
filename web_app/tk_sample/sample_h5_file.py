
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_h5_file
from tk_compare import read_h5_file


def main():
    #
    # create hd5 file containing all data with a key in the key dictionary
    #
    create_h5_file( )
    #
    # read hd5 file
    #
    read_h5_file( )
    
    
if __name__ == "__main__":
    main()
