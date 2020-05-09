import pandas as pd
import keras
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


rede_neural_json = rede_neural.to_json()
with open('rede_neural_detecta_cancer.json', 'w') as json_file:
    json_file.write(rede_neural_json)
    
rede_neural.save_weights('pesos_rede_neural.h5')
