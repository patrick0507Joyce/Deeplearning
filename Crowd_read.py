import numpy as np
from PIL import Image
import glob
import scipy.io

# grass 1,2 followed by square 1, 2, 3 and inside 1, 2, 3(problem), 4, 5, 6


matlist = glob.glob("crowd-dataset/1MeiYiZhenEntropy0*.mat")
# mat_set = np.array([np.array(scipy.io.loadmat(matname)) for matname in matlist])
mat_set_01 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy01.mat")
feature01 = mat_set_01['C']
print(feature01.shape)
mat_set_02 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy02.mat")
feature02 = mat_set_02['C']
print(feature02.shape)
mat_set_03 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy03.mat")
feature03 = mat_set_03['C']
print(feature03.shape)
mat_set_04 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy04.mat")
feature04 = mat_set_04['C']
print(feature04.shape)
mat_set_05 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy05.mat")
feature05 = mat_set_05['C']
print(feature05.shape)
mat_set_06 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy06.mat")
feature06 = mat_set_06['C']

print(feature06.shape)
mat_set_07 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy07.mat")
feature07 = mat_set_07['C']
print(feature07.shape)
mat_set_08 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy08.mat")
feature08 = mat_set_08['C']
print(feature08.shape)
mat_set_09 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy09.mat")
feature09 = mat_set_09['C']
print(feature09.shape)
mat_set_010 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy010.mat")
feature010 = mat_set_010['C']
print(feature010.shape)
mat_set_011 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy011.mat")
feature011 = mat_set_011['C']
print(feature011.shape)

print(feature01.shape[1] + feature02.shape[1] + feature03.shape[1] +
      feature04.shape[1] + feature05.shape[1] + feature06.shape[1] +
      feature07.shape[1] + feature08.shape[1] + feature09.shape[1] +
      feature010.shape[1] + feature011.shape[1])

print(feature02[0, 600:690])