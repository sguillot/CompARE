
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_h5
from tk_compare import read_h5
from tk_compare import show_res

def main():
    #
    # create hd5 file containing all data with a key in the key dictionary
    #
    create_h5( )
    #
    print(50*'-')
    #
    # read hd5 file and store data in res
    #
    res = read_h5( )
    #
    # describe dictionary stored in res
    #
    show_res( res )
    #
    #
    #
    
if __name__ == "__main__":
    main()
