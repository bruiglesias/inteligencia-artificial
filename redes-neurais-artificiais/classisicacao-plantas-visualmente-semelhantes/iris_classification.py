import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import np_utils


base = pd.read_csv('base_dados.csv')

previsores = base.iloc[:, 0:4].values
classes = base.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()

classes = labelencoder.fit_transform(classes)
classes_dummy = np_utils.to_categorical(classes)

# iris setosa 1 0 0
# iris virginica 0 1 0
# iris versicolor 0 0 1 


from sklearn.model_selection import train_test_split

( previsores_treinamento, 
 previsores_teste, classes_treinamento, 
 classes_teste) = train_test_split(previsores, classes_dummy, test_size = 0.25)

classificador = Sequential()

classificador.add(Dense(units = 4,
                        activation = 'relu',
                        input_dim = 4))

classificador.add(Dense(units = 4,
                        activation = 'relu'))

classificador.add(Dense(units = 3,
                        activation = 'softmax'))

classificador.compile(optimizer = 'adam',
                      loss = 'categorical_crossentropy',
                      metrics = ['categorical_accuracy'])

classificador.fit(previsores_treinamento, 
                  classes_treinamento,
                  batch_size = 10,
                  epochs = 1000)

resultado = classificador.evaluate(previsores_teste,
                                   classes_teste)

previsoes = classificador.predict(previsores_teste)

previsoes = (previsoes > 0.5)

# gerando a matriz de confusão
import numpy as np
classes_teste_2 = [np.argmax(t) for t in classes_teste]
previsoes_2 = [np.argmax(t) for t in previsoes]
from sklearn.metrics import confusion_matrix
matrix = confusion_matrix(previsoes_2, classes_teste_2)



















