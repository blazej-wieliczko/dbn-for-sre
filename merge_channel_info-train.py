#!/usr/bin/env python

#prints speaker info with channel, filtered through the language requirement, based on the trn file (with channel info)
# and the segment.key file (which has the language information)

from numpy import *
import numpy as np

# np.loadtxt?
female_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists/trn/female/short2.trn.csv'
male_file = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists/trn/male/short2.trn.csv'

chan_f = np.genfromtxt(female_file,
    dtype=str, delimiter=',', skip_header=0, autostrip=True)
chan_m = np.genfromtxt(male_file,
    dtype=str, delimiter=',', skip_header=0, autostrip=True)


use_female = False
if use_female:
    both_chan = vstack((chan_m, chan_f))
else: both_chan = chan_m

from collections import defaultdict

both_chan_dict = defaultdict(dict)

channel_id = 2
segment_id = 1
model_id = 0

lang_header = 'lang'
maintype_header = 'maintype'
native_lang_header = 'native_lang'
native_lang2_header = 'native_lang2'
conv_type_header = 'conv_type'

# segmentid -> channel_id -> model
#           -> conv_type




for row in both_chan:
    both_chan_dict[row[segment_id]][row[channel_id]] = row[0]
for row in both_chan:
    both_chan_dict[row[segment_id]][row[channel_id]] = row[model_id]


train_data = np.genfromtxt('/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists/short2.train.segment.key-all-trainin-examples.csv',
    dtype=str, delimiter=',', skip_header=1, autostrip=True)

for i, row in enumerate(train_data):
        segid = row[0]
        conv_type = row[3]
        lang = row[4]
        maintype = row[6]
        native_lang = row[7]
        native_lang2 = row[10]
        segment_data = both_chan_dict[segid]
        segment_data[conv_type_header] =    conv_type
        segment_data[lang_header] =         lang
        segment_data[maintype_header] =     maintype
        segment_data[native_lang_header] =  native_lang
        segment_data[native_lang2_header] = native_lang2

us_eng_phone_only = []

for seg_id in both_chan_dict:
    data = both_chan_dict[seg_id]
    if data[conv_type_header] == 'phonecall' and data[lang_header] == 'ENG':

        if data.has_key('A') and data[native_lang_header] == 'USE':
#                                       segment chan  model_id
            us_eng_phone_only.append( [ seg_id, 'A', data['A'] ])
        if data.has_key('B') and data[native_lang2_header] == 'USE':
        #                               segment chan  model_id
            us_eng_phone_only.append( [ seg_id, 'B', data['B'] ])


from pprint import pprint
pprint (sorted(us_eng_phone_only, key = lambda x: x[2]))
print len(us_eng_phone_only)

#/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists/trn/male/short2.trn.csv
#
#
#
#a - baba b - facet
#
#10072,tgtxj,B
#11458,tgwfw,B
#


#def ffunc(x):
#    return x[3] == 'phonecall' and x[4] == 'ENG' and
#
#filt = filter(ffunc, train_data)


