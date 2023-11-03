
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_plot_contour

def main():
    #
    # define the keys
    #
    #skeys = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7', 'qLMXB-8', 'qLMXB-9', 'qLMXB-10', 'qLMXB-11', 'qLMXB-12', 'qLMXB-13', 'qLMXB-14' ]
    skeys = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7' ]
    #
    from_data = True
    from_h5 = False
    pname = 'plot_contour'
    #
    create_plot_contour( skeys, from_data, from_h5, pname )
    
    
if __name__ == "__main__":
    main()
