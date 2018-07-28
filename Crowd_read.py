import numpy as np
from PIL import Image
import glob
import scipy.io

# grass 1,2 followed by  inside 1, 2, 3(problem), 4, 5, 6 square 1, 2, 3


matlist = glob.glob("crowd-dataset/1MeiYiZhenEntropy0*.mat")
# mat_set = np.array([np.array(scipy.io.loadmat(matname)) for matname in matlist])
mat_set_01 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy01.mat")
feature01 = mat_set_01['C']
print(feature01.shape)
mat_set_02 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy010.mat")
feature02 = mat_set_02['C']
print(feature02.shape)
mat_set_03 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy011.mat")
feature03 = mat_set_03['C']
print(feature03.shape)
mat_set_04 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy06.mat")
feature04 = mat_set_04['C']
print(feature04.shape)
mat_set_05 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy05.mat")
feature05 = mat_set_05['C']
print(feature05.shape)
mat_set_06 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy04.mat")
feature06 = mat_set_06['C']

print(feature06.shape)
mat_set_07 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy03.mat")
feature07 = mat_set_07['C']
print(feature07.shape)
mat_set_08 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy02.mat")
feature08 = mat_set_08['C']
print(feature08.shape)
mat_set_09 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy07.mat")
feature09 = mat_set_09['C']
print(feature09.shape)
mat_set_010 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy08.mat")
feature010 = mat_set_010['C']
print(feature010.shape)
mat_set_011 = scipy.io.loadmat("crowd-dataset/1MeiYiZhenEntropy09.mat")
feature011 = mat_set_011['C']
print(feature011.shape)

feature = []
feature.append(0)
feature.append(feature01)
feature.append(feature02)
feature.append(feature03)
feature.append(feature04)
feature.append(feature05)
feature.append(feature06)
feature.append(feature07)
feature.append(feature08)
feature.append(feature09)
feature.append(feature010)
feature.append(feature011)
feature_smoothed = feature
feature_length = 0
