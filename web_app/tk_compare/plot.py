import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from tk_compare import env

col = [ 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'orange', 'purple', 'brown', 'pink', 'olive' ]

def create_plot_contour( skeys, from_data, from_h5, pname ):
    #
    if env.verb: print('Enter create_plot_contour( skey, from_data, from_h5, pname )')
    #
    ndim = len(skeys)
    print('ndim:',ndim)
    #
    # define the key
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    #if env.verb: print('   show dictionary key:')
    #if env.verb: print('   ',key)
    if from_data:
        res_data = {}
    if from_h5:
        res_h5 = {}
    #
    # loop over skeys
    #
    for ind,skey in enumerate(skeys):
        sind = str(ind)
        if from_data:
            fname = env.path_data_out_file+'/'+data[skey]['name']+'.cont'
            if not os.path.isfile( fname ):
                print('The file does not exist ',fname)
                continue
            print('The file does exists ',fname)
            res_data[sind] = {}
            cont_R, cont_M = np.loadtxt( fname, usecols=(0, 1), unpack = True )
            if cont_R[0] != cont_R[-1]:
                cont_R = np.append(cont_R, cont_R[0])
                cont_M = np.append(cont_M, cont_M[0])
            res_data[sind]['rad'] = cont_R
            res_data[sind]['mas'] = cont_M
            if 'hydrogen' in data[skey]['name']:
                res_data[sind]['line'] = 'dashed'
            elif 'helium' in data[skey]['name']:
                res_data[sind]['line'] = 'dotted'

    #
    # plot the figure with contours
    #
    if ndim == 1:
        plotname = pname+'_'+data[skey]['name']+'.pdf'
    else:
        plotname = pname+'_several.pdf'
    fig, axs = plt.subplots(1,1)
    fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
    fig.subplots_adjust(left=0.12, bottom=0.1, right=None, top=None, wspace=0.6, hspace=0.3)
    #plt.title('Matter with baryons and leptons')
    # 
    axs.set_xlabel(r'Radius (km)')
    axs.set_ylabel(r'Mass (M$_\odot$)')
    axs.set_xlim(4,18)
    axs.set_ylim(0.4,3.2)
    for ind,skey in enumerate(skeys):
        sind = str(ind)
        axs.plot( res_data[sind]['rad'], res_data[sind]['mas'], linestyle=res_data[sind]['line'], color=col[ind], label=data[skey]['name'] )
    axs.legend(loc='upper right',fontsize='xx-small')
    #
    plt.savefig(plotname)


    #
    if env.verb: print('Exit create_plot_contour( skey, from_data, from_h5, pname )')

