import tensorflow as tf
from keras.models import load_model
import numpy as np

model = load_model("models/model")
img_height= 256
img_width= 256

def predict():
    test_image = tf.keras.utils.load_img("photo.png", target_size=(img_height, img_width))
    test_image = tf.keras.utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    predictions = model.predict(test_image)

    class_names = (tf.keras.utils.image_dataset_from_directory("Garbage")).class_names

    return (class_names[np.argmax(tf.nn.softmax(predictions[0]))])

def predictURL(img_url):

    img_path = tf.keras.utils.get_file(origin=img_url)
    test_image = tf.keras.utils.load_img(img_path, target_size=(img_height, img_width))
    test_image = tf.keras.utils.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis = 0)

    predictions = model.predict(test_image)

    class_names = (tf.keras.utils.image_dataset_from_directory("Garbage")).class_names

    return (class_names[np.argmax(tf.nn.softmax(predictions[0]))])
