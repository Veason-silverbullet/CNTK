import numpy as np
from sklearn.preprocessing import normalize
import struct
import os
import sys
data_size = 1862120
feature_dim = 256
def generateBinSingleImage(inputfile,outputfile):
    features_all = np.zeros( (data_size, feature_dim), dtype=np.float32 )
    f = open(inputfile,'r')
    i = 0
    for line in f.readlines():
        line = line.strip()
        feature = line.split('\t')[1].split(' ')
        feature = np.array([float(x) for x in feature])
        features_all[i,:] = feature
        #features_all[i,:] = normalize(feature.reshape(1,-1))[0]
        i = i + 1
    features_all = normalize(features_all)
    print(features_all)
    f.close()
    # write file
    print('Start writing file.')
    rows, cols = features_all.shape
    assert rows == data_size
    with open(outputfile, 'wb') as f:
        f.write(struct.pack('4i', rows, cols, cols * 4, 5))
        f.write(features_all.data)    

def generateBinSingleImageMirror(inputfile,inputfile2,outputfile):
    features_all = np.zeros( (data_size, feature_dim), dtype=np.float32 )
    f = open(inputfile,'r')
    i = 0
    for line in f.readlines():
        line = line.strip()
        feature = line.split('\t')[1].split(' ')
        feature = np.array([float(x) for x in feature])
        features_all[i,:] = feature
        #features_all[i,:] = normalize(feature.reshape(1,-1))[0]
        i = i + 1
    f.close()
    f = open(inputfile2,'r')
    i = 0
    for line in f.readlines():
        line = line.strip()
        feature = line.split('\t')[1].split(' ')
        feature = np.array([float(x) for x in feature])
        features_all[i,:] += feature
        #features_all[i,:] = normalize(features_all[i,:].reshape(1,-1))[0]
        i = i + 1
    f.close()
    features_all = normalize(features_all)
    print(features_all)
    # write file
    print('Start writing file.')
    rows, cols = features_all.shape
    assert rows == data_size
    with open(outputfile, 'wb') as f:
        f.write(struct.pack('4i', rows, cols, cols * 4, 5))
        f.write(features_all.data)    


if __name__ == '__main__':
    assert len(sys.argv) == 2, '2 args are needed'
    model_path = sys.argv[1]
    #F:\chol\IBug\fix7.0_proxyless_GDConv\results\096
    filein = os.path.join(model_path, 'result.txt')
    #filemirror = 'F:\\chol\\IBug\\fix7.0_proxyless_GDConv\\results\\096\\result_test_mirror.txt'
    fileout = os.path.join(model_path, 'result.bin')
    generateBinSingleImage(filein,fileout)
    #generateBinSingleImageMirror(filein,filemirror,fileout)
