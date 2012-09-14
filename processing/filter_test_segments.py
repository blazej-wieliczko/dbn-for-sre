import numpy as np

segments_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2-short3.trial.is_8.key'
models_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2.model.key'


models = np.genfromtxt(models_file, dtype=str, delimiter=',', skip_header=0, autostrip=True)
segments = np.genfromtxt(segments_file, dtype=str, delimiter=',', skip_header=1, autostrip=True)


maleslist = [row[0] for row in models if row[1] == 'm']
males = set(maleslist)

print 'len(segments):', len(segments)
malesegments = [row[1] + ',' + row[2] for row in segments if row[-1] == 'Y' and row[0] in males]


print 'len(malesegments)', len(malesegments)
print 'len(set(malesegments)', len(set(malesegments))


out = open('/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/test-file-list', 'w')



for row in set(set(malesegments)):
    out.write(row)
    out.write('\n')

out.close()















