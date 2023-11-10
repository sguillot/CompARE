import os
import numpy as np
from tk_compare import env
import matplotlib.pyplot as plt

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
            print('   convert pdf into contour (to be done)')
            print('   name:',data[skey]['name'])
            rad, mass, pdf = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
            max_pdf = max( pdf )
            rad = np.array( list( set( rad ) ) )
            mass = np.array( list( set( mass ) ) )
            #print( 'len(rad):',rad.size )
            #print( 'rad:',rad)
            #print( 'len(mass):',str(mass.size) )
            #print( 'mass:',mass)
            #print( 'len(pdf):',str(pdf.size),str(rad.size*mass.size) )
            #print( 'max_pdf',max_pdf )
            apdf = np.array(pdf).reshape( rad.size, mass.size )
            for scl in data[skey]['CL']:
                icl = int( scl )
                print('   cl:',scl,str(icl),icl*max_pdf/100)
                cs = plt.contour(rad, mass, apdf, levels=[icl*max_pdf/100])
                #print('cs:',cs.collections[0].get_paths())
                p = cs.collections[0].get_paths()[0]
                v = p.vertices
                x = v[:,0]
                y = v[:,1]
                #print('x:',x)
                #print('y:',y)
                cont = np.array( [x, y], dtype = np.float)
                #print('  data_out:',env.path_data_out_file)
                #print('  data:',data[skey]['name'])
                #print('  CL:',scl)
                np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', cont, header='CL '+scl )
        #
        elif data[skey]['type'] == 'mcmc':
        #
            print('   convert mcmc into contour (to be done)')
        #
        else:
        #
            print('input type not understood')
            print('for key=',skey)
            exit()
    #
    if env.verb: print('Exit create_contours( )')

