import os
import numpy as np
from tk_compare import env
from scipy import optimize
import matplotlib.pyplot as plt

def fcl(x, apdf, max_pdf, xcl):
    return apdf[apdf>x*max_pdf].sum()-xcl*apdf.sum()

def create_contours( ):
    #
    if env.verb: print('Enter create_contours( )')
    #
    # read the dictionary
    #
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    if not os.path.isdir(env.path_data_out_file):
        os.system('mkdir '+env.path_data_out_file)
    #
    skeys = data.keys()
    #
    # loop over skeys
    #
    for skey in skeys:
        #
        print('For key = ',skey)
        #
        if data[skey]['type'] == 'contour':
        #
            ncl = len( data[skey]['CL'] )
            if ncl == 2:
                r1, m1, r2, m2 = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)]; r2 = r2[~np.isnan(r2)]
                m1 = m1[~np.isnan(m1)]; m2 = m2[~np.isnan(m2)]
                #
                if r1[0] != r1[-1] and m1[0] != m1[-1]:
                    r1 = np.append(r1, r1[0]); m1 = np.append(m1, m1[0])
                if r2[0] != r2[-1] and m2[0] != m2[-1]:
                    r2 = np.append(r2, r2[0]); m2 = np.append(m2, m2[0])
                #
                data1 = np.array( [r1, m1], dtype = np.float)
                data2 = np.array( [r2, m2], dtype = np.float)
            elif ncl ==3:
                r1, m1, r2, m2, r3, m3 = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)]; r2 = r2[~np.isnan(r2)]; r3 = r3[~np.isnan(r3)]
                m1 = m1[~np.isnan(m1)]; m2 = m2[~np.isnan(m2)]; m3 = m3[~np.isnan(m3)]
                #
                if r1[0] != r1[-1] and m1[0] != m1[-1]:
                    r1 = np.append(r1, r1[0]); m1 = np.append(m1, m1[0])
                if r2[0] != r2[-1] and m2[0] != m2[-1]:
                    r2 = np.append(r2, r2[0]); m2 = np.append(m2, m2[0])
                if r3[0] != r3[-1] and m3[0] != m3[-1]:
                    r3 = np.append(r3, r3[0]); m3 = np.append(m3, m3[0])
                #
                data1 = np.array( [r1, m1], dtype = np.float)
                data2 = np.array( [r2, m2], dtype = np.float)
                data3 = np.array( [r3, m3], dtype = np.float)
            #
            for ind,scl in enumerate(data[skey]['CL']):
                print('   save data in ',data[skey]['name']+'CL'+scl+'.txt')
                if ind == 0:
                    np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', data1, header='CL '+scl )
                elif ind == 1:
                    np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', data2, header='CL '+scl )
                elif ind == 2:
                    np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', data3, header='CL '+scl )
        #
        elif data[skey]['type'] == 'pdf':
        #
            print('   name:',data[skey]['name'])
            rad, mass, pdf = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
            max_pdf = max( pdf )
            print('  max_pdf:',max_pdf)
            rad = np.array( list( set( rad ) ) )
            mass = np.array( list( set( mass ) ) )
            apdf = np.array(pdf).reshape( rad.size, mass.size )
            for scl in data[skey]['CL']:
                print('   cl:',scl)
                icl = int( scl )
                xcl = float( icl/100.0 )
                sol = optimize.root_scalar(fcl, args=(apdf,max_pdf,xcl), x0=1.0-xcl, x1=min(1.0,1.3-xcl), rtol=0.01, maxiter=100)
                xlev = sol.root
                print('   xlev:',xlev)
                cs = plt.contour(rad, mass, apdf, levels=[xlev*max_pdf])
                p = cs.collections[0].get_paths()[0]
                v = p.vertices
                x = v[:,0]
                y = v[:,1]
                cont = np.array( [x, y], dtype = np.float)
                np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', cont, header='CL '+scl )
        #
        elif data[skey]['type'] == 'mcmc':
        #
            print('   convert mcmc into contour (to be done)')
            print('   name:',data[skey]['name'])
            rad, mass = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
            pdf, rad, mass = np.histogram2d( rad, mass, bins=30, density = True )
            rad = rad[1:]
            mass = mass[1:]
            pdf = pdf.T
            max_pdf = np.max( pdf )
            print('  max_pdf:',max_pdf)
            #print('  rad:',rad,rad.size)
            #print('  mass:',mass,mass.size)
            #print('  pdf.size:',pdf.size,30*30)
            for scl in data[skey]['CL']:
                print('   cl:',scl)
                icl = int( scl )
                xcl = float( icl/100.0 )
                sol = optimize.root_scalar(fcl, args=(pdf,max_pdf,xcl), x0=1.0-xcl, x1=min(1.0,1.3-xcl), rtol=0.01, maxiter=100)
                xlev = sol.root
                print('   xlev:',xlev)
                cs = plt.contour(rad, mass, pdf, levels=[xlev*max_pdf])
                p = cs.collections[0].get_paths()[0]
                v = p.vertices
                x = v[:,0]
                y = v[:,1]
                cont = np.array( [x, y], dtype = np.float)
                np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', cont, header='CL '+scl )
        #
        else:
        #
            print('input type not understood')
            print('for key=',skey)
            exit()
    #
    if env.verb: print('Exit create_contours( )')

