from skimage import data
from skimage.filters import try_all_threshold
from skimage.color import rgb2gray
import matplotlib.pyplot as plt

# segmentasi gambar dengan melakukan scanning pixel satu per satu untuk mendefinisikan apakah pixel tersebut termasuk object atau background
# segmentasi tersebut berdasarkan seberapa besar gray level dari suatu pixel apakah lebih besar atau lebih keci dari value keseluruhan

gambarBerwarna = data.astronaut() #gambar asli berupa rgb
gambarAbu = rgb2gray(gambarBerwarna) #kemudian di convert menjadi gambar abu menggunakan rgb2gray filter
plt.imshow(gambarBerwarna)
plt.show()

fig, ax = try_all_threshold(
    gambarAbu, figsize=(10, 8) #verbose=False terjadi error jadi tidak saya sertakan
)

fig.tight_layout()
plt.show()