import os
from tk_compare import env
import h5py
import numpy as np
from time import gmtime, strftime

def create_h5_file( ):
    #
    if env.verb: print('Enter create_hd5_file( )')
    #
    timestamp=strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    print("time:",timestamp)
    #
    f = h5py.File( env.h5file, "w" )
    f.create_dataset('timestamp', data=timestamp)
    f.close()
    #
    # read the data dictionary
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    # dictionary keys:
    skeys = data.keys()
    if env.verb: print('   show data dictionary keys:')
    if env.verb: print('   ',skeys)
    #
    # loop over the keys
    #
    for skey in skeys:
        print('   skey:',skey)
        print('   name:',data[skey]['name'])
        if data[skey]['type'] == 'contour':
            ncl = len( data[skey]['CL'] )
            f = h5py.File( env.h5file, "a")
            #grp = f.create_group('group')
            grp_skeys = f.create_group(skey)
            #
            for i in np.arange(ncl):
                #f = h5py.File( env.h5file, "a")
                scl = data[skey]['CL'][i]
                #grp_skeys_scl = grp_skeys.create_group(scl)
                fname = env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt'
                if not os.path.isfile( fname ):
                    print('The file does not exist ',fname)
                    continue
                print('The file does exists ',fname)
                cont_R, cont_M = np.loadtxt( fname )
                grp_skeys.create_dataset('rad'+scl,data=cont_R)
                grp_skeys.create_dataset('mas'+scl,data=cont_M)
                #f.create_dataset(skey+'rad'+scl,data=cont_R)
                #f.create_dataset(skey+'mas'+scl,data=cont_M)
                #f.close()
            f.close()

            # store contours:
            #fname = env.path_data_out_file+'/'+data[skey]['name']+'.cont'
            #if not os.path.isfile( fname ):
            #    print('The file does not exist ',fname)
            #    continue
            #print('The file does exists ',fname)
            #cont_R, cont_M = np.loadtxt( fname, usecols=(0, 1), unpack = True )
            #if cont_R[0] != cont_R[-1]:
            #    cont_R = np.append(cont_R, cont_R[0])
            #    cont_M = np.append(cont_M, cont_M[0])
            #print('Radius:',cont_R[0:-1:10])
            #print('Mass:',cont_M[0:-1:10])

    #if key[skey]['type'] == 'contour':
    #    #print('copy ',env.path_data_file,key[skey],'.txt')
    #    print(f'   copy {env.path_data_file+"/"+key[skey]["name"]+".txt"}')
    #    print(f'     to {env.path_data_out_file+"/"+key[skey]["name"]+".cont"}')
    #    os.system('cp '+env.path_data_file+'/'+key[skey]['name']+'.txt '+env.path_data_out_file+'/'+key[skey]['name']+'.cont')
    #if key[skey]['type'] == 'pdf':
    #    print(f'   convert pdf into contour (to be done)')
    #
    if env.verb: print('Exit create_hd5_file( )')


def get_dataset( skey ):
    f = h5py.File(env.h5file, 'r')
    return f[skey]

def read_h5_file( ):
    #
    if env.verb: print('Enter read_hd5_file( )')
    #
    skey = 'timestamp'
    #ds = get_dataset( skey[0] )
    #print(ds)
    #
    with h5py.File( env.h5file, 'r') as f1:
        #print("   Keys: %s" % f1.keys())
        print( '   name',f1.name)
        print( '   keys:', f1.keys() )
        skeys = list( f1.keys() )
        skeys.remove('timestamp')
        print( '   skeys:', skeys )
        #a_group_key = list(f1.keys())[0]
        #print( '   keys[0]:', a_group_key )
        #rint( '   type(keys[0]):', type(f1[a_group_key]) )
        ts = f1['timestamp'][()]
        print( '   ts:', ts )
        for skey in skeys:
            print('skey:',skey)
            grp_skey = f1[skey]
            print('group keys',grp_skey.keys())
            for key in grp_skey.keys():
                print('grp_skey.keys():',key)
                data = grp_skey[key][()]
                print('data:',data)
    #
    if env.verb: print('Exit read_hd5_file( )')
