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
    print(30*'#')
    runcmd('mkdir -p data', verbose = True)
    print(30*'#')
    #
    print(30*'#')
    print('From LIGO Document P1800115-v12')
    print('get EoS-insensitive_posterior_samples.dat (428.0 kB)')
    runcmd('wget -P data https://dcc.ligo.org/public/0152/P1800115/012/EoS-insensitive_posterior_samples.dat', verbose = True)
    runcmd('gzip data/EoS-insensitive_posterior_samples.dat.gz data/EoS-insensitive_posterior_samples.dat')
    runcmd('rm data/EoS-insensitive_posterior_samples.dat')
    print(30*'#')
    print()
    #
    print()
    print(30*'#')
    print('From LIGO Document P1800061-v11')
    print('get low_spin_PhenomPNRT_posterior_samples.dat.gz (423.1 kB)')
    runcmd("wget -P data https://dcc.ligo.org/public/0150/P1800061/011/low_spin_PhenomPNRT_posterior_samples.dat.gz", verbose = True)
    print('get high_spin_PhenomPNRT_posterior_samples.dat.gz (971.3 kB)')
    runcmd("wget -P data https://dcc.ligo.org/public/0150/P1800061/011/high_spin_PhenomPNRT_posterior_samples.dat.gz", verbose = True)
    print(30*'#')
    print()

    
if __name__ == "__main__":
    main()
