import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

def main():
    #
    #
    # ------------------------------------------------------------------
    # READ INPUT FILES
    # ------------------------------------------------------------------
    #
    # reading the EoS-insensitive_posterior_samples.dat.gz file
    no_eos = pd.read_table('../data/gw/gw170817/EoS-insensitive_posterior_samples.dat.gz', delim_whitespace=True)
    # reading the high_spin_PhenomPNRT_posterior_samples.dat.gz file
    high_spin = pd.read_table('../data/gw/gw170817/high_spin_PhenomPNRT_posterior_samples.dat.gz', delim_whitespace=True)
    # reading the low_spin_PhenomPNRT_posterior_samples.dat.gz file
    low_spin = pd.read_table('../data/gw/gw170817/low_spin_PhenomPNRT_posterior_samples.dat.gz', delim_whitespace=True)
    #
    # 1D histogram of the "lambda1" parameter
    # high_spin.hist(column='lambda1', bins=50);
    #
    # redshift
    z=0.0099
    #
    # ------------------------------------------------------------------
    # PLOTS
    # ------------------------------------------------------------------
    #
    # ++++++++++++++++++++++++++++++++++++++
    # Plot Lambda_1 - Lambda_2 for low spin
    # ++++++++++++++++++++++++++++++++++++++
    #
    plotname='../plots/gw170817-L1-L2-lowspin.pdf'
    print('plot:',plotname)
    #
    # Low spin
    #
    # compute 2d histogram
    bins_x = 50
    bins_y = 50
    H, xedges, yedges = np.histogram2d(low_spin['lambda1'], low_spin['lambda2'], [bins_x, bins_y])
    #H, xedges, yedges = np.histogram2d(low_spin['lambda1']*(1+z), low_spin['lambda2']*(1+z), [bins_x, bins_y])
    X, Y = np.meshgrid(xedges[1:],yedges[1:])
    H=H.T
    #
    print(H)
    print(xedges)
    print(yedges)
    xmin=xedges.min()
    xmax=xedges.max()
    ymin=yedges.min()
    ymax=yedges.max()
    pmin=H.min()
    pmax=H.max()
    print("Min/Max H: {} {} ".format(pmin,pmax))
    print("Min/Max x: {} {} ".format(xmin,xmax))
    print("Min/Max y: {} {} ".format(ymin,ymax))
    norm=np.sum(np.sum( H, axis=0))
    print("Norm: {} ".format(norm))
    #
    # Draw figure for low spin
    #
    plt.figure()
    plt.title(r'correlation $\Lambda_1 - \Lambda_2$ (low spin)')
    plt.xlabel(r'$\Lambda_1$')
    plt.ylabel(r'$\Lambda_2$')
    # make the plot, using a "jet" colormap for colors
    #plt.contourf(X, Y, H, cmap='jet')
    #plt.imshow(H, interpolation='nearest', origin='low',cmap=cm.BuGn,extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    plt.imshow(H, interpolation='nearest', origin='lower', aspect='auto', cmap=cm.BuGn, extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
    #CS = plt.contour( X, Y, H, levels=[p90,p50], linewidths=2, colors=('black','black') )
    # Recast levels to new class
    #CS.levels = [nf(val) for val in CS.levels]
    #fmt = {}
    #strs = ['90', '50']
    #for l, s in zip(CS.levels, strs):
    #    fmt[l] = s
    # Label every other level using strings
    #loc =  [ (100,600), (400,500) ]
    #plt.clabel(CS, CS.levels, inline=True, fmt=fmt, fontsize=10, manual = [ (500,1500), (300,600) ] )
    plt.savefig(plotname)
    #plt.show()


    
if __name__ == "__main__":
    main()
