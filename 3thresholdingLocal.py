import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import sobel
from skimage.color import rgb2gray

# proses identifikasi local thresholding berjalan lebih lambat dibanding global tresholding
# local thresholding bekerja dengan baik apabila pada background terdapat corak yang lebih kompleks atau beragam



gambarBerwarna = data.astronaut() #gambar asli berupa rgb
gambarAbu = rgb2gray(gambarBerwarna) #kemudian di convert menjadi gambar abu menggunakan rgb2gray filter
gambarEdge = sobel(gambarAbu) #gambar yang di tampilkan garis tepinya adalah gambar abu

plt.imshow(gambarAbu, cmap=plt.cm.gray)
plt.show()

plt.gray()
plt.imshow(gambarEdge)
plt.show()