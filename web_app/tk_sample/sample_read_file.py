
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import read_file
from tk_compare import show_res

def main():
    #
    # read file and store data in res
    #
    res = read_file( )
    #
    # describe dictionary stored in res
    #
    show_res( res )
    #
    #
    #
    
if __name__ == "__main__":
    main()
