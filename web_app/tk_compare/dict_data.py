import os
from tk_compare import env

col = [ 'k', 'b', 'g', 'r', 'c', 'm', 'y', 'orange', 'purple', 'brown', 'pink', 'olive' ]

def create_dict_data( ):
    #
    if env.verb: print('Enter create_dict_data( )')
    #
    # define the data
    #
    data = {}
    data['sources'] = {}
    data['skeys'] = {}
    data['qLMXB-1'] = {}
    # provide the name of the file
    data['qLMXB-1']['name'] = 'qLMXB_NGC2808-qLMXB_2007-massradius-hydrogen-1'
    # provide the type of data
    data['qLMXB-1']['type'] = 'contour'
    # if contour, provide the contour as given by the authors (A)
    data['qLMXB-1']['CL_A'] = ['90', '99']
    # repeat:
    data['qLMXB-2'] = {}
    data['qLMXB-2']['name'] = 'qLMXB_NGC5139-qLMXB_2014-massradius-hydrogen-1'
    data['qLMXB-2']['type'] = 'contour'
    data['qLMXB-2']['CL_A'] = ['68', '90', '99']
    data['qLMXB-3'] = {}
    data['qLMXB-3']['name'] = 'qLMXB_NGC6397-qLMXB_2014-massradius-helium-1'
    data['qLMXB-3']['type'] = 'contour'
    data['qLMXB-3']['CL_A'] = ['68', '90', '99']
    data['qLMXB-4'] = {}
    data['qLMXB-4']['name'] = 'qLMXB_NGC6397-qLMXB_2014-massradius-hydrogen-1'
    data['qLMXB-4']['type'] = 'contour'
    data['qLMXB-4']['CL_A'] = ['68', '90', '99']
    data['qLMXB-5'] = {}
    data['qLMXB-5']['name'] = 'qLMXB_47TucX5-qLMXB_2016-massradius-hydrogen-1'
    data['qLMXB-5']['type'] = 'contour'
    data['qLMXB-5']['CL_A'] = ['68', '95']
    data['qLMXB-6'] = {}
    data['qLMXB-6']['name'] = 'qLMXB_47TucX7-qLMXB_2016-massradius-helium-1'
    data['qLMXB-6']['type'] = 'contour'
    data['qLMXB-6']['CL_A'] = ['68', '95']
    data['qLMXB-7'] = {}
    data['qLMXB-7']['name'] = 'qLMXB_47TucX7-qLMXB_2016-massradius-hydrogen-1'
    data['qLMXB-7']['type'] = 'contour'
    data['qLMXB-7']['CL_A'] = ['68', '95']
    data['qLMXB-8'] = {}
    data['qLMXB-8']['name'] = 'qLMXB_NGC6304-qLMXB_2017-massradius-hydrogen-1'
    data['qLMXB-8']['type'] = 'contour'
    data['qLMXB-8']['CL_A'] = ['68', '95', '99']
    data['qLMXB-9'] = {}
    data['qLMXB-9']['name'] = 'qLMXB_M13-qLMXB_2018-massradius-helium-1'
    data['qLMXB-9']['type'] = 'pdf'
    data['qLMXB-10'] = {}
    data['qLMXB-10']['name'] = 'qLMXB_M13-qLMXB_2018-massradius-hydrogen-1'
    data['qLMXB-10']['type'] = 'pdf'
    data['qLMXB-11'] = {}
    data['qLMXB-11']['name'] = 'qLMXB_M30-qLMXB_2020-massradius-helium-1'
    data['qLMXB-11']['type'] = 'mcmc'
    data['qLMXB-12'] = {}
    data['qLMXB-12']['name'] = 'qLMXB_M30-qLMXB_2020-massradius-hydrogen-1'
    data['qLMXB-12']['type'] = 'mcmc'
    data['qLMXB-13'] = {}
    data['qLMXB-13']['name'] = 'qLMXB_M28-qLMXB_2022-massradius-helium-1'
    data['qLMXB-13']['type'] = 'contour'
    data['qLMXB-13']['CL_A'] = ['68', '90', '95']
    data['qLMXB-14'] = {}
    data['qLMXB-14']['name'] = 'qLMXB_M28-qLMXB_2022-massradius-hydrogen-1'
    data['qLMXB-14']['type'] = 'contour'
    data['qLMXB-14']['CL_A'] = ['68', '90', '95']
    data['Mass-1'] = {}
    data['Mass-1']['name'] = 'NS-Mass_PSRJ0740+6620_2020-mass-shapiro-1'
    data['Mass-2'] = {}
    data['Mass-2']['name'] = 'NS-Mass_PSRJ1614-2230_NANOgrav11yr-mass-shapiro-1'
    data['Mass-3'] = {}
    data['Mass-3']['name'] = 'NS-Mass_PSRJ1614-2230_NANOgrav15yr-mass-shapiro-2'
    data['Spin-1'] = {}
    data['Spin-1']['name'] = 'NS-Spin_PSRJ1748-2446ad_2005-spin-1'
    #
    # setup default options: 'color', 'line', 'CL_C'
    # also count the number of sources and give their list
    #
    skeys = list( data.keys() )
    print('skeys full:',skeys)
    skeys_qLMXB = []
    skeys_Mass = []
    skeys_Spin = []
    for skey in skeys:
        if 'qLMXB' in skey:
            skeys_qLMXB.append(skey)
        elif 'Mass' in skey:
            skeys_Mass.append(skey)
        elif 'Spin' in skey:
            skeys_Spin.append(skey)
    #skeys.remove('sources')
    #skeys.remove('skeys')
    data['skeys']['qLMXB'] = skeys_qLMXB
    data['skeys']['Mass'] = skeys_Mass
    data['skeys']['Spin'] = skeys_Spin
    print('skeys qLMXB:',data['skeys']['qLMXB'])
    print('skeys Mass:',data['skeys']['Mass'])
    print('skeys Spin:',data['skeys']['Spin'])
    # Treat qLMXB
    print('qLMXB:')
    source_qLMXB = set()
    lnames = []
    i=0
    for ind,skey in enumerate( data['skeys']['qLMXB'] ):
        print('   skey: ',skey)
        # give here the CL which will be constructed (C) by the code
        data[skey]['CL_C'] = ['68', '90', '95', '99']
        name_long  = data[skey]['name'].split('-')
        name_short = name_long[0].split('_')
        name_new = name_long[0]+'-'+name_long[1]
        if name_short[0] == 'qLMXB':
            source_qLMXB.add(name_short[1])
        if name_new not in lnames:
            lnames.append(name_new)
            color = col[i]
            i = i + 1
        data[skey]['color'] = color
        if 'hydrogen' in data[skey]['name']:
            data[skey]['line'] = 'dashed'
        elif 'helium' in data[skey]['name']:
            data[skey]['line'] = 'dotted'
        print('   ind:',ind,' i:',i-1,' name_new:',name_new,' source:',name_short[1],' color:',color,' line:',data[skey]['line'])
    print('   number of sources:',len(source_qLMXB))
    print('   source names:',source_qLMXB)
    data['sources']['qLMXB'] = source_qLMXB
    # Treat Mass
    print('Mass:')
    source_Mass = set()
    for ind,skey in enumerate( data['skeys']['Mass'] ):
        print('   skey: ',skey,' name:',data[skey]['name'])
        name  = data[skey]['name'].split('_')
        if name[0] == 'NS-Mass':
            source_Mass.add(name[1])
            color = col[ind]
        data[skey]['color'] = color
        data[skey]['line'] = 'solid'
        print('   ind:',ind,' name[0]:',name[0],' source:',name[1],' color:',color,' line:',data[skey]['line'])
    print('   number of sources:',len(source_Mass))
    print('   source names:',source_Mass)
    data['sources']['Mass'] = source_Mass
    # Treat Spin
    print('Spin:')
    source_Spin = set()
    for ind,skey in enumerate( data['skeys']['Spin'] ):
        print('   skey: ',skey)
        name  = data[skey]['name'].split('_')
        if name[0] == 'NS-Spin':
            source_Spin.add(name[1])
            color = col[ind]
        data[skey]['color'] = color
        data[skey]['line'] = 'solid'
        print('   ind:',ind,' name[0]:',name[0],' source:',name[1],' color:',color,' line:',data[skey]['line'])
    print('   number of sources:',len(source_Spin))
    print('   source names:',source_Spin)
    data['sources']['Spin'] = source_Spin
    #
    if env.verb: print('   show dictionary data:')
    if env.verb: print('   ',data)
    #
    print('-'*10)
    print('WRITE DICT INTO FILE:',env.dict_data)
    with open(env.dict_data, 'w') as f:
        print(data, file=f)
    #
    if env.verb: print('Exit create_dict_data( )')

