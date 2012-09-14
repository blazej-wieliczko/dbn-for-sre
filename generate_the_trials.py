full_trial_filename = "/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists/test/short2-short3.ndx.csv"

# this file contains:
#model_id,test_id,channel,trial_status,is_1,is_2,is_3,is_4,is_5,is_6,is_7,is_8
#10017,fivsw,b,nontarget,N,N,N,Y,N,N,N,N
#10017,ftvgt,a,nontarget,N,N,N,Y,N,N,N,N
#10017,flkdw,b,target,N,N,N,Y,N,N,N,N
#10017,fntnt,a,nontarget,N,N,N,Y,N,N,N,N
#10017,fvrpn,b,nontarget,N,N,N,Y,N,N,N,N
#10017,fodvw,b,nontarget,N,N,N,Y,N,N,N,N
#10017,fuoix,b,nontarget,N,N,N,Y,N,N,N,N
#10017,foyyd,b,nontarget,N,N,N,Y,N,N,N,N
#10017,fhpti,a,target,Y,N,Y,N,N,N,N,N




train_filename = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists/trn/male_use_eng.trn'
#
#tahzx,B,41117
#twcid,B,26374
#txmgz,B,17492
#twauo,B,43041
#tahzk,B,21781
#tkrym,B,60953
#tjjrd,B,31662
#tgicd,B,70080
#tsjxf,A,76973
#tgyot,B,71158
#tafan,B,39418



import numpy as np

trial_data = np.genfromtxt(full_trial_filename, dtype=str, delimiter=' ', skip_header=0, autostrip=True)

train_models = set(np.genfromtxt(train_filename, dtype=str, delimiter=',', skip_header=0, autostrip=True)[:,2])


filtered_trials = []

for trial in trial_data:
    if trial[0] in train_models and trial[1] == 'm':
        segment_elements = trial[2].split(':')

        segment_id = 'SI8-' + segment_elements[0][:-4] +'_SI8-' + segment_elements[1]

        print trial[0], trial[1], segment_id
        filtered_trials.append(trial)


print len(filtered_trials)
print len(trial_data)






