import os
import numpy as np
from tk_compare import env
from scipy import optimize
import matplotlib.pyplot as plt

def fcl(x, apdf, max_pdf, xcl):
    return apdf[apdf>x*max_pdf].sum()-xcl*apdf.sum()

def create_files_qLMXB_contours_A( ):
    #
    if env.verb: print('Enter create_files_qLMXB_contours_A( )')
    #
    # read the dictionary
    #
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    # loop over skeys
    #
    for skey in data['skeys']['qLMXB']:
        #
        print('For key = ',skey,' type = ',data[skey]['type'])
        fname = env.path_data_file+'/'+data[skey]['name']+'.txt'
        foname = env.path_data_out_file+'/'+data[skey]['name']
        print('fname:',fname)
        #
        if data[skey]['type'] == 'contour':
        #
            print('   copy contours CL_A into files')
            ncl = len( data[skey]['CL_A'] )
            if ncl == 1:
                #
                r1, m1 = np.loadtxt( fname, unpack=True, comments='#' )
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)];
                m1 = m1[~np.isnan(m1)];
                #
                if r1[0] != r1[-1] and m1[0] != m1[-1]:
                    r1 = np.append(r1, r1[0]); m1 = np.append(m1, m1[0])
                #
                data1 = np.array( [r1, m1], dtype = np.float)
                #
            elif ncl == 2:
                #
                r1, m1, r2, m2 = np.loadtxt( fname, unpack=True, comments='#' )
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)]; r2 = r2[~np.isnan(r2)]
                m1 = m1[~np.isnan(m1)]; m2 = m2[~np.isnan(m2)]
                #
                if r1[0] != r1[-1] and m1[0] != m1[-1]:
                    r1 = np.append(r1, r1[0]); m1 = np.append(m1, m1[0])
                if r2[0] != r2[-1] and m2[0] != m2[-1]:
                    r2 = np.append(r2, r2[0]); m2 = np.append(m2, m2[0])
                #
                data1 = np.array( [r1, m1], dtype = np.float)
                data2 = np.array( [r2, m2], dtype = np.float)
                #
            elif ncl ==3:
                #
                r1, m1, r2, m2, r3, m3 = np.loadtxt( fname, unpack=True, comments='#')
                # Remove NaN from file
                r1 = r1[~np.isnan(r1)]; r2 = r2[~np.isnan(r2)]; r3 = r3[~np.isnan(r3)]
                m1 = m1[~np.isnan(m1)]; m2 = m2[~np.isnan(m2)]; m3 = m3[~np.isnan(m3)]
                #
                if r1[0] != r1[-1] and m1[0] != m1[-1]:
                    r1 = np.append(r1, r1[0]); m1 = np.append(m1, m1[0])
                if r2[0] != r2[-1] and m2[0] != m2[-1]:
                    r2 = np.append(r2, r2[0]); m2 = np.append(m2, m2[0])
                if r3[0] != r3[-1] and m3[0] != m3[-1]:
                    r3 = np.append(r3, r3[0]); m3 = np.append(m3, m3[0])
                #
                data1 = np.array( [r1, m1], dtype = np.float)
                data2 = np.array( [r2, m2], dtype = np.float)
                data3 = np.array( [r3, m3], dtype = np.float)
                #
            #
            for ind,scl in enumerate(data[skey]['CL_A']):
                print('   save data in ',data[skey]['name']+'-CL_A'+scl+'.txt')
                if ind == 0:
                    np.savetxt( foname+'-CLA'+scl+'.txt', data1, header='CL_A '+scl )
                elif ind == 1:
                    np.savetxt( foname+'-CLA'+scl+'.txt', data2, header='CL_A '+scl )
                elif ind == 2:
                    np.savetxt( foname+'-CLA'+scl+'.txt', data3, header='CL_A '+scl )
        #
        elif data[skey]['type'] == 'pdf':
        #
            print('   no contour given by author')
        #
        elif data[skey]['type'] == 'mcmc':
        #
            print('   no contour given by author')
        #
        else:
        #
            print('input type not understood')
            print('for key=',skey)
            exit()
    #
    if env.verb: print('Exit create_files_qLMXB_contours_A( )')

