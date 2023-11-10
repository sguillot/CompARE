import os
import numpy as np
from tk_compare import env

def read_file( ):
    #
    if env.verb: print('Enter read_file( )')
    #
    # define the key
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    skeys = data.keys()
    #if env.verb: print('   show dictionary key:')
    #if env.verb: print('   ',key)
    res = {}
    #
    # loop over skeys
    #
    for skey in skeys:
        res[skey] = {}
        res[skey]['name']  = data[skey]['name']
        res[skey]['type']  = data[skey]['type']
        res[skey]['line']  = data[skey]['line']
        res[skey]['color'] = data[skey]['color']
        res[skey]['CL']    = data[skey]['CL']
        for ind,scl in enumerate( data[skey]['CL'] ):
            res[skey][scl] = {}
            fname = env.path_data_out_file+'/'+data[skey]['name']+'CL'+scl+'.txt'
            if not os.path.isfile( fname ):
                print('The file does not exist ',fname)
                continue
            print('The file does exists ',fname)
            cont_R, cont_M = np.loadtxt( fname )
            res[skey][scl]['rad'] = cont_R
            res[skey][scl]['mas'] = cont_M
    #
    return res
    #
    if env.verb: print('Exit read_file( )')

