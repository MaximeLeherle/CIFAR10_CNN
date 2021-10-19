from matplotlib import pyplot
from keras.datasets import cifar10

(train_x, train_y), (test_x, test_y) = cifar10.load_data()


print('train x have the folloing shape : ', train_x.shape)
print('train x have the folloing shape : ', train_y.shape)
print('train x have the folloing shape : ', test_x.shape)
print('train x have the folloing shape : ', test_y.shape)