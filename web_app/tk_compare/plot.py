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
    lnames = []
    #
    for ind,skey in enumerate(skeys):
        sind = str(ind)
        ncl = len( data[skey]['CL'] )
        if from_data:
            res_data[sind] = {}
            name = data[skey]['name'].split('-')
            name_new = name[0]+'-'+name[1]
            if name_new not in lnames:
                lnames.append(name_new)
                color = col[ind]
            print('names 0+1',name_new)
            for i in np.arange(ncl):
                scl = data[skey]['CL'][i]
                res_data[sind][scl] = {}
                fname = env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt'
                if not os.path.isfile( fname ):
                    print('The file does not exist ',fname)
                    continue
                print('The file does exists ',fname)
                cont_R, cont_M = np.loadtxt( fname )
                #cont_R, cont_M = np.loadtxt( fname, usecols=(0, 1), unpack = True )
                print('cont_R',cont_R)
                print('cont_M',cont_M)
                if cont_R[0] != cont_R[-1]:
                    cont_R = np.append(cont_R, cont_R[0])
                    cont_M = np.append(cont_M, cont_M[0])
                res_data[sind][scl]['rad'] = cont_R
                res_data[sind][scl]['mas'] = cont_M
                if 'hydrogen' in data[skey]['name']:
                    res_data[sind][scl]['line'] = 'dashed'
                    res_data[sind][scl]['color'] = color
                elif 'helium' in data[skey]['name']:
                    res_data[sind][scl]['line'] = 'dotted'
                    res_data[sind][scl]['color'] = color
        if from_h5:
            print('to be done')
            exit()
    #
    # plot the figure with contours
    #
    scls = [ '68', '90', '95', '99']
    ncls = len( scls )
    for ind, scl in enumerate( scls ):
        if ndim == 1:
            plotname = pname+'_'+data[skey]['name']+'CL'+scl+'.pdf'
        else:
            plotname = pname+'_several'+'CL'+scl+'.pdf'
        #
        fig, axs = plt.subplots(1,1)
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig.subplots_adjust(left=0.12, bottom=0.1, right=None, top=None, wspace=0.6, hspace=0.3)
        #plt.title('MR Contours')
        #
        axs.set_xlabel(r'Radius (km)')
        axs.set_ylabel(r'Mass (M$_\odot$)')
        axs.set_xlim(5,18)
        axs.set_ylim(0.4,2.7)
        for ind,skey in enumerate(skeys):
            sind = str(ind)
            if scl in data[skey]['CL']:
                axs.plot( res_data[sind][scl]['rad'], res_data[sind][scl]['mas'], linestyle=res_data[sind][scl]['line'], color=res_data[sind][scl]['color'], label=data[skey]['name'] )
        axs.text(6,2.5,scl+'% CL')
        axs.legend(loc='upper right',fontsize='xx-small')
        #
        plt.savefig(plotname)


    #
    if env.verb: print('Exit create_plot_contour( skey, from_data, from_h5, pname )')

