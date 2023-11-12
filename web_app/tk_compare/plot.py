import os
import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
from tk_compare import env

col = [ 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'orange', 'purple', 'brown', 'pink', 'olive' ]

def create_plot_qLMXB_contour_A( res, skeys, scls, pname ):
    #
    if env.verb: print('Enter create_plot_contour_A( res, skeys, scls, pname )')
    #
    # plot the figure with contours
    #
    for scl in scls:
        if len(skeys) == 1:
            plotname = pname+'-'+res[skey]['name']+'-CLA'+scl+'.pdf'
        else:
            plotname = pname+'-several'+'-CLA'+scl+'.pdf'
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
            if scl in res[skey]['CL_A']:
                axs.plot( res[skey][scl]['rad'], res[skey][scl]['mas'], linestyle=res[skey]['line'], color=res[skey]['color'], label=res[skey]['name'] )
        axs.text(6,2.5,scl+'% CL(authors)')
        axs.legend(loc='upper right',fontsize='xx-small')
        plt.savefig(plotname)
    #
    if env.verb: print('Exit create_plot_contour_A( res, skeys, scls, pname )')

def create_plot_qLMXB_contour_C( res, skeys, scls, pname ):
    #
    if env.verb: print('Enter create_plot_contour_C( res, skeys, scls, pname )')
    #
    # plot the figure with contours
    #
    for scl in scls:
        if len(skeys) == 1:
            plotname = pname+'-'+res[skey]['name']+'-CLC'+scl+'.pdf'
        else:
            plotname = pname+'-several'+'-CLC'+scl+'.pdf'
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
            if scl in res[skey]['CL_C']:
                axs.plot( res[skey][scl]['rad'], res[skey][scl]['mas'], linestyle=res[skey]['line'], color=res[skey]['color'], label=res[skey]['name'] )
        axs.text(6,2.5,scl+'% CL(created)')
        axs.legend(loc='upper right',fontsize='xx-small')
        plt.savefig(plotname)
    #
    if env.verb: print('Exit create_plot_contour_C( res, skeys, scls, pname )')

def fcl(x, apdf, max_pdf, xcl):
    return apdf[apdf>x*max_pdf].sum()-xcl*apdf.sum()

def create_plot_qLMXB_pdf( res, skeys, scls, pname ):
    #
    if env.verb: print('Enter create_plot_pdf( res, skeys, scls, pname )')
    #
    # plot the figure with pdf
    #
    for skey in skeys:
        if res[skey]['type'] == 'pdf' or res[skey]['type'] == 'mcmc':
            print('name:',res[skey]['name'])
            plotname = pname+'-'+res[skey]['name']+'-pdf.pdf'
            fig, axs = plt.subplots(1,1)
            fig.tight_layout() # Or equivalently,  "plt.tight_layout()"
            fig.subplots_adjust(left=0.12, bottom=0.1, right=None, top=None, wspace=0.6, hspace=0.3)
            #plt.title('MR Contours')
            axs.set_xlabel(r'Radius (km)')
            axs.set_ylabel(r'Mass (M$_\odot$)')
            #axs.set_xlim(5,18)
            #axs.set_ylim(0.4,2.7)
            # plot pdf
            axs.pcolor( res[skey]['pdf']['rad'], res[skey]['pdf']['mass'], res[skey]['pdf']['pdf'] )
            # plot contours
            max_pdf = np.amax( res[skey]['pdf']['pdf'] )
            scls = ['68', '90', '95', '99']
            for ind,scl in enumerate( scls ):
                print('   scl:',scl)
                icl = int( scl )
                xcl = float( icl/100.0 )
                sol = optimize.root_scalar(fcl, args=( res[skey]['pdf']['pdf'], max_pdf, xcl ), x0=1.0-xcl, x1=min(1.0,1.3-xcl), rtol=0.01, maxiter=100)
                xlev = sol.root
                print('   xlev:',xlev)
                cs = axs.contour(res[skey]['pdf']['rad'], res[skey]['pdf']['mass'], res[skey]['pdf']['pdf'], levels=[xlev*max_pdf] )
                if scl in res[skey]['CL_C']:
                    axs.plot( res[skey][scl]['rad'], res[skey][scl]['mas'], linestyle='dashed', color=col[ind+1], label=scl )
            #axs.text(6,2.5,scl+'% CL')
            axs.legend(loc='upper right',fontsize='xx-small')
            plt.savefig(plotname)
    #
    if env.verb: print('Exit create_plot_pdf( res, skeys, scls, pname )')
    