from random import gauss
import matplotlib.pyplot as plt
from scipy import misc
from skimage.filters import gaussian

# Smoothing umumnya digunakan untuk menyamarkan noise pada citra dengan cara memberikan blur pada citra.

gambar = misc.face()
# gambar belum ter-blur
plt.gray()
plt.imshow(gambar)
plt.show()

smoothedGambar = gaussian(gambar, multichannel=True, sigma=2)
# gambar telah ter-blur

plt.imshow(smoothedGambar)
# yang ditampilkan bukan lagi gambar melainkan smoothedGambar

plt.show