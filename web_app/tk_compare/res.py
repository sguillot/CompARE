import os
import numpy as np
from tk_compare import env

def create_res_qLMXB( ):
    #
    if env.verb: print('Enter create_res_qLMXB( )')
    #
    # define the key
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    res = {}
    #
    # loop over skeys
    #
    for skey in data['skeys']['qLMXB']:
        res[skey] = {}
        res[skey]['name']  = data[skey]['name']
        res[skey]['type']  = data[skey]['type']
        res[skey]['line']  = data[skey]['line']
        res[skey]['color'] = data[skey]['color']
        res[skey]['CL']    = data[skey]['CL']
        #
        for ind,scl in enumerate( data[skey]['CL'] ):
            #
            res[skey][scl] = {}
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-CL'+scl+'.txt'
            if not os.path.isfile( foname ):
                print('The file CL does not exist ',foname)
                continue
            print('The file does exists ',foname)
            cont_R, cont_M = np.loadtxt( foname )
            res[skey][scl]['rad'] = cont_R
            res[skey][scl]['mas'] = cont_M
        #
        if res[skey]['type'] == 'pdf' or res[skey]['type'] == 'mcmc':
            #
            res[skey]['pdf'] = {}
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_rad.txt'
            if not os.path.isfile( foname ):
                print('The file pdf_rad does not exist ',foname)
                continue
            rad = np.loadtxt( foname )
            res[skey]['pdf']['rad'] = rad
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_mass.txt'
            if not os.path.isfile( foname ):
                print('The file pdf_mass does not exist ',foname)
                continue
            mass = np.loadtxt( foname )
            res[skey]['pdf']['mass'] = mass
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_pdf.txt'
            if not os.path.isfile( foname ):
                print('The file pdf_pdf does not exist ',foname)
                continue
            pdf = np.loadtxt( foname )
            res[skey]['pdf']['pdf'] = pdf
    #
    return res
    #
    if env.verb: print('Exit create_res_qLMXB( )')


def show_res_qLMXB( res ):
    #
    if env.verb: print('Enter show_res_qLMXB( res )')
    #
    skeys = list( res.keys() )
    print('skeys:',skeys)
    #
    for skey in skeys:
        print('for key:',skey)
        print('   res[skey].keys()',list(res[skey].keys()))
        print('   name:',res[skey]['name'])
        print('   type:',res[skey]['type'])
        print('   color:',res[skey]['color'])
        print('   line:',res[skey]['line'])
        scls = res[skey]['CL']
        print('   CL:',scls)
        for scl in scls:
            print('      CL:',scl)
            # give mas and rad
        if 'pdf' in res[skey].keys():
            print('   Found pdf plot in res dictionary')
    #
    if env.verb: print('Exit show_res_qLMXB( res )')
    #


