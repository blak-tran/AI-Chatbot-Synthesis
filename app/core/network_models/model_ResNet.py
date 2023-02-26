
import tensorflow
from tensorflow.keras import Model
from tensorflow.keras.layers import Add, GlobalAveragePooling2D,Dense, Flatten, Conv2D, Lambda,Input , BatchNormalization, Activation

from app.core.settings import Settings 

settings  = Settings()

def residual_block(x, number_of_filters, match_filter_size=False):
    
    
    # Retrieve initializer
    initializer = settings.INITIALIZER
    # Create skip connection
    x_skip = x

    # Perform the original mapping
    if match_filter_size:
        x = Conv2D(number_of_filters, kernel_size=(3, 3), strides=(2,2),
                   kernel_initializer=initializer, padding="same")(x_skip)
    else:
        x = Conv2D(number_of_filters, kernel_size=(3, 3), strides=(1,1), 
                   kernel_initializer=initializer, padding="same")(x_skip)
        
    x = BatchNormalization(axis=3)(x)
    x = Activation("relu")(x)
    x = Conv2D(number_of_filters, kernel_size=(3, 3),kernel_initializer=initializer, padding="same")(x)
    x = BatchNormalization(axis=3)(x)

    # Perform matching of filter numbers if necessary
    if match_filter_size and settings.SHORTCUT_TYPE == "identity":
        x_skip = Lambda(lambda x: tensorflow.pad(x[:, ::2, ::2, :], tensorflow.constant([[0, 0,], [0, 0], [0, 0], [number_of_filters//4, number_of_filters//4]]), mode="CONSTANT"))(x_skip)
    elif match_filter_size and  settings.SHORTCUT_TYPE == "projection":  
        x_skip = Conv2D(number_of_filters, kernel_size=(1,1),kernel_initializer=initializer, strides=(2,2))(x_skip)
    # Add the skip connection to the regular mapping 
    x = Add()([x, x_skip])

    # Nonlinearly activate the result
    x = Activation("relu")(x)
    # Return the result

    return x


def ResidualBlocks(x):
  # Set initial filter size
    filter_size = settings.INIT_FM_DIM


    for layer_group in range(3):
        for block in range(settings.N):
            if layer_group > 0 and block == 0:
                filter_size *= 2
                x = residual_block(x, filter_size, match_filter_size=True)
            else:
                x = residual_block(x, filter_size)

    return x

def model_base(shp):
  # Get number of classes from model configuration
    initializer = settings.INITIALIZER

    # Define model structure
    # logits are returned because Softmax is pushed to loss function.
    inputs = Input(shape=shp)
    x = Conv2D(settings.INIT_FM_DIM, kernel_size=(3,3),\
        strides=(1,1), kernel_initializer=initializer, padding="same")(inputs)
    x = BatchNormalization()(x)
    x = Activation("relu")(x)
    x = ResidualBlocks(x)
    x = GlobalAveragePooling2D()(x)
    x = Flatten()(x)
    outputs = Dense(settings.NUM_CLASSES, kernel_initializer=initializer)(x)

    return inputs, outputs
    

def init_ResNet_model():
  # Get model base
    inputs, outputs = model_base((settings.WIDTH, settings.HEIGHT,settings.CHANNELS))
    
  # Initialize and compile mode

    model = Model(inputs, outputs, name=settings.NAME)
    model.compile(loss=settings.LOSS, optimizer=settings.OPTIMIZER, metrics=settings.OPTIMIZER_ADDITIONAL_METRICS)

    return model