
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import read_h5
from tk_compare import show_res
from tk_compare import create_plot_contour

def main():
    #
    # read hd5 file and store data in res
    #
    res = read_h5( )
    #
    # describe dictionary stored in res
    #
    show_res( res )
    #
    # define the keys
    #
    #skeys = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7', 'qLMXB-8', 'qLMXB-9', 'qLMXB-10', 'qLMXB-11', 'qLMXB-12', 'qLMXB-13', 'qLMXB-14' ]
    skeys = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7' ]
    #
    scls = [ '68', '90', '95', '99']
    #
    pname = 'plot_contour_h5'
    #
    create_plot_contour( res, skeys, scls, pname )
    
    
if __name__ == "__main__":
    main()
