import os
import cv2
import numpy as np


def extract_mnist(image_f, label_f):
	'''
	This function is used to extract image files and the corresponding labels from ubyte format and save them in seperate directory.
	Source: https://gist.github.com/fukuroder/caa351677bf718a8bfe6265c2a45211f
	P.S. - The source of the code is not working due to some bugs. This function has modifications to work as per my liking.
	Parameters:
	image_f - full-path to the uncompressed images file
	labels_f - full-path to the uncompressed labels file

	Returns: 
	None
	'''
	with open(image_f, 'rb') as f:
		images = f.read()
	with open(label_f, 'rb') as f:
		labels = f.read()
	
	images = [d for d in images[16:]]
	images = np.array(images, dtype=np.uint8)
	images = images.reshape((-1,28,28))
	
	outdir = image_f + "_folder"
	if not os.path.exists(outdir):
		os.mkdir(outdir)
	for k,image in enumerate(images):
		cv2.imwrite(os.path.join(outdir, '%05d.png' % (k,)), image)
	
	labels = ['%05d.png %d' % (k, l) for k,l in enumerate(labels[8:])]
	with open('%s.txt' % label_f, 'w') as f:
		f.write(os.linesep.join(labels))


# train_image = 'train-images-idx3-ubyte'
# train_label = 'train-labels-idx1-ubyte'
# test_image = 't10k-images-idx3-ubyte'
# test_label = 't10k-labels-idx1-ubyte'

# # for f in [train_image, train_label, test_image, test_label]:
# # 	os.system('wget --no-check-certificate http://yann.lecun.com/exdb/mnist/%s.gz' % (f,))
	
# # for f in [train_image, train_label, test_image, test_label]:
# # 	os.system('gunzip %s.gz' % (f,))

# for image_f, label_f in [(train_image, train_label), (test_image, test_label)]:
# 	with open(image_f, 'rb') as f:
# 		images = f.read()
# 	with open(label_f, 'rb') as f:
# 		labels = f.read()
	
# 	images = [d for d in images[16:]]
# 	images = np.array(images, dtype=np.uint8)
# 	images = images.reshape((-1,28,28))
	
# 	outdir = image_f + "_folder"
# 	if not os.path.exists(outdir):
# 		os.mkdir(outdir)
# 	for k,image in enumerate(images):
# 		cv2.imwrite(os.path.join(outdir, '%05d.png' % (k,)), image)
	
# 	labels = [outdir + '/%05d.png %d' % (k, l) for k,l in enumerate(labels[8:])]
# 	with open('%s.txt' % label_f, 'w') as f:
# 		f.write(os.linesep.join(labels))