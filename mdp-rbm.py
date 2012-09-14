from  mdp.nodes import RBMNode
import mdp
from numpy import *
import time

import read_spro

X = read_spro.load_mfcc_file()



rbm = RBMNode(10, X.shape[1])


x2 = X.dot(X.T)

print x2.shape

mdp_pca = mdp.pca(x2)

print X.shape

