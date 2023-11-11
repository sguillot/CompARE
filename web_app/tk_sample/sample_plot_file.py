
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_res_qLMXB
from tk_compare import show_res_qLMXB
from tk_compare import create_plot_qLMXB_contour
from tk_compare import create_plot_qLMXB_pdf

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
    # define the keys
    #
    skeys_qLMXB = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7', 'qLMXB-8', 'qLMXB-9', 'qLMXB-10', 'qLMXB-11', 'qLMXB-12', 'qLMXB-13', 'qLMXB-14' ]
    #skeys = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7' ]
    #
    scls = [ '68', '90', '95', '99']
    #
    pname = 'plot_contour'
    #
    create_plot_qLMXB_contour( res_qLMXB, skeys_qLMXB, scls, pname )
    #
    skeys_qLMXB = [ 'qLMXB-9', 'qLMXB-10',  'qLMXB-11', 'qLMXB-12' ]
    #
    scls = [ '68', '95']
    #
    pname = 'plot_pdf'
    #
    create_plot_qLMXB_pdf( res_qLMXB, skeys_qLMXB, scls, pname )
    #
    
    
if __name__ == "__main__":
    main()
