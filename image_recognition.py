import tensorflow as tf
from tensorflow import keras

# Cargar el modelo pre-entrenado
model = keras.applications.ResNet50(weights='imagenet')

# Cargar una imagen de prueba
image_path = 'C:/Users/gonxa/OneDrive/Imágenes/Hidroponia/8c025a08bbb9519fd0d2f0ac647c4be6--hydroponic-systems-hydroponic-gardening.jpg'
image = keras.preprocessing.image.load_img(image_path, target_size=(224, 224))
image_array = keras.preprocessing.image.img_to_array(image)
image_array = tf.expand_dims(image_array, 0)
image_array = keras.applications.resnet.preprocess_input(image_array)

# Realizar la predicción de la imagen
predictions = model.predict(image_array)
decoded_predictions = keras.applications.resnet.decode_predictions(predictions, top=3)

# Mostrar las predicciones
for pred in decoded_predictions[0]:
    print(f"{pred[1]}: {pred[2]*100}%")
