inputfile = '/Volumes/MacHD/Dropbox/Sheffield/project/flists/train-validate-labels.ndx'

labels_suffix = ',N,N,N,N,N,Y,Y,Y'


#98107,tmamgTE,b,N,N,N,N,N,Y,Y,Y



class TestFile:
    def __init__(self, line):
        model, segment = line.split(' ')
        self.model = model
        self.segmentid = segment[:-9]




def load_input(inputfile):
    return [TestFile(line) for line in (open(inputfile))]



testfiles = load_input(inputfile)
models = sorted(set([testfile.model for testfile in testfiles]))


testfiles_dict = dict((testfile.model, testfile) for testfile in testfiles)


impostor_trials_per_model = 10


import random


trial_file = open('/Volumes/MacHD/Dropbox/Sheffield/project/flists/cv-trials.ndx', 'w')
labels_file = open('/Volumes/MacHD/Dropbox/Sheffield/project/flists/cv-trial-labels.ndx', 'w')


def stripped_segment(model_segment_id):
    split = model_segment_id.split('-')
    return ','.join([split[1][:-4], split[-1].lower()])


for target_model_id in models[:199]:
    trials = random.sample(models[199:], impostor_trials_per_model)

    trial_file_lines = []
    labels_file_lines = []

    #98107,tmamgTE,b,    nontarget  N,N,N,N,C,Y

    for impostor_model_id in trials:
        if impostor_model_id != target_model_id:
            impostor_segment_id = testfiles_dict[impostor_model_id].segmentid
            trial_file_lines.append(' '.join([impostor_segment_id +'-M-' + impostor_model_id, target_model_id]))
            labels_file_lines.append(','.join([target_model_id, stripped_segment(impostor_segment_id)]) + ',nontarget' + labels_suffix)

    model_segment_id = testfiles_dict[target_model_id].segmentid
    trial_file_lines.append(' '.join([model_segment_id +'-M-' + target_model_id, target_model_id]))
    labels_file_lines.append(','.join([target_model_id, stripped_segment(model_segment_id)]) + ',target' + labels_suffix)

    trial_file.write('\n'.join(trial_file_lines))
    trial_file.write('\n')
    labels_file.write('\n'.join(labels_file_lines))
    labels_file.write('\n')


trial_file.close()
labels_file.close()


print 'finished'







