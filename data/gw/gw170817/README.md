   Project to analyse Gravitational wave data. 

Short description of files in this repository:


BNS.py: Modification of sample code found in Bilby's documentation. All parameters except mass_1 and mass_2 are frozen at the mean values of Capano's posteriors.


BNS_EOS.py : Modification of BNS.py so that the sampler directly samples over the 2000 Equations of State contained in the folder Capano_Eos. This code uses the IMRPhenomPv2_NRTidal waveform in order to better account for tidal effects. 

Note 1: The Equations of state found in the folder 'Capano_Eos' can be downloded at: https://github.com/sugwg/gw170817-eft-eos

Note 2: The two codes 'BNS.py' and 'BNS_EOS.py' download GW170817 L1, V1 and H1 data (around 660 MB) automatically when run for the first time.

Results_BNS : Folder containing the results produced by the code 'BNS.py'

Results_Eos_IMRPhenomPv2_NRTidal : Folder containing results produced by the code 'BNS_EOS.py'.

Read_results.py : Code that reads the posterior distributions sotred in the result folders.
