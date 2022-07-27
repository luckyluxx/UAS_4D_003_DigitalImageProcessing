import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import sobel
from skimage.color import rgb2gray

# edge detection adalah sebuah metode pendeteksian citra digital untuk mengetahui bagian mana yang termasuk objek 
# serta bagian mana yang termasuk background sehingga dapat meminimalisasi data diproses yang dianggap tidak berkaitan.

gambarBerwarna = data.astronaut() #gambar asli berupa rgb
gambarAbu = rgb2gray(gambarBerwarna) #kemudian di convert menjadi gambar abu menggunakan rgb2gray filter
gambarEdge = sobel(gambarAbu) #gambar yang di tampilkan garis tepinya adalah gambar abu

plt.imshow(gambarAbu, cmap=plt.cm.gray)
plt.show()

plt.imshow(gambarEdge)
plt.show()