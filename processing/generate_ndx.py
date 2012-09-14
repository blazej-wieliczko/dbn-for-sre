# ndx needs lines like this:      SI8-fcxuk_SI8-A 12316


import numpy as np

models_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2.model.key'
segments_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/clean-filelists/NIST_SRE08_short2-short3.trial.is_8.key'


models = np.genfromtxt(models_file, dtype=str, delimiter=',', skip_header=0, autostrip=True)
segments = np.genfromtxt(segments_file, dtype=str, delimiter=',', skip_header=1, autostrip=True)


maleslist = [row[0] for row in models if row[1] == 'm']
males = set(maleslist)

print 'len(segments):', len(segments)

def getndx_line(row):
    return ''.join(['SI8-', row[1], '_SI8-',row[2].upper(), ' ', row[0]])


ndx_lines = [getndx_line(row) for row in segments if row[-1] == 'Y' and row[0] in males]


print 'len(malesegments)', len(ndx_lines)
print 'len(set(malesegments)', len(set(ndx_lines))


out = open('/Volumes/MacHD/Dropbox/Sheffield/project/sre-docs/clean-filelists/male-us-eng-test.ndx', 'w')

for row in ndx_lines:
    print row

print len(ndx_lines)



out.write('\n'.join(ndx_lines))

out.close()

















