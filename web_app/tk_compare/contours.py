import os
import numpy as np
from tk_compare import env

def create_contours( skeys ):
    #
    if env.verb: print('Enter create_contours( skeys )')
    #
    # read the key dictionary
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    #if env.verb: print('   show dictionary data:')
    #if env.verb: print('   ',data)
    if not os.path.isdir(env.path_data_out_file):
        os.system('mkdir '+env.path_data_out_file)
    #
    # loop over skeys
    #
    for skey in skeys:
        if data[skey]['type'] == 'contour':
            ncl = len( data[skey]['CL'] )
            #print('copy ',env.path_data_file,data[skey],'.txt')
            #print(f'   copy {env.path_data_file+"/"+data[skey]["name"]+".txt"}')
            #print(f'     to {env.path_data_out_file+"/"+data[skey]["name"]+".cont"}')
            #os.system('cp '+env.path_data_file+'/'+data[skey]['name']+'.txt '+env.path_data_out_file+'/'+data[skey]['name']+'.cont')
            if ncl == 2:
                r1, m1, r2, m2 = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)]
                m1 = m1[~np.isnan(m1)]
                r2 = r2[~np.isnan(r2)]
                m2 = m2[~np.isnan(m2)]
                ndata1 = len(r1); ndata2 = len(r2)
                data1 = np.empty(shape=(2,ndata1))
                data2 = np.empty(shape=(2,ndata2))
                data1 = np.array( [r1, m1], dtype = np.float)
                data2 = np.array( [r2, m2], dtype = np.float)
                #print('data1:',data1)
                #print('data1[0]:',data1[0])
                #print('data1[1]:',data1[1])
            elif ncl ==3:
                r1, m1, r2, m2, r3, m3 = np.loadtxt(env.path_data_file+'/'+data[skey]['name']+'.txt', unpack=True, comments='#')
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)]
                m1 = m1[~np.isnan(m1)]
                r2 = r2[~np.isnan(r2)]
                m2 = m2[~np.isnan(m2)]
                r3 = r3[~np.isnan(r3)]
                m3 = m3[~np.isnan(m3)]
                ndata1 = len(r1); ndata2 = len(r2); ndata3 = len(r3)
                data1 = np.empty(shape=(2,ndata1))
                data2 = np.empty(shape=(2,ndata2))
                data3 = np.empty(shape=(2,ndata3))
                data1 = np.array( [r1, m1], dtype = np.float)
                data2 = np.array( [r2, m2], dtype = np.float)
                data3 = np.array( [r3, m3], dtype = np.float)
            #
            for i in np.arange(ncl):
                scl = data[skey]['CL'][i]
                print('save data in ',data[skey]['name']+'CL'+scl+'.txt')
                if i == 0:
                    np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', data1, header='CL '+scl )
                    #print('data1:',data1)
                elif i == 1:
                    np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', data2, header='CL '+scl )
                    #print('data2:',data2)
                elif i == 2:
                    np.savetxt( env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt', data3, header='CL '+scl )
                    #print('data3:',data3)
        if data[skey]['type'] == 'pdf':
            print('   convert pdf into contour (to be done)')
        if data[skey]['type'] == 'mcmc':
            print('   convert mcmc into contour (to be done)')
    #
    if env.verb: print('Exit create_contours( skeys )')

