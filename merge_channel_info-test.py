#!/usr/bin/env python

#prints speaker info with channel for the test set, filtered through the language requirement, based on the trn file (with channel info)
# and the segment.key file (which has the language information)

import numpy as np


input_dir = '/Volumes/Mac HD/Dropbox/Sheffield/project/sre-docs/derived_data_info-and_filelists'
#train_data_raw = np.genfromtxt(input_dir + '/test/NIST_SRE08_short3.test.segment.key.csv',
#    dtype=str, delimiter=',', skip_header=0, autostrip=True, invalid_raise=False)


import csv


train_data_raw = csv.reader(open(input_dir + '/test/NIST_SRE08_short3.test.segment.key.csv'))
speaker_data =   csv.reader(open(input_dir + '/test/NIST_SRE08_speaker.tbl'))

speaker_data = dict([[row[0], row]   for row in speaker_data])

us_eng_phone_only = []

lengths = []
rejects = 0
for row in train_data_raw:
    lengths.append(len(row))
    segid = row[0]
    conv_type = row[3]
    lang = row[4]
    speaker_id1 = row[5]
    maintype = row[6]
    native_lang = row[7]
    speaker_id2 = row[8] if len(row) > 8 else ''
    native_lang2 = row[10] if len(row) > 10 else ''

    if lang == 'ENG' and conv_type == 'phonecall':
        if native_lang == 'USE':
            us_eng_phone_only.append([segid, 'A', speaker_id1])
        else:
            rejects+=1
        if native_lang2 == 'USE':
            us_eng_phone_only.append([segid, 'B', speaker_id2])
        else:
            rejects+=1
    else:
        rejects+=1


from pprint import pprint
#pprint (sorted(us_eng_phone_only, key = lambda x: x[2]))
pprint (us_eng_phone_only)
print len(us_eng_phone_only)

print rejects



