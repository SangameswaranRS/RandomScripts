import pandas as pd 
import numpy as np
import keras
import tensorflow as tf
import matplotlib
# matplotlib.use("agg")
import matplotlib.pyplot as plt
print('[INFO] Libraries Imported')

df = pd.read_csv('logicGate.csv')
trainingDataFeatures = np.array(df.drop(['y'],1))
trainingDataLabels = np.array(df['y'])
print('[INFO] Creating Neural Network ')
classifier = keras.Sequential()
classifier.add(keras.layers.Dense(16,input_dim=2,activation=tf.nn.relu))
classifier.add(keras.layers.Dense(1,activation=tf.nn.sigmoid))
classifier.compile(optimizer=tf.train.AdamOptimizer(),loss='mean_squared_error',metrics=['accuracy'])
history = classifier.fit(trainingDataFeatures, trainingDataLabels, epochs=500)
print('[INFO] Neural Network Trained')
result = classifier.predict(trainingDataFeatures).round()
print('[RESULT] '+ str(result))
plt.plot(history.history['acc'])
# plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
