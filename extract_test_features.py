import os
import numpy as np

filelist = '/home/acp11bw/dirs/tel-us/flists/split/test-file-list/test-file-list-' + os.environ['SGE_TASK_ID']
segments = np.genfromtxt(filelist, dtype=str, delimiter=',', skip_header=0, autostrip=True)
chan_to_num = {'a': '1', 'b': '2'}
#sfbcep -F sphere -l 20 -d 10 -w Hamming -p 19 -e -D -k 0 -i 300 -u 3400 -x 1 SI8-facdk.sph /home/acp11bw/dirs/dev/sre2008/data/mfc/short3.test/SI8-facdk_SI8-A.mfcc
command_prefix = 'sfbcep -F sphere -l 20 -d 10 -w Hamming -p 19 -e -D -k 0 -i 300 -u 3400 -x '

indir = ' /share/spandh.ami4/sid/dev/sre2008/audio/test.short3/'
outdir = ' /share/spandh.ami4/sid/dev/sre2008/data/mfc/short3.test/'

import commands


for seg, chan in segments:
    command = command_prefix + chan_to_num[chan] + indir + 'SI8-' + seg +'.sph' + outdir + 'SI8-' + seg + '_SI8-' + chan.upper() + '.mfcc'
    failure, output = commands.getstatusoutput(command)
    if failure:
        print 'failed to process command: "', command, '"'
        print output
        break



