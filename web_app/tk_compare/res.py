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
        print('For key = ',skey,' type = ',data[skey]['type'])
        res[skey] = {}
        res[skey]['name']  = data[skey]['name']
        res[skey]['type']  = data[skey]['type']
        res[skey]['line']  = data[skey]['line']
        res[skey]['color'] = data[skey]['color']
        #
        if res[skey]['type'] == 'contour':
            #
            #res[skey]['CL_A'] = data[skey]['CL_A']
            res[skey]['CL_A'] = {}
            #
            for ind,scl in enumerate( data[skey]['CL_A'] ):
                #
                res[skey]['CL_A'][scl] = {}
                foname = env.path_data_out_file+'/'+data[skey]['name']+'-CL_A'+scl+'.txt'
                if not os.path.isfile( foname ):
                    print('   The file CL_A does not exist ',foname)
                    continue
                print('   The file CL_A does exists ',foname)
                cont_R, cont_M = np.loadtxt( foname )
                res[skey]['CL_A'][scl]['rad'] = cont_R
                res[skey]['CL_A'][scl]['mass'] = cont_M
            #
            #res[skey]['CL_C'] = data[skey]['CL_C']
            res[skey]['CL_C'] = {}
            #
            for ind,scl in enumerate( data[skey]['CL_C'] ):
                #
                res[skey]['CL_C'][scl] = {}
                foname = env.path_data_out_file+'/'+data[skey]['name']+'-CL_C'+scl+'.txt'
                if not os.path.isfile( foname ):
                    print('   The file CL_C does not exist ',foname)
                    continue
                print('   The file CL_C does exists ',foname)
                cont_R, cont_M = np.loadtxt( foname )
                res[skey]['CL_C'][scl]['rad'] = cont_R
                res[skey]['CL_C'][scl]['mass'] = cont_M
        #
        elif res[skey]['type'] == 'pdf' or res[skey]['type'] == 'mcmc':
            #
            res[skey]['pdf'] = {}
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_rad.txt'
            if not os.path.isfile( foname ):
                print('   The file pdf_rad does not exist ',foname)
                continue
            rad = np.loadtxt( foname )
            res[skey]['pdf']['rad'] = rad
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_mass.txt'
            if not os.path.isfile( foname ):
                print('   The file pdf_mass does not exist ',foname)
                continue
            mass = np.loadtxt( foname )
            res[skey]['pdf']['mass'] = mass
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_pdf.txt'
            if not os.path.isfile( foname ):
                print('   The file pdf_pdf does not exist ',foname)
                continue
            pdf = np.loadtxt( foname )
            res[skey]['pdf']['pdf'] = pdf
            #
            #res[skey]['CL_C'] = data[skey]['CL_C']
            res[skey]['CL_C'] = {}
            #
            for ind,scl in enumerate( data[skey]['CL_C'] ):
                #
                res[skey]['CL_C'][scl] = {}
                foname = env.path_data_out_file+'/'+data[skey]['name']+'-CL_C'+scl+'.txt'
                if not os.path.isfile( foname ):
                    print('   The file CL_C does not exist ',foname)
                    continue
                print('   The file CL_C does exists ',foname)
                cont_R, cont_M = np.loadtxt( foname )
                res[skey]['CL_C'][scl]['rad'] = cont_R
                res[skey]['CL_C'][scl]['mass'] = cont_M
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
        skey_keys = list(res[skey].keys())
        print('   res[skey].keys()',skey_keys)
        print('   name:',res[skey]['name'])
        print('   type:',res[skey]['type'])
        print('   color:',res[skey]['color'])
        print('   line:',res[skey]['line'])
        if 'CL_A' in skey_keys:
            scls = list( res[skey]['CL_A'].keys() )
            print('   CL_A:',scls)
            for scl in scls:
                print('      CL_A:',scl)
                # give mas and rad
                print('         rad:',res[skey]['CL_A'][scl]['rad'])
                print('         mass:',res[skey]['CL_A'][scl]['mass'])
        if 'pdf' in list( res[skey].keys() ):
            print('   Found pdf plot in res dictionary')
        if 'CL_C' in skey_keys:
            scls = list( res[skey]['CL_C'].keys() )
            print('   CL_C:',scls)
            for scl in scls:
                print('      CL_C:',scl)
                # check that 'rad' is non-zero:
                # give mas and rad
                if 'rad' in list(res[skey]['CL_C'][scl].keys()):
                    print('         rad:',res[skey]['CL_C'][scl]['rad'])
                    print('         mass:',res[skey]['CL_C'][scl]['mass'])
    #
    if env.verb: print('Exit show_res_qLMXB( res )')
    #


