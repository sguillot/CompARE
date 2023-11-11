
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_res_qLMXB
from tk_compare import show_res_qLMXB

def main():
    #
    # read file and store data in res
    #
    res_qLMXB = create_res_qLMXB( )
    #
    # describe dictionary stored in res
    #
    show_res_qLMXB( res_qLMXB )
    #
    #
    #
    
if __name__ == "__main__":
    main()
