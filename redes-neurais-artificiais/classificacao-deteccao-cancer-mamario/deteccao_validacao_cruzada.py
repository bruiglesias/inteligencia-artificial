import pandas as pd
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score

historico_exames = pd.read_csv('dados_exames.csv')
historico_diagnosticos = pd.read_csv('dados_diagnosticos.csv')


def criar_rede():
    NEURONIOS_ENTRADA = 30
    NEURONIOS_OCULTOS = 16
    NEURONIOS_SAIDA = 1
    ATIVACAO_NEURONIOS = 'relu'
    
    rede_neural = Sequential()
    rede_neural.add(Dense(units = NEURONIOS_OCULTOS, 
                          activation = ATIVACAO_NEURONIOS,
                          kernel_initializer = 'random_uniform',
                          input_dim = NEURONIOS_ENTRADA
                          ))
    rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = NEURONIOS_OCULTOS, 
                          activation = ATIVACAO_NEURONIOS,
                          kernel_initializer = 'random_uniform',
    
                          ))
    rede_neural.add(Dropout(0.2))
    rede_neural.add(Dense(units = NEURONIOS_SAIDA, 
                          activation = 'sigmoid'
                          ))
    
    otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)
    
    rede_neural.compile(optimizer = otimizador, loss='binary_crossentropy',
                        metrics = ['binary_accuracy'])
    
    return rede_neural
    


rede_neural = KerasClassifier(build_fn = criar_rede,
                              epochs = 100,
                              batch_size = 10)

resultados = cross_val_score(estimator = rede_neural,
                             X=historico_exames,
                             y=historico_diagnosticos,
                             cv = 10,
                             scoring = 'accuracy')

media = resultados.mean()
# quanto maior o valor maior a probabilidade de haver overfit
# overfit = quando a rede neural se adapta demais aos dados de treinamento
desvio_padrao = resultados.std()


