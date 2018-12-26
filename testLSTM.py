import pickle
import matplotlib.pyplot as plt 
file = open('history','rb')
history = pickle.load(file)
plt.plot(history.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
