import os
from tk_compare import env
import h5py
import numpy as np
from time import gmtime, strftime

def create_h5( ):
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
    f = h5py.File( env.h5file, "a")
    for skey in skeys:
        print('   skey:',skey)
        print('   name:',data[skey]['name'])
        print('   type:',data[skey]['type'])
        print('   color:',data[skey]['color'])
        print('   line:',data[skey]['line'])
        grp_skey = f.create_group(skey)
        grp_skey.create_dataset('name',data=data[skey]['name'])
        grp_skey.create_dataset('type',data=data[skey]['type'])
        grp_skey.create_dataset('CL',data=data[skey]['CL'])
        grp_skey.create_dataset('color',data=data[skey]['color'])
        grp_skey.create_dataset('line',data=data[skey]['line'])
        #
        #if data[skey]['type'] == 'contour':
        #
        #ncl = len( data[skey]['CL'] )
        #f = h5py.File( env.h5file, "a")
        #
        for scl in data[skey]['CL']:
            #scl = data[skey]['CL'][i]
            grp_skey_scl = grp_skey.create_group(scl)
            fname = env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt'
            if not os.path.isfile( fname ):
                print('The file does not exist ',fname)
                continue
            print('The file does exists ',fname)
            cont_R, cont_M = np.loadtxt( fname )
            grp_skey_scl.create_dataset('rad',data=cont_R)
            grp_skey_scl.create_dataset('mas',data=cont_M)
            #grp_skeys.create_dataset('rad'+scl,data=cont_R)
            #grp_skeys.create_dataset('mas'+scl,data=cont_M)
        #f.close()
        #
    f.close()
    #
    if env.verb: print('Exit create_hd5_file( )')


#def get_dataset( skey ):
#    f = h5py.File(env.h5file, 'r')
#    return f[skey]

def read_h5( ):
    #
    if env.verb: print('Enter read_hd5_file( )')
    #
    res = {}
    with h5py.File( env.h5file, 'r') as f1:
        #print("   Keys: %s" % f1.keys())
        print( '   name',f1.name)
        print( '   keys:', f1.keys() )
        ts = f1['timestamp'][()].decode()
        print( '   ts:', ts )
        #
        skeys = list( f1.keys() )
        skeys.remove('timestamp')
        print( '   skeys:', skeys )
        #
        for skey in skeys:
            print('for skey:',skey)
            res[skey] = {}
            grp_skey = f1[skey]
            print('   grp_skey:', list( grp_skey.keys()) )
            res[skey]['name'] = grp_skey['name'][()].decode()
            res[skey]['type'] = grp_skey['type'][()].decode()
            res[skey]['color'] = grp_skey['color'][()].decode()
            res[skey]['line'] = grp_skey['line'][()].decode()
            #res[skey]['CL'] = grp_skey['CL'][()]
            scls = list( grp_skey.keys() )
            #print('group keys',scls)
            scls.remove('name'); scls.remove('type'); scls.remove('color'); scls.remove('line'); scls.remove('CL')
            #print('group keys',scls)
            res[skey]['CL'] = scls
            for scl in scls:
                print('   scl:',scl)
                res[skey][scl] = {}
                grp_skey_scl = grp_skey[scl]
                rad = grp_skey_scl['rad'][()]
                mas = grp_skey_scl['mas'][()]
                print('   rad:',rad)
                print('   mas:',mas)
                res[skey][scl]['rad'] = rad
                res[skey][scl]['mas'] = mas
    #
    if env.verb: print('Exit read_hd5_file( )')
    #
    return res


