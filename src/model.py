import keras
from keras.preprocessing import image
from keras.applications import imagenet_utils
import numpy as np

# Importing MOBILE NET
mobile = keras.applications.mobilenet.MobileNet()


def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array_expanded_dims = np.expand_dims(img_array, axis=0)
    return keras.applications.mobilenet.preprocess_input(img_array_expanded_dims)


def predict(target_image):
    preprocessed_image = prepare_image(target_image)
    predictions = mobile.predict(preprocessed_image)
    results = imagenet_utils.decode_predictions(predictions)
    return results
