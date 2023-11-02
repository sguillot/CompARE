import os
from tk_compare import env

def create_contours( skeys ):
    #
    if env.verb: print('Enter create_contours( skeys )')
    #
    # read the key dictionary
    #
    #print('-'*10)
    #print('READ DICT FROM FILE:')
    with open(env.dict_key, 'r') as f:
        key = eval(f.read())
    #
    #if env.verb: print('   show dictionary key:')
    #if env.verb: print('   ',key)
    #
    # loop over skeys
    #
    for skey in skeys:
        if key[skey]['type'] == 'contour':
            #print('copy ',env.path_data_file,key[skey],'.txt')
            print(f'   copy {env.path_data_file+"/"+key[skey]["name"]+".txt"}')
            print(f'     to {env.path_data_out_file+"/"+key[skey]["name"]+".cont"}')
            os.system('cp '+env.path_data_file+'/'+key[skey]['name']+'.txt '+env.path_data_out_file+'/'+key[skey]['name']+'.cont')
        if key[skey]['type'] == 'pdf':
            print(f'   convert pdf into contour (to be done)')
    #
    if env.verb: print('Exit create_contours( skeys )')

