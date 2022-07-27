from PIL import Image
from matplotlib import pyplot as plt

# image asli
original = Image.open("./logounmer.png")

# image flip vertical
flipVertical = original.transpose(method=Image.FLIP_TOP_BOTTOM)
# image flip horizontal
flipHorizontal = original.transpose(method=Image.FLIP_LEFT_RIGHT)

# tampilan plot
fig, axes = plt.subplots(1,3, figsize=(8,4))
ax = axes.ravel()

ax[0].imshow(original)
ax[0].set_title("Original")
ax[1].imshow(flipVertical)
ax[1].set_title("Flip Vertical")
ax[2].imshow(flipHorizontal)
ax[2].set_title("Flip Horizontal")

fig.tight_layout()
plt.show()