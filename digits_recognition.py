from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import sklearn.datasets
from mnist import MNIST
import numpy as np


train_path = 'drive-download-20190713T111647Z-001/data/mnist/training'
test_path = 'drive-download-20190713T111647Z-001/data/mnist/testing'
image_data = sklearn.datasets.load_files(train_path, shuffle='False')
test_data = sklearn.datasets.load_files(test_path, shuffle='False')

clf = KNeighborsClassifier()

# Train on the first 10000 images:
train_x = image_data.data
train_x = np.array(train_x)
train_y = image_data.target

print("Train model")
clf.fit(train_x, train_y)

# Test on the next 100 images:
test_x = test_data.data
expected = image_data.target

print("Compute predictions")
predicted = clf.predict(test_x)

print("Accuracy: ", accuracy_score(expected, predicted))