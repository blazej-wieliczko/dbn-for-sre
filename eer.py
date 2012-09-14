#!/usr/bin/env python

# false alarm = false positive
# miss     =  false negative

# the labels file format: 10171,fbrfk,a,nontarget,N,N,N,N,N,Y,Y,Y
## the scores file format:   M 24831 0 SI8-fqbdi_SI8-B -0.0750835

from optparse import OptionParser
#from matplotlib.pyplot import plot

parser = OptionParser()
parser.add_option("--scores", dest="scores_file", default='/Volumes/MacHD/Dropbox/Sheffield/project/sre-docs/clean-filelists/scores/scores.res')
parser.add_option("--labels", dest="labels_file", default='/Volumes/MacHD/Dropbox/Sheffield/project/sre-docs/clean-filelists/short2-short3-labels.csv')

(options, args) = parser.parse_args()

import numpy as np

#def detection_cost(p_miss_target, p_falsealarm_non_target):
#    return 1             * p_miss_target           * 0.1 + \
#           1             * p_falsealarm_non_target * 0.99

model_index = 1
seg_index = 3
is_target_index = 2
score_index = 4
#side_index = 6

labels_filename = options.labels_file
scores_filename = options.scores_file
scores_file = open(scores_filename)
labels_file = open(labels_filename)
indexed_scores = {}

def strip_segment_affixes(segment):
    segment_stripped = segment.strip()
    return segment_stripped.split('-')[1].split('_')[0] + '_' + segment_stripped.split('-')[2].lower()


def get_model_segment_key(model_id, segment_id, sep = '', channel = ''):
    return model_id + segment_id + sep + channel


def read_scores():
    just_scores = []
    for line in scores_file:
        split = line.split(" ")
        score_val = float(split[score_index])
        segment_id = strip_segment_affixes(split[seg_index])
        just_scores.append(score_val)
        indexed_scores[get_model_segment_key(split[model_index], segment_id)] = score_val

    return just_scores

just_scores = read_scores()

maxscore = max(just_scores)
minscore = min(just_scores)

scores_file.close()

def calc_miss_prob(threshold, scores, labels):
    """
    returns (miss_rate, false_alarm_rate) for given threshold
    labels is a boolean list
    """
    miss_count = 0
    false_alarm_count = 0
    n_target_trials = 0.0
    n_impostor_trials = .0


    for key in scores:
        score = scores[key]
        isTarget = labels[key]
        assert score is not None and isTarget is not None

        if score < threshold and isTarget:
            miss_count += 1
        elif score > threshold and not isTarget:
            false_alarm_count += 1
        if isTarget:
            n_target_trials += 1
        else: n_impostor_trials += 1

    return float(miss_count) / n_target_trials, float(false_alarm_count)/n_impostor_trials

labels = []
indexed_labels = {}
for line in labels_file:
    split = line.split(",")
    label = split[3].strip()
    isTarget = label == 'target'
    labels.append(isTarget)
    if label != 'target' and label != 'nontarget':
        print "some labels aren't labels target or nontarget"
    model_id = split[0].strip()
    segment_id = split[1].strip()
    channel = split[2]
    indexed_labels[get_model_segment_key(model_id, segment_id, '_', channel)] = isTarget


assert len(just_scores) <= len(labels)

n_thresholds = 1000.0
thresholds =  [minscore + t * (maxscore-minscore)/ n_thresholds for t in range(0,int(n_thresholds))]

miss_rates = []
false_alarm_rates = []

# calculate the miss and false_alarm rates for different thresholds
for t in thresholds:
    (miss_rate, false_alarm_rate) = calc_miss_prob(t, indexed_scores, indexed_labels)
    miss_rates.append(miss_rate)
    false_alarm_rates.append(false_alarm_rate)

# finds the smallest diff between miss and fa rates.
miss_rates = np.array(miss_rates)
false_alarm_rates = np.array(false_alarm_rates)
closest_rate_index = np.argmin(abs(miss_rates - false_alarm_rates))

#plot(false_alarm_rates, miss_rates)

print 'Equal Error Rate; Miss rate:', miss_rates[closest_rate_index], 'False alarm rate:', false_alarm_rates[closest_rate_index]
print 'closest_rate_index:', closest_rate_index
print 'total thresholds tried:', len(miss_rates)
print 'with best threshold:', thresholds[closest_rate_index]
print 'min,max score:', minscore, maxscore
