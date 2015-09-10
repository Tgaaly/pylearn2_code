# creates dataset from images contained in directory structure corresponding to class labels
# e.g. chairs: chair1.png, chair2.png, boats: boat1.png, boat2.png, cars: car1.png, car2.png, car3.png

import sys
import glob
import pickle
import os, os.path
import gzip, cPickle
from PIL import Image


path = '/path_to_root_dir'

imgs = []
lbls = []
valid_images = ['.jpg','.gif','.png','.tga']
for f in os.listdir(path):
	print f
	if os.path.isdir(os.path.join(path,f)):
		subpath = os.path.join(path,f)
		print 'going deeper into ' + f
		for f2 in os.listdir(subpath):
			ext = os.path.splitext(f2)[1]
			if ext.lower() not in valid_images:
				continue
			print os.path.join(path,f)
			imgs.append(Image.open(os.path.join(subpath,f2)))
			lbls.append(f)
	else:
		#print os.path.isfile(os.path.join(path,f))
		ext = os.path.splitext(f)[1]
		if ext.lower() not in valid_images:
			continue
		print os.path.join(path,f)
		imgs.append(Image.open(os.path.join(path,f)))
		lbls.append('anonymous')


print lbls
print imgs
print '# of images read : ' + str(len(imgs))
print '# of labels read : ' + str(len(lbls))


# make pickle file with images and their labels
f = gzip.open('file.pkl.gz','wb')
cPickle.dump((imgs,lbls), f, protocol=2)
f.close()

# make pickle file with images and their labels
f = gzip.open('file.pkl.gz','wb')
cPickle.dump((imgs,lbls), f, protocol=2)
f.close()

# test by unpacking pkl file and displaying images
fo = open('file.pkl','rb')
(imgs2,lbls2) = cPickle.load(fo)
fo.close()
print '# of images loaded : ' + str(len(imgs))
print '# of labels loaded : ' + str(len(lbls))
plt.imshow(imgs2[0])
plt.show()
