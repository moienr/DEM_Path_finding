import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import generic_filter
from scipy.stats import mode

mainpath= plt.imread('mainpath.tif')

mainpath = mainpath[:,:,1]

m = np.zeros((320, 216))
m[:,:-1]  = mainpath 
print(m.shape)
mainpath = m

count = np.count_nonzero(mainpath)
print(count)


output_path = np.load('best.npy')
print(output_path.shape)



x = (mainpath+output_path)
y =x>125

count = np.count_nonzero(y)
print(count)


y= y*255

#applying 3x3 max filter to make the lines thicker
from scipy import ndimage, misc
conjunction = ndimage.maximum_filter(y, size=2)



fig, (ax1, ax2,ax3) = plt.subplots(1, 3)
fig.suptitle('Real Path vs AI')
ax1.imshow((mainpath>1)*125)
ax2.imshow(output_path)
ax3.imshow(conjunction)
ax1.axis('off')
ax2.axis('off')
ax3.axis('off')
ax1.set_title('Real Path')
ax2.set_title('AI Path')
ax3.set_title('Overlaping pixels')
plt.show()


