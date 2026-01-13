import imageio.v3 as iio

filenames = ['pic.png', 'second.png']
images = []

for filename in filenames:
  images.append(iio.imread(filename))

iio.imwrite('together.gif', images, duration = 500, loop = 0)
