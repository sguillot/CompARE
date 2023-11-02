import os
from tk_compare import env

def create_dict_key( ):
    #
    if env.verb: print('Enter create_dict_key( )')
    #
    # define the key
    #
    key = {}
    key['qLMXB-1'] = {}
    key['qLMXB-1']['name'] = 'qLMXB_NGC2808-qLMXB_2007-massradius-hydrogen-1'
    key['qLMXB-1']['type'] = 'contour'
    key['qLMXB-1']['line'] = 'dashed'
    key['qLMXB-2'] = {}
    key['qLMXB-2']['name'] = 'qLMXB_NGC5139-qLMXB_2014-massradius-hydrogen-1'
    key['qLMXB-2']['type'] = 'contour'
    key['qLMXB-2']['line'] = 'dashed'
    key['qLMXB-3'] = {}
    key['qLMXB-3']['name'] = 'qLMXB_NGC6397-qLMXB_2014-massradius-helium-1'
    key['qLMXB-3']['type'] = 'contour'
    key['qLMXB-3']['line'] = 'dotted'
    key['qLMXB-4'] = {}
    key['qLMXB-4']['name'] = 'qLMXB_NGC6397-qLMXB_2014-massradius-hydrogen-1'
    key['qLMXB-4']['type'] = 'contour'
    key['qLMXB-4']['line'] = 'dashed'
    key['qLMXB-5'] = {}
    key['qLMXB-5']['name'] = 'qLMXB_47TucX5-qLMXB_2016-massradius-hydrogen-1'
    key['qLMXB-5']['type'] = 'contour'
    key['qLMXB-5']['line'] = 'dashed'
    key['qLMXB-6'] = {}
    key['qLMXB-6']['name'] = 'qLMXB_47TucX7-qLMXB_2016-massradius-helium-1'
    key['qLMXB-6']['type'] = 'contour'
    key['qLMXB-6']['line'] = 'dotted'
    key['qLMXB-7'] = {}
    key['qLMXB-7']['name'] = 'qLMXB_47TucX7-qLMXB_2016-massradius-hydrogen-1'
    key['qLMXB-7']['type'] = 'contour'
    key['qLMXB-7']['line'] = 'dashed'
    key['qLMXB-8'] = {}
    key['qLMXB-8']['name'] = 'qLMXB_NGC6304-qLMXB_2017-massradius-hydrogen-1'
    key['qLMXB-8']['type'] = 'contour'
    key['qLMXB-8']['line'] = 'dashed'
    key['qLMXB-9'] = {}
    key['qLMXB-9']['name'] = 'qLMXB_M13-qLMXB_2018-massradius-helium-1'
    key['qLMXB-9']['type'] = 'pdf'
    key['qLMXB-9']['line'] = 'dotted'
    key['qLMXB-10'] = {}
    key['qLMXB-10']['name'] = 'qLMXB_M13-qLMXB_2018-massradius-hydrogen-1'
    key['qLMXB-10']['type'] = 'pdf'
    key['qLMXB-10']['line'] = 'dashed'
    key['qLMXB-11'] = {}
    key['qLMXB-11']['name'] = 'qLMXB_M30-qLMXB_2020-massradius-helium-1'
    key['qLMXB-11']['type'] = 'contour'
    key['qLMXB-11']['line'] = 'dotted'
    key['qLMXB-12'] = {}
    key['qLMXB-12']['name'] = 'qLMXB_M30-qLMXB_2020-massradius-hydrogen-1'
    key['qLMXB-12']['type'] = 'contour'
    key['qLMXB-12']['line'] = 'dashed'
    key['qLMXB-13'] = {}
    key['qLMXB-13']['name'] = 'qLMXB_M28-qLMXB_2022-massradius-helium-1'
    key['qLMXB-13']['type'] = 'contour'
    key['qLMXB-13']['line'] = 'dotted'
    key['qLMXB-14'] = {}
    key['qLMXB-14']['name'] = 'qLMXB_M28-qLMXB_2022-massradius-hydrogen-1'
    key['qLMXB-14']['type'] = 'contour'
    key['qLMXB-14']['line'] = 'dashed'
    #
    if env.verb: print('   show dictionary key:')
    if env.verb: print('   ',key)
    #
    print('-'*10)
    print('WRITE DICT INTO FILE:',env.dict_key)
    with open(env.dict_key, 'w') as f:
        print(key, file=f)
    #
    if env.verb: print('Exit create_dict_key( )')

