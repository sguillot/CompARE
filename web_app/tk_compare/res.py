import os
from tk_compare import env
import numpy as np

def show_res( res ):
    #
    if env.verb: print('Enter show_res( res )')
    #
    skeys = res.keys()
    print('skeys:',skeys)
    #
    for skey in skeys:
        print('for key:',skey)
        print('   res[skey].keys()',res[skey].keys())
        print('   name:',res[skey]['name'])
        print('   type:',res[skey]['type'])
        print('   color:',res[skey]['color'])
        print('   line:',res[skey]['line'])
        scls = res[skey]['CL']
        print('   CL:',scls)
        for scl in scls:
            print('CL:',scl)
            # give mas and rad
    #
    if env.verb: print('Exit show_res( res )')
    #

