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
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    #if env.verb: print('   show dictionary data:')
    #if env.verb: print('   ',data)
    #
    # loop over skeys
    #
    for skey in skeys:
        if data[skey]['type'] == 'contour':
            #print('copy ',env.path_data_file,data[skey],'.txt')
            print(f'   copy {env.path_data_file+"/"+data[skey]["name"]+".txt"}')
            print(f'     to {env.path_data_out_file+"/"+data[skey]["name"]+".cont"}')
            os.system('cp '+env.path_data_file+'/'+data[skey]['name']+'.txt '+env.path_data_out_file+'/'+data[skey]['name']+'.cont')
        if data[skey]['type'] == 'pdf':
            print(f'   convert pdf into contour (to be done)')
    #
    if env.verb: print('Exit create_contours( skeys )')

