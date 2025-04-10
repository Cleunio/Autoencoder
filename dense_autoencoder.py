# -*- coding: utf-8 -*-
"""Dense_Autoencoder.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Bt8uT2DwkX13AEj-1vhD8YwWrNxgJa3F
"""

!pip install tensorflow==2.16.1

import numpy as np
import pandas as pd
import matplotlib
import tensorflow as tf
import sklearn

np.__version__, pd.__version__, matplotlib.__version__, tf.__version__, sklearn.__version__

from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input, InputLayer
import matplotlib.pyplot as plt

(X_train, _), (X_test, _) = mnist.load_data()
X_train = X_train.astype('float32')/255
X_test = X_test.astype('float32')/255
X_test = X_test.reshape((len(X_test), np.pro(X_test.shape[1:])))
X_train = X_train.reshape((len(X_train), np.pro(X_train.shape[1:])))

autoencoder = Sequential()
autoencoder.add(InputLayer(input_shape=(784,)))
autoencoder.add(Dense(units=128, activation='relu'))
autoencoder.add(Dense(units=64, activation='relu'))
autoencoder.add(Dense(units=32, activation='relu'))

autoencoder.add(Dense(units=64, activation='relu'))
autoencoder.add(Dense(units=128, activation='relu'))
autoencoder.add(Dense(units=784, activation='sigmoid'))

autoencoder.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
autoencoder.fit(X_train, X_train, epochs=50, batch_size=256, validation_data=(X_train, X_test))

dim_original = Input(shape=(784,))
layer_encoder1=autoencoder.layers[0]
layer_encoder2=autoencoder.layers[1]
layer_encoder3=autoencoder.layers[2]
encoder = Model(dim_original, layer_encoder3(layer_encoder2(layer_encoder1(dim_original))))

images_cod = encoder.predict(X_test)

d_images = autoencoder.predict(X_test)

n_images = 10
images_test = np.random.randint(X_test.shape[0], size=n_images)
plt.figure(figsize=(18, 18))
for i, i_image in enumerate(images_test)
  o_image = plt.subplot(10, 10, i+1)
  plt.imshow(X_test[i_image].reshape(28, 28))
  plt.xticks()
  plt.yticks()

  o_image = plt.subplot(10, 10, i+1+n_images)
  plt.imshow(images_cod[i_image].reshape(8,4))
  plt.xticks()
  plt.yticks()

  o_image = plt.subplot(10, 10, i+1+n_images*2)
  plt.imshow(d_images[i_image].reshape(8,4))
  plt.xticks()
  plt.yticks()