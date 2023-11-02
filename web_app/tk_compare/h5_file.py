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
    # read the key dictionary
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_key, 'r') as f:
        key = eval(f.read())
    #
    # dictionary keys:
    skeys = key.keys()
    if env.verb: print('   show dictionary keys:')
    if env.verb: print('   ',skeys)
    #
    # loop over the keys
    #
    for skey in skeys:
        print('   skey:',skey)
        print('   name:',key[skey]['name'])
        #f = h5py.File("data.hdf5", "a")
        #grp = f.create_group('group')
        #grp = f.create_group(skey)
        # store contours:
        fname = env.path_data_out_file+'/'+key[skey]['name']+'.cont'
        if not os.path.isfile( fname ):
            print('The file does not exist ',fname)
            continue
        print('The file does exists ',fname)
        cont_R, cont_M = np.loadtxt( fname, usecols=(0, 1), unpack = True )
        if cont_R[0] != cont_R[-1]:
            cont_R = np.append(cont_R, cont_R[0])
            cont_M = np.append(cont_M, cont_M[0])
        print('Radius:',cont_R[0:-1:10])
        print('Mass:',cont_M[0:-1:10])
        #f.close()

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
        print( 'name',f1.name)
        print( 'keys:', list(f1.keys()) )
        ds = f1['timestamp']
        print( 'ds:', ds )
    #
    if env.verb: print('Exit read_hd5_file( )')
