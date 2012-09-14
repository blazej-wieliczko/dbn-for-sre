import struct
from StringIO import StringIO
import numpy as np


class SproData:
    def __init__(self, dimension, content, framerate, data):
        self.dimension = dimension
        self.content = content
        self.framerate = framerate
        self.data = data


def get_bytes_in_vector(dim):
    return 4 * dim

default_input_file = '/home/blazej/tmp/mfcc/SI8-totcm_SI8-B-M-83366.norm.feat.mfcc'
default_output_file = '/home/blazej/tmp/mfcc/SI8-totcm_SI8-B-M-83366.norm.feat.mfcc-new'

headerend = '</header>\n'

def load_mfcc_file(filename = default_input_file):

    f = open(filename, 'rb')
    rawString = f.read()

    print 'head raw string:', rawString[:20]
    header_pos = rawString.find(headerend)
    if header_pos != -1:
        print 'removing header'
        rawString = rawString[header_pos + len(headerend):]

    print 'head raw string:', rawString[:20]
    f = StringIO(rawString)

#    load the header
    bytes = f.read(2)
    dim = struct.unpack("H", bytes)[0]
    print 'dim:', dim
    bytes = f.read(4)
    content = struct.unpack("i", bytes)
    bytes = f.read(4)
    framerate = struct.unpack("f", bytes)

    str = struct.Struct("f " * dim)

    bytes_in_vector = get_bytes_in_vector(dim)


    data = '_'
    features = []
    while True:
        data = f.read(bytes_in_vector)
        print type(data)
        print len(data)
        if not data:
            break
        features.append(list(str.unpack(data)))

    dataarray = np.array(features)
    return SproData(dim, content, framerate, dataarray)


def save_mfcc_file(sprodata, filename = default_output_file):
    f = open(filename, 'wb')

    f.write(struct.pack("H", sprodata.dimension))
    f.write(struct.pack("i", sprodata.content[0]))
    f.write(struct.pack("f", sprodata.framerate[0]))

    str = struct.Struct("f " * sprodata.dimension)

    assert sprodata.data.shape[1] == sprodata.dimension

    for row in sprodata.data:
        f.write(str.pack(*row))

    f.close()



def split_mfcc_file(infile):
    spro_data = load_mfcc_file(infile)

    alldata = spro_data.data
    splitpoint = alldata.shape[0] / 2
    spro_data.data = alldata[:splitpoint]
    save_mfcc_file(spro_data, infile+'.train')
    spro_data.data = alldata[splitpoint:]
    save_mfcc_file(spro_data, infile+'.test')


    #content_desc = f.read(4)
    #
    #frame_rate = f.read(4)

    #Format	C Type
    #x	pad byte
    #c	char
    #b	signed char
    #B	unsigned char
    #?	_Bool
    #h	short
    #H	unsigned short
    #i	int
    #I	unsigned int	integer	4	(3)
    #l	long	integer	4	(3)
    #L	unsigned long	integer	4	(3)
    #q	long long	integer	8	(2), (3)
    #Q	unsigned long long	integer	8	(2), (3)
    #f	float	float	4	(4)
    #d	double	float	8	(4)
    #s	char[]	string
    #p	char[]	string
    #P	void *	integer	 	(5), (3)er	 	(5), (3)


#filename = '/Volumes/Mac HD/Dropbox/Sheffield/project/data/SI8-faapz_SI8-A.mfcc'
#dim, content, framerate, features = load_mfcc_file(filename)
#dim, content, framerate, features = load_mfcc_file(filename)
#import numpy as np
#np_array = np.array(features)
#print np_array.shape
#print np_array.dtype

if __name__ == '__main__':
    print 'Running'
    sprodata = load_mfcc_file()
    save_mfcc_file(sprodata)

    import  filecmp

    if filecmp.cmp(default_input_file, default_output_file, shallow=False):
        print 'ok'

    split_mfcc_file(default_input_file, '', '')

    original = load_mfcc_file(default_input_file)
    mfcc_file = load_mfcc_file(default_input_file + 'training')
    mfcc_file2 = load_mfcc_file(default_input_file + 'validation')
    together = np.vstack((mfcc_file.data, mfcc_file2.data))
    assert np.all(together == original.data)


