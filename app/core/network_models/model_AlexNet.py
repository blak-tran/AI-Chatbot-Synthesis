from tensorflow import keras
from keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
from keras.optimizers import SGD
from keras.losses import categorical_crossentropy
from keras.models import Sequential
# Get rid of warnings!
import warnings
warnings.filterwarnings('ignore')


class AlexNet(Sequential):
  def __init__(self, input_shape, num_classes):
    super().__init__()

    self.add(Conv2D(64, kernel_size = (3,3),
                    strides= 2, 
                    padding = 'valid', 
                    activation = 'relu',
                    input_shape= input_shape,
                    kernel_initializer= 'he_normal'
                    ))
    
    self.add(MaxPooling2D(pool_size=(3,3), 
                          strides= (2,2),
                          padding= 'valid', 
                          data_format= None))

    self.add(Conv2D(128, kernel_size=(3,3), 
                    strides= 1,
                    padding= 'same', 
                    activation= 'relu',
                    kernel_initializer= 'he_normal'))
    
    self.add(MaxPooling2D(pool_size=(3,3), 
                          strides= (2,2),
                          padding= 'valid', 
                          data_format= None)) 

    self.add(Conv2D(256, kernel_size=(3,3), 
                    strides= 1,
                    padding= 'same', activation= 'relu',
                        kernel_initializer= 'he_normal'))
    
    self.add(MaxPooling2D(pool_size=(3,3), 
                          strides= (2,2),
                          padding= 'valid', 
                          data_format= None)) 

    self.add(Conv2D(512, kernel_size=(3,3), 
                    strides= 1,
                    padding= 'same', 
                    activation= 'relu',
                    kernel_initializer= 'he_normal'))

    self.add(MaxPooling2D(pool_size=(2,2), 
                          strides= (2,2),
                          padding= 'valid', 
                          data_format= None))

    self.add(Flatten())
    self.add(Dense(4096, activation= 'relu'))
    self.add(Dense(4096, activation= 'relu'))
    self.add(Dense(1000, activation= 'relu'))
    self.add(Dense(1000, activation= 'relu'))
    self.add(Dense(1000, activation= 'relu'))
    self.add(Dense(1000, activation= 'relu'))
    self.add(Dense(num_classes, activation= 'softmax'))

    opt = SGD(lr=0.01)
    self.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['accuracy'])