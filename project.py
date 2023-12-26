import numpy as np
from PIL import image

img1 = image.open("1.jpg")
img1.show()

img2 = image.open("2.jpg")
img2.show()

mat1 = np.array(img1)
print(mat1)

print ("..........................................................")

mat2 = np.array(img2)
print(img2)

print("..........................................................")

diff = mat1 -mat2
print(diff)

res = image.fromarray(diff)
res.show()
