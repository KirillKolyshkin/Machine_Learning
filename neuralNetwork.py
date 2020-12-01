import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# нормализуем данные 
x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
# создаем 3 слоя, последний - внешний слой
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
# тренируем модель
model.fit(x=x_train, y=y_train, epochs=5)

model.save('mnist.h5')

# Считаем точность обучения
test_loss, test_acc = model.evaluate(x=x_test, y=y_test)
print('\nTest accuracy:', test_acc)