def create_files_qLMXB_pdf( ):
    #
    if env.verb: print('Enter create_files_qLMXB_pdf( )')
    #
    # read the dictionary
    #
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    # loop over skeys
    #
    for skey in data['skeys']['qLMXB']:
        #
        print('   For key = ',skey,' type = ',data[skey]['type'])
        fname = env.path_data_file+'/'+data[skey]['name']+'.txt'
        foname = env.path_data_out_file+'/'+data[skey]['name']
        print('   fname:',fname)
        #
        if data[skey]['type'] == 'contour':
        #
            print('      create pdf from contours (to be done)')
        #
        elif data[skey]['type'] == 'pdf':
        #
            print('      convert pdf into pdf')
            rad, mass, pdf = np.loadtxt( fname, unpack=True, comments='#')
            rad2=list(set(rad)); mass2=list(set(mass))
            rad2.sort(); mass2.sort();
            print('      rad2:',rad2 )
            rad = np.array( rad2 )
            mass = np.array( mass2 )
            print('      rad:',rad)
            print('      mass:',mass)
            apdf = np.array(pdf).reshape( rad.size, mass.size )
            #data[skey]['pdf'] = {}
            #data[skey]['pdf']['rad'] = rad
            #data[skey]['pdf']['mass'] = mass
            #data[skey]['pdf']['pdf'] = apdf
            np.savetxt( foname+'-pdf_rad.txt', rad, header='pdf rad' )
            np.savetxt( foname+'-pdf_mass.txt', mass, header='pdf mass' )
            np.savetxt( foname+'-pdf_pdf.txt', apdf, header='pdf pdf' )
        #
        elif data[skey]['type'] == 'mcmc':
        #
            print('      convert mcmc into pdf')
            rad, mass = np.loadtxt( fname, unpack=True, comments='#')
            pdf, rad, mass = np.histogram2d( rad, mass, bins=100, density = False )
            #pdf, rad, mass = np.histogram2d( rad, mass, bins=100, density = True )
            rad = rad[0:-1]
            mass = mass[0:-1]
            pdf = pdf.T
            #print('  rad:',rad,rad.size)
            #print('  mass:',mass,mass.size)
            #print('  pdf.size:',pdf.size,30*30)
            #data[skey]['pdf'] = {}
            #data[skey]['pdf']['rad'] = rad
            #data[skey]['pdf']['mass'] = mass
            #data[skey]['pdf']['pdf'] = apdf
            np.savetxt( foname+'-pdf_rad.txt', rad, header='pdf rad' )
            np.savetxt( foname+'-pdf_mass.txt', mass, header='pdf mass' )
            np.savetxt( foname+'-pdf_pdf.txt', pdf, header='pdf pdf' )
        #
        else:
        #
            print('input type not understood')
            print('for key=',skey)
            exit()
    #
    if env.verb: print('Exit create_files_qLMXB_pdf( )')
    #


def create_files_qLMXB_contours_C( ):
    #
    if env.verb: print('Enter create_files_qLMXB_contours_C( )')
    #
    # read the dictionary
    #
    with open(env.dict_data, 'r') as f:
        data = eval(f.read())
    #
    # loop over skeys
    #
    for skey in data['skeys']['qLMXB']:
        #
        print('For key = ',skey,' type = ',data[skey]['type'])
        fname = env.path_data_file+'/'+data[skey]['name']+'.txt'
        foname = env.path_data_out_file+'/'+data[skey]['name']
        print('fname:',fname)
        #
        if data[skey]['type'] == 'contour':
        #
            print('      create contours from pdf (to be done)')
        #
        elif data[skey]['type'] == 'pdf' or data[skey]['type'] == 'mcmc':
        #
            print('      convert pdf into contours')
            #
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_rad.txt'
            if not os.path.isfile( foname ):
                print('The file pdf_rad does not exist ',foname)
                continue
            rad = np.loadtxt( foname )
            #
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_mass.txt'
            if not os.path.isfile( foname ):
                print('The file pdf_mass does not exist ',foname)
                continue
            mass = np.loadtxt( foname )
            #
            foname = env.path_data_out_file+'/'+data[skey]['name']+'-pdf_pdf.txt'
            if not os.path.isfile( foname ):
                print('The file pdf_pdf does not exist ',foname)
                continue
            pdf = np.loadtxt( foname )
            max_pdf = np.max( pdf )
            print('   max_pdf:',max_pdf)
            #
            for scl in data[skey]['CL_C']:
                print('      CL_C:',scl)
                icl = int( scl )
                xcl = float( icl/100.0 )
                sol = optimize.root_scalar(fcl, args=(pdf,max_pdf,xcl), x0=1.0-xcl, x1=min(1.0,1.3-xcl), rtol=0.01, maxiter=100)
                xlev = sol.root
                print('      xlev:',xlev)
                cs = plt.contour(rad, mass, pdf, levels=[xlev*max_pdf])
                p = cs.collections[0].get_paths()[0]
                v = p.vertices
                x = v[:,0]
                y = v[:,1]
                contour = np.array( [x, y], dtype = np.float)
                np.savetxt( foname+'-CLC'+scl+'.txt', contour, header='CL_C '+scl )
        #
        else:
        #
            print('input type not understood')
            print('for key=',skey)
            exit()
    #
    if env.verb: print('Exit create_files_qLMXB_contours_C( )')
    #

