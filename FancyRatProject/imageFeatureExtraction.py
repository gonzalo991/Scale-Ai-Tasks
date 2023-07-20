import numpy as np
from scipy.io import loadmat
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import layers, Model, optimizers
import os
from tensorflow.keras.callbacks import (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau)
import matplotlib.pyplot as plt


np.random.seed(10)

train_data = loadmat('train_32x32.mat')
test_data = loadmat('test_32x32.mat')

train_images = np.array(train_data['X'])
test_images = np.array(test_data['X'])
train_labels = train_data['y']
test_labels = test_data['y']
# We set the number of images as the first axis
train_images = np.moveaxis(train_images, -1, 0)
test_images = np.moveaxis(test_images, -1, 0)

train_labels[train_labels == 10] = 0
test_labels[test_labels == 10] = 0

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)

datagen = ImageDataGenerator(rotation_range=10,
                            zoom_range=[0.95, 1.05],
                            height_shift_range=0.1,
                            shear_range=0.1,
                            channel_shift_range=0.1,
                            brightness_range=[0.95, 1.05])

# Input layer with the shape of our images
inputs = layers.Input(shape=(32, 32, 3))

# We will repeat these block for different number of filters, so we can define it first
i=0
def block(inputs, filters, size, drop_out=None):
    global i
    i += 1
    x = layers.Conv2D(filters, size, padding='same',
                        activation='swish',
                        name=f'conv{i}')(inputs)
    x = layers.MaxPooling2D((2, 2))(x)
    if drop_out != None:
        x = layers.Dropout(drop_out)(x)
    return x

# We define the "stem" of the cnn with a convolutional layer with 32 filters
# The activation is 'swish', which usually performs better than the most common "relu"
x = layers.Conv2D(32, (3, 3), padding='same',
                        activation='swish',
                        input_shape=(32, 32, 3),
                        name ='stem_conv2d')(inputs)

x = layers.BatchNormalization(name='stem_bn')(x)
x = layers.Activation('swish', name='stem_activation')(x)

#main "body of the cnn"
for i in range(5, 10):
    if i<9:
        x = block(x, np.power(2,i), (3,3), drop_out=0.2)
    else:
        x = block(x, np.power(2,i), (3,3))

# Classifier, here we use a GlobalAveragePooling instead of flatten the output
# as it also allows to reduce # parameters

x = layers.GlobalAveragePooling2D(name="avg_pool")(x)
x = layers.Dropout(0.3, name="top_dropout")(x)
outputs = layers.Dense(10, activation="softmax", name="predictions")(x)

# Finally, we define the model by specifying the input and output
model = Model(inputs, outputs, name='Custom_model')

optimizer = optimizers.Adam(learning_rate=1e-3)
model.compile(optimizer=optimizer, loss='categorical_crossentropy',
                            metrics=["accuracy"])

def plot_hist(hist, name):
        """Plots training chart"""
        plt.figure(figsize=[12, 10])
        plt.plot(hist.history["accuracy"])
        plt.plot(hist.history["val_accuracy"])
        plt.plot(hist.history["loss"])
        plt.plot(hist.history["val_loss"])
        plt.title(f"{name}")
        plt.ylabel("accuracy")
        plt.xlabel("epoch")
        plt.ylim(top=1.1)
        plt.legend(["train_acc", "validation_acc", "train_loss", "validation_loss"], loc="upper left")
        plt.savefig(f'{name}_chart.png')
        plt.show()

# Stop training if val_loss does not decrease in four consecutive epochs
early_stopping = EarlyStopping(monitor='val_loss',
                            patience=4, restore_best_weights=True)

# save best model indicating epoch
model_save = ModelCheckpoint('./weights/Custom_model_{epoch}.h5',
                            save_best_only=True, monitor='val_loss', verbose=1)
# Folder to save weights
if not os.path.exists('./weights'):
    os.makedirs('./weights', mode=0o770, exist_ok=True)

# reduce learning rate if val_loss does not decrease in 2 epochs, cooldown of 1 epoch
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=2, cooldown=1, verbose=1)

hist = model.fit(datagen.flow(train_images, train_labels, batch_size=128), epochs=50, validation_data=(test_images, test_labels), verbose=1,
                        callbacks=[model_save, reduce_lr, early_stopping])

plot_hist(hist, name='Custom_model')

model.summary()