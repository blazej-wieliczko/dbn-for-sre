from read_spro import load_mfcc_file
import rbm
from numpy import *



X = load_mfcc_file()

bias = ones((X.shape[0], 1))

#X = hstack((bias, X))

ndata, nfeatures = X.shape
nhid = 20

W = zeros(nfeatures)
hids = X

rbm.trainW(X, hids, W, 10, 0.001)


#obs = mydata  #  (Ndata*Nfeatures array)
#obs = addColumnOfOnesForBias(obs)
#for layer = 1:5
#WB = zeros(1, N_nodes_in_this_hidden_layer)
#out  = zeros(Ndata, N_nodes_in_this_hidden_layer)
#for datapoint = 1:Ndata
#out[datapoint, :] = bolzmannprobs(obs[datapoint,:], other args)
#out[datapoint, :] = drawSamplesFrom(out[datapoint, :])
#do a training step with that input and output
#obs = addColumnOfOnesForBias(out)
#return set of trained weight matrices
#
#
#
#