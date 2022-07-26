import subprocess

def runcmd(cmd, verbose = False, *args, **kwargs):

    process = subprocess.Popen(
        cmd,
        stdout = subprocess.PIPE, 
        stderr = subprocess.PIPE,
        text = True, 
        shell = True
    )
    std_out, std_err = process.communicate()
    if verbose:
        print(std_out.strip(), std_err)
    pass

def main():
    #
    print()
    print('python3 get_data.py')
    print()
    #
    print()
    print('- Creates new folder: data')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data', verbose = True)
    print(30*'#')
    #
    # =================================================
    #
    # GW
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: data/gw')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/gw', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get GW170817 data and store in data/gw/gw170817')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/gw/gw170817', verbose = True)
    print(30*'#')
    #
    print(30*'#')
    print('From LIGO Document P1800115-v12')
    print('get EoS-insensitive_posterior_samples.dat (428.0 kB)')
    runcmd('wget -P ../data/gw/gw170817 https://dcc.ligo.org/public/0152/P1800115/012/EoS-insensitive_posterior_samples.dat', verbose = True)
    runcmd('gzip ../data/gw/gw170817/EoS-insensitive_posterior_samples.dat.gz ../data/gw/gw170817/EoS-insensitive_posterior_samples.dat')
    runcmd('rm ../data/gw/gw170817/EoS-insensitive_posterior_samples.dat')
    print(30*'#')
    print()
    #
    print()
    print(30*'#')
    print('From LIGO Document P1800061-v11')
    print('get low_spin_PhenomPNRT_posterior_samples.dat.gz (423.1 kB)')
    runcmd("wget -P ../data/gw/gw170817 https://dcc.ligo.org/public/0150/P1800061/011/low_spin_PhenomPNRT_posterior_samples.dat.gz", verbose = True)
    print('get high_spin_PhenomPNRT_posterior_samples.dat.gz (971.3 kB)')
    runcmd("wget -P ../data/gw/gw170817 https://dcc.ligo.org/public/0150/P1800061/011/high_spin_PhenomPNRT_posterior_samples.dat.gz", verbose = True)
    print(30*'#')
    print()
    #
    # =================================================
    #
    # MSPS
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: msps')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/msps', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get data (to be done)')
    print()
    #
    # =================================================
    #
    # BURSTS
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: bursts')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/bursts', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get data (to be done)')
    print()
    #
    # =================================================
    #
    # COOLING
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: cooling')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/cooling', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get data (to be done)')
    print()
    #
    # =================================================
    #
    # FASTEST
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: fastest')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/fastest', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get data (to be done)')
    print()
    #
    # =================================================
    #
    # MASSES
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: masses')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/masses', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get data (to be done)')
    print()
    #
    # =================================================
    #
    # QLMXB
    #
    # =================================================
    #
    print()
    print('  - Creates new folder: qlmxb')
    print()
    #
    print(30*'#')
    runcmd('mkdir -p ../data/qlmxb', verbose = True)
    print(30*'#')
    #
    print()
    print('    - Get data (to be done)')
    print()

    
if __name__ == "__main__":
    main()
