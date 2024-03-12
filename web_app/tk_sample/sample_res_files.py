
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_res_qLMXB
from tk_compare import create_res_Mass
from tk_compare import create_res_Spin
from tk_compare import show_res_qLMXB
from tk_compare import show_res_Mass
from tk_compare import show_res_Spin

def main():
    #
    print(50*'-')
    #
    # read file qLMXB and store data in res_qLMXB
    #
    res_qLMXB = create_res_qLMXB( )
    #
    print(50*'-')
    #
    # show dictionary stored in res_qLMXB
    #
    show_res_qLMXB( res_qLMXB )
    #
    print(50*'-')
    #
    # read file Mass and store data in res_Mass
    #
    res_Mass = create_res_Mass( )
    #
    print(50*'-')
    #
    # show dictionary stored in res_Mass
    #
    show_res_Mass( res_Mass )
    #
    print(50*'-')
    #
    # read file Spin and store data in res_Spin
    #
    res_Spin = create_res_Spin( )
    #
    print(50*'-')
    #
    # show dictionary stored in res_Spin
    #
    show_res_Spin( res_Spin )
    #
    print(50*'-')
    
if __name__ == "__main__":
    main()
