# %%
# %%
from mcnptools import Mctal, MctalTally

# %%
import pandas as pd
import numpy as np
import tqdm
import pickle
import os
import json

# %%
sims_df = pd.read_csv('../sims.csv')

mctal_folder = '../compute/output/mctal/'
mctal_files = mctal_folder+sims_df['label']+'.mctal'

# Remove entries from sims_df where the corresponding mctal file does not exist
existing_mask = [os.path.exists(f) for f in mctal_files]
sims_df = sims_df[existing_mask].reset_index(drop=True)
mctal_files = mctal_folder + sims_df['label'] + '.mctal'


specs_folder = '../Spectrums/'

# %%
def readMCTAL(file, tally):

    m = Mctal(file)
    tfc = MctalTally.TFC
    # print(tfc)
    t = m.GetTally(tally)

    t_f_bins = t.GetFBins()
    t_d_bins = t.GetDBins()
    t_u_bins = t.GetUBins()
    t_s_bins = t.GetSBins()
    t_m_bins = t.GetMBins()
    t_c_bins = t.GetCBins()
    t_e_bins = t.GetEBins()
    t_t_bins = t.GetTBins()

    bins = [t_f_bins, t_d_bins, t_u_bins, t_s_bins, t_m_bins, t_c_bins, t_e_bins, t_t_bins]
    shape = (len(t_f_bins), len(t_d_bins), len(t_u_bins), len(t_s_bins), len(t_m_bins), len(t_c_bins), len(t_e_bins), len(t_t_bins))
    # print(shape)
    array = np.zeros(shape)
    for i in range(len(t_f_bins)):
        for j in range(len(t_d_bins)):
            for k in range(len(t_u_bins)):
                for l in range(len(t_s_bins)):
                    for m in range(len(t_m_bins)):
                        for n in range(len(t_c_bins)):
                            for o in range(len(t_e_bins)):
                                for p in range(len(t_t_bins)):
                                    array[i,j,k,l,m,n,o,p] = t.GetValue(i,j,k,l,m,n,o,p)
    # #                        f    d    u    s    m    c   e   t
    return bins, array


tally_bins = []
tally_arrays = {}
tallies = ['8', '18', '28']

for tally in tallies:
    tally_arrays[tally] = []

inc_tally_arrays = []
# %%
for i in tqdm.tqdm(
    range(len(sims_df)), 
    desc="Processing simulations"):
    sim_label = sims_df['label'][i]
    # check if pkl file exists
    pkl_file = specs_folder + sim_label + '.pkl'
    # if os.path.exists(pkl_file):
    #     print(f"Skipping {sim_label}, already processed.")
    #     continue
    
    _tals = []
    for tally in tqdm.tqdm(tallies, desc="Processing tallies", leave=False):
        # print(mctal_files[i])
        i_bins, i_array = readMCTAL(mctal_files[i], int(tally))
        tally_bins.append(i_bins)
        # print(i_array.shape)
        tally_arrays[tally].append(i_array.flatten())

print(np.array(tally_arrays['18']).shape)
DetRead = pd.DataFrame(np.array(tally_arrays['18'])).T
DetRead.columns = sims_df['label']
DetRead.index = i_bins[-2]
DetRead.to_csv('../DetectorReadings.csv')

IncRead = pd.DataFrame(np.array(tally_arrays['28'])).T
IncRead.columns = sims_df['label']
IncRead.index = i_bins[-2]
IncRead.to_csv('../IncidentSpectrums.csv')
