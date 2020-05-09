import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

historico_exames = pd.read_csv('dados_exames.csv')
historico_diagnosticos = pd.read_csv('dados_diagnosticos.csv')


rede_neural = Sequential()
rede_neural.add(Dense(units = 8,
                      activation = 'relu',
                      kernel_initializer = 'normal',
                      input_dim = 30
                          ))
rede_neural.add(Dropout(0.2))
rede_neural.add(Dense(units = 8,
                      activation = 'relu',
                      kernel_initializer = 'normal',
    
                          ))
rede_neural.add(Dropout(0.2))
rede_neural.add(Dense(units = 1,
                      activation = 'sigmoid'
                          ))
    
rede_neural.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                    metrics = ['binary_accuracy'])
    
rede_neural.fit(historico_exames,
                historico_diagnosticos,
                batch_size = 10,
                epochs = 100)

novo_exame = novo = np.array([[15.80, 8.34, 118, 900, 0.10, 0.26, 0.08, 0.134, 0.178,
                  0.20, 0.05, 1098, 0.87, 4500, 145.2, 0.005, 0.04, 0.05, 0.015,
                  0.03, 0.007, 23.15, 16.64, 178.5, 2018, 0.14, 0.185,
                  0.84, 158, 0.363]])

previsao = rede_neural.predict(novo)
previsao = (previsao > 0.5)