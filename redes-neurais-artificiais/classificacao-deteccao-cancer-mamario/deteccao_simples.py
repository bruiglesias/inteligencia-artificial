import pandas as pd
import keras
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from sklearn.metrics import confusion_matrix, accuracy_score

NEURONIOS_ENTRADA = 30
NEURONIOS_OCULTOS = 16
NEURONIOS_SAIDA = 1
ATIVACAO_NEURONIOS = 'relu'

historico_exames = pd.read_csv('dados_exames.csv')
historico_diagnosticos = pd.read_csv('dados_diagnosticos.csv')

(exames_treinamento, 
     exames_teste_rn, 
     diagnosticos_treinamento, 
     diagnosticos_teste) = train_test_split(historico_exames, 
                                                historico_diagnosticos, 
                                                test_size=0.25)

rede_neural = Sequential()
rede_neural.add(Dense(units = NEURONIOS_OCULTOS, 
                      activation = ATIVACAO_NEURONIOS,
                      kernel_initializer = 'random_uniform',
                      input_dim = NEURONIOS_ENTRADA
                      ))
rede_neural.add(Dense(units = NEURONIOS_OCULTOS, 
                      activation = ATIVACAO_NEURONIOS,
                      kernel_initializer = 'random_uniform',

                      ))
rede_neural.add(Dense(units = NEURONIOS_SAIDA, 
                      activation = 'sigmoid'
                      ))

otimizador = keras.optimizers.Adam(lr = 0.001, decay = 0.0001, clipvalue = 0.5)

rede_neural.compile(optimizer = otimizador, loss='binary_crossentropy',
                    metrics = ['binary_accuracy'])


rede_neural.fit(exames_treinamento, 
                diagnosticos_treinamento,
                batch_size = 10,
                epochs = 100)  

# pesos da camada de entrada para camada oculta
pesos_entrada_oculta = rede_neural.layers[0].get_weights()                                       
print(pesos_entrada_oculta)
print(len(pesos_entrada_oculta)) 

# pesos da primeira camada oculta para segunda camada oculta
pesos_ocula_oculta = rede_neural.layers[1].get_weights()      
print(pesos_ocula_oculta)
print(len(pesos_ocula_oculta)) 

# pesos da segunda camada oculta para camada de saida
pesos_ocula_saida = rede_neural.layers[2].get_weights()      
print(pesos_ocula_saida)
print(len(pesos_ocula_saida)) 

                           
previsoes = rede_neural.predict(exames_teste_rn)
previsoes = previsoes > 0.5

# precisao manual usando sklearn
precisao = accuracy_score(diagnosticos_teste, previsoes)
matriz_confusão = confusion_matrix(diagnosticos_teste, previsoes)

# precisao usando keras
resultado = rede_neural.evaluate(exames_teste_rn,diagnosticos_teste)                                            