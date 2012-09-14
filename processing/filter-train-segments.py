# output file format
#SI8-taavg_SI8-A-M-11367
#SI8-tadis_SI8-B-M-32757
#SI8-tadtr_SI8-B-M-20161

import numpy as np

models_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2.model.key'
trials_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2-short3.trial.is_8.key'

models = np.genfromtxt(models_file, dtype=str, delimiter=',', skip_header=1, autostrip=True)
trials = np.genfromtxt(trials_file, dtype=str, delimiter=',', skip_header=1, autostrip=True)

trial_males_list = [row[0] for row in trials]
males = set( trial_males_list )

print 'len(segments):', len(trials)

lines = [','.join(row) for row in trials if row[-1] == 'Y' and row[0] in males]

lines = [row for row in models if row[1] == 'm' and row[0] in trial_males_list]

#out = open('/Volumes/MacHD/Dropbox/Sheffield/project/sre-docs/clean-filelists/short2-short3-labels', 'w')
#
#for row in lines:
#    out.write(row + '\n')


for row in lines:
    segment, channel = row[2].split(':')
    print 'SI8-%s_SI8-%s-M-%s' % (segment, channel.upper(), row[0])




#print trial_males_list

#out.close()

















