from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras import backend as K
import tensorflow as tf
from tensorflow.keras.regularizers import l2
batch_size = 16
train_datagen = ImageDataGenerator()
test_datagen = ImageDataGenerator()

train_generator = train_datagen.flow_from_directory(
        # This is the target directory
        'data/denoised/train',
        # All images will be resized to 150x150
        target_size=(256, 256),
        batch_size=batch_size,
        shuffle=True,
        # Since we use categorical_crossentropy loss, we need binary labels
        class_mode='binary')

test = test_datagen.flow_from_directory(
        'data/denoised/test',
        target_size=(256, 256),
        batch_size=batch_size,
        class_mode='binary')

def recall_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    recall = true_positives / (possible_positives + K.epsilon())
    return recall

def precision_m(y_true, y_pred):
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    return precision

def f1_m(y_true, y_pred):
    precision = precision_m(y_true, y_pred)
    recall = recall_m(y_true, y_pred)
    return 2*((precision*recall)/(precision+recall+K.epsilon()))

# train_generator.
# print(train_generator.labels)
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(256, 256, 3)),
    # tf.keras.layers.MaxPool2D((2,2)),
    # tf.keras.layers.Conv2D(16, (1,1)),
    tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(512,activation='relu', kernel_regularizer=l2(0.01)),
    # tf.keras.layers.Dense(256,activation='relu', kernel_regularizer=l2(0.01)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
    # tf.keras.layers.Flatten(input_shape=(128,128,3)),
    # tf.keras.layers.Dense(128,activation='relu',kernel_regularizer=l2(0.01)),
    # tf.keras.layers.Dense(64,activation='relu',kernel_regularizer=l2(0.01)),
    # tf.keras.layers.Dense(256,activation='relu',kernel_regularizer=l2(0.01)),
    # tf.keras.layers.Dense(1,activation='sigmoid')
    # tf.keras.layers.Conv2D(64, (3,3), activation='relu', input_shape=(128, 128, 3)),
    # tf.keras.layers.Dropout(0.4),
    # tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(64, activation='relu'),
    # tf.keras.layers.Dense(1, activation='sigmoid')
    # tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(128, 128, 3)),
#     tf.keras.layers.Flatten(input_shape=(128,128,3)),
#     tf.keras.layers.Dense(512, activation='relu'),
#     tf.keras.layers.Dense(256,activation='relu'),
#     tf.keras.layers.Dense(32,activation='relu'),
#     tf.keras.layers.Dense(1, activation='sigmoid')
    # tf.keras.layers.MaxPooling2D(2, 2),
    # tf.keras.layers.Dropout(0.5),
    # tf.keras.layers.Conv2D(32, (3,3), activation='relu'),
    # tf.keras.layers.Flatten(),
    # tf.keras.layers.Dense(512, activation='relu'),
    # tf.keras.layers.Dense(1, activation='sigmoid')
])
print("Training on noisy images")
model.summary()
# optimizer = tf.keras.optimizers.Adam(lr=0.001)
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['acc',f1_m,precision_m, recall_m])
model.fit(train_generator,epochs=5)
loss, accuracy, f1_score, precision, recall = model.evaluate_generator(test)
print("Test statistics:")
print("Accuracy:", accuracy)
print("Precision",precision)
print("Recall",recall)
print("F1_score:", f1_score)