import numpy as np

models_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2.model.key'
segments_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2-short3.trial.is_8.key'

models = np.genfromtxt(models_file, dtype=str, delimiter=',', skip_header=0, autostrip=True)
segments = np.genfromtxt(segments_file, dtype=str, delimiter=',', skip_header=1, autostrip=True)

maleslist = [row[0] for row in models if row[1] == 'm']
males = set(maleslist)

print 'len(segments):', len(segments)

lines = [','.join(row) for row in segments if row[-1] == 'Y' and row[0] in males]

out = open('/Volumes/MacHD/Dropbox/Sheffield/project/sre-docs/clean-filelists/short2-short3-labels', 'w')

for row in lines:
    out.write(row + '\n')

out.close()

















