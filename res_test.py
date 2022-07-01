
from tensorflow.keras.applications.resnet50 import ResNet50

if __name__ == '__main__':

    resnet_model = ResNet50(weights = None, include_top=False, input_shape = (224, 224, 3))
    x = Dense(512, activation="relu")(x)

    x = Dense(256, activation="relu")(x)
    x = Dropout(0.5)(x)
    predictions = Dense(2, activation="softmax")(x)
    print(resnet_model.output)