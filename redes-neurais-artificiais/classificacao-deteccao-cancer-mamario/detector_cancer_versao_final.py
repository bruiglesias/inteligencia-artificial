import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import GridSearchCV
from keras.callbacks import ModelCheckpoint

historico_exames = pd.read_csv('dados_exames.csv')
historico_diagnosticos = pd.read_csv('dados_diagnosticos.csv')


# encontrando a melhor combinação de parametros
def criar_rede(optimizer, loss, kernel_initializer,
                activation, neurons):
    
    rede_neural = Sequential()
    rede_neural.add(Dense(units = neurons, 
                          activation = activation,
                          kernel_initializer = kernel_initializer,
                          input_dim = 30
                          ))
    rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = neurons, 
                          activation = activation,
                          kernel_initializer = kernel_initializer,
    
                          ))
    rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = neurons, 
                          activation = activation,
                          kernel_initializer = kernel_initializer,
    
                          ))
    rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = neurons, 
                          activation = activation,
                          kernel_initializer = kernel_initializer,
    
                          ))
    rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = 1, 
                          activation = 'sigmoid'
                          ))
    
    rede_neural.compile(optimizer = optimizer, loss = loss,
                        metrics = ['binary_accuracy'])
    
    return rede_neural

rede_neural = KerasClassifier(build_fn = criar_rede)

parametros = {'batch_size': [5, 10, 20, 30, 40],
               'epochs': [50, 100, 500, 1000],
               'optimizer': ['adam', 'sgd'],
               'loss': ['binary_crossentropy', 'hinge'],
               'kernel_initializer': ['random_uniform', 'normal'],
               'activation': ['relu', 'tanh'],
               'neurons': [8, 16, 24, 32, 64]}

grid_search = GridSearchCV(estimator = rede_neural,
                           param_grid = parametros,
                           scoring = 'accuracy',
                           cv = 10)

grid_search = grid_search.fit(historico_exames, historico_diagnosticos )

melhores_parametros = grid_search.best_params_
melhor_precisao = grid_search.best_score_

# gerando a rede final
rede_neural = criar_rede(optimizer = melhores_parametros['optimizer'],
                         loss = melhores_parametros['loss'],
                         kernel_initializer = melhores_parametros['kernel_initializer'],
                         activation =  melhores_parametros['activation'],
                         neurons = melhores_parametros['neurons'])


# salvando a arquitetura e os pesos
checkpoint = ModelCheckpoint("best_weight.h5", monitor='loss', verbose=1,
    save_best_only=True, save_weights_only=True, mode='auto', period=1)

rede_neural.fit(historico_exames,
                historico_diagnosticos,
                batch_size = melhores_parametros['batch_size'],
                epochs = melhores_parametros['epochs'],
                callbacks=[checkpoint])

rede_neural_json = rede_neural.to_json()
with open('arquitetura_rede_neural.json', 'w') as json_file:
    json_file.write(rede_neural_json)


