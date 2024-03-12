
import sys
tk_compare = '../'
sys.path.insert(0, tk_compare)

from tk_compare import env
from tk_compare import create_res_qLMXB
from tk_compare import create_res_Mass
from tk_compare import create_res_Spin
from tk_compare import show_res_qLMXB
from tk_compare import create_plot_qLMXB_contour_A
from tk_compare import create_plot_qLMXB_contour_C
from tk_compare import create_plot_qLMXB_pdf
from tk_compare import create_plot_Mass
from tk_compare import create_plot_Spin

def main():
    #
    # --------------------------------------------------
    # qLMXB
    # --------------------------------------------------
    #
    print(50*'-')
    #
    # read file and store data in res
    #
    res_qLMXB = create_res_qLMXB( )
    #
    # describe dictionary stored in res
    #
    #show_res_qLMXB( res_qLMXB )
    #
    print(50*'-')
    #
    # define the keys
    #
    skeys_qLMXB = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7', 'qLMXB-8', 'qLMXB-9', 'qLMXB-10', 'qLMXB-11', 'qLMXB-12', 'qLMXB-13', 'qLMXB-14' ]
    #skeys = [ 'qLMXB-1', 'qLMXB-2', 'qLMXB-3', 'qLMXB-4', 'qLMXB-5', 'qLMXB-6', 'qLMXB-7' ]
    scls = [ '68', '90', '95', '99']
    pname = 'plot_contour'
    #
    create_plot_qLMXB_contour_A( res_qLMXB, skeys_qLMXB, scls, pname )
    #
    print(50*'-')
    #
    skeys_qLMXB = [ 'qLMXB-9', 'qLMXB-10',  'qLMXB-11', 'qLMXB-12' ]
    scls = [ '68', '95']
    pname = 'plot_pdf'
    #
    create_plot_qLMXB_pdf( res_qLMXB, skeys_qLMXB, scls, pname )
    #
    print(50*'-')
    #
    skeys_qLMXB = [ 'qLMXB-9', 'qLMXB-10',  'qLMXB-11', 'qLMXB-12' ]
    scls = [ '68', '90', '95', '99']
    pname = 'plot_contour'
    #
    create_plot_qLMXB_contour_C( res_qLMXB, skeys_qLMXB, scls, pname )
    #
    # --------------------------------------------------
    # Mass
    # --------------------------------------------------
    #
    print(50*'-')
    #
    # read file and store data in res_Mass
    #
    res_Mass = create_res_Mass( )
    #
    print(50*'-')
    #
    # define the keys
    #
    skeys_Mass = [ 'Mass-1', 'Mass-2', 'Mass-3']
    pname = 'plot_mass'
    #
    create_plot_Mass( res_Mass, skeys_Mass, pname )
    #
    print(50*'-')
    #
    # --------------------------------------------------
    # Spin
    # --------------------------------------------------
    #
    print(50*'-')
    #
    # read file and store data in res_Mass
    #
    res_Spin = create_res_Spin( )
    #
    print(50*'-')
    #
    # define the keys
    #
    skeys_Spin = [ 'Spin-1']
    pname = 'plot_spin'
    #
    #create_plot_Spin( res_Spin, skeys_Spin, pname )
    #
    print(50*'-')
    
if __name__ == "__main__":
    main()
