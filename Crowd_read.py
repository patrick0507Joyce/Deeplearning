import numpy as np
from PIL import Image
import glob


filelist = glob.glob("OutPut/out*.png")
x = np.array([np.array(Image.open(fname)) for fname in filelist])
print(x.shape)