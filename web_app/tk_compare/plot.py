import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from tk_compare import env

def create_plot_contour( res, skeys, scls, pname ):
    #
    if env.verb: print('Enter create_plot_contour( res, skeys, scls, pname )')
    #
    # plot the figure with contours
    #
    for scl in scls:
        if len(skeys) == 1:
            plotname = pname+'_'+data[skey]['name']+'CL'+scl+'.pdf'
        else:
            plotname = pname+'_several'+'CL'+scl+'.pdf'
        #
        fig, axs = plt.subplots(1,1)
        fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
        fig.subplots_adjust(left=0.12, bottom=0.1, right=None, top=None, wspace=0.6, hspace=0.3)
        #plt.title('MR Contours')
        axs.set_xlabel(r'Radius (km)')
        axs.set_ylabel(r'Mass (M$_\odot$)')
        axs.set_xlim(5,18)
        axs.set_ylim(0.4,2.7)
        for skey in skeys:
            if scl in res[skey]['CL']:
                axs.plot( res[skey][scl]['rad'], res[skey][scl]['mas'], linestyle=res[skey]['line'], color=res[skey]['color'], label=res[skey]['name'] )
        axs.text(6,2.5,scl+'% CL')
        axs.legend(loc='upper right',fontsize='xx-small')
        plt.savefig(plotname)
    #
    if env.verb: print('Exit create_plot_contour( res, skeys, scls, pname )')

