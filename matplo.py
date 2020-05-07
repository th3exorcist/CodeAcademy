import matplot.lib as plt
import tensorflow as tf

''' live tensorflow no twitch - mnist database'''

plt.imshow(imagens_treino[0])

imagens_treino = imagens_treino/255.0
imagens_teste = imagens_teste/255.0
print("Imagens normalizadas")

modelo = tf.keras.Sequential(
    
    tf.keras.layers.Flatten() # transforma em unidimensional
    tf.keras.layers.Dense(128, activation=tf.nn.relu)
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
)

modelo.compile(optimizer=tf.optimizers.Adam(),
              loss='sparse_categorical_crossentropy,
              metrics=['accuracy'])
print("modelo compilado")

modelo.fit(imagens_treino, rotulo_treino, epochs=5)

modelo.evaluate(imagens_teste, rotulo_testes)