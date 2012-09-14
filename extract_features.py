import numpy as np

file_list = '/share/spandh.ami4/sid/dev/sre2008/exp/tel-us/test-short3-use-eng-phonecall.csv'
input_directory = '/share/spandh.ami4/sid/dev/sre2008/audio/test.short3/'

output_directory = '/share/spandh.ami4/sid/dev/sre2008/data/mfc/short3.test/'

#data = [[]]
data = np.genfromtxt(file_list,
    dtype=str, delimiter=',', skip_header=0, autostrip=True)


import commands
command_prefix = "/share/spandh.ami4/sw/spl/spro/bin/sfbcep -F sphere -l 20 -d 10 -w Hamming -p 19 -e -D -k 0 -i 300 -u 3400 "
#$COMMAND $INPUTDIR/tgaar.sph tgaar.mfc

def build_output_filename(f):
    return f + '.mfc'

channels = {'A': '1', 'B': '2'}

def build_cmd(row):
    file, channel, speaker = row
    # SI8-filename(paddedto6)_SI8-M/F-SPEAKERID.mfcc
    output_filename = output_directory + """SI8-%(file)s_SI8-%(channel)s.mfcc""" % locals()
    return command_prefix + '-x ' + channels[channel] + ' ' + input_directory + 'SI8-' + file + '.sph ' + output_filename

import os
job_id = int(os.environ['SGE_TASK_ID']) - 1
#print 'Job ', chunk_start

subtasks = range(1,24)

for subtask in subtasks:
    item_id = job_id * len(subtasks) + subtask - 1
    print 'job:', job_id, 'subtask: ', item_id
    row = data[item_id]
    cmd = build_cmd(row)
    #print 'Executing command', cmd
    try:
        exitstatus, outtext = commands.getstatusoutput(cmd)
        if exitstatus:
            print outtext
    except Exception as e:
        print e

#23*113

