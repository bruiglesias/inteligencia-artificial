# -*- coding: utf-8 -*-

import numpy as np
from keras.models import model_from_json

arquivo = open('rede_neural_detecta_cancer.json', 'r')
rede_neural = arquivo.read()
arquivo.close()

rede_neural = model_from_json(rede_neural)
rede_neural.load_weights('pesos_rede_neural.h5')

# previsao em cima de um registro
novo_exame = novo = np.array([[15.80, 8.34, 118, 900, 0.10, 0.26, 0.08, 0.134, 0.178,
                  0.20, 0.05, 1098, 0.87, 4500, 145.2, 0.005, 0.04, 0.05, 0.015,
                  0.03, 0.007, 23.15, 16.64, 178.5, 2018, 0.14, 0.185,
                  0.84, 158, 0.363]])

previsao = rede_neural.predict(novo)
previsao = (previsao > 0.5)

# previsao em cima de uma base
historico_exames = pd.read_csv('dados_exames.csv')
historico_diagnosticos = pd.read_csv('dados_diagnosticos.csv')

rede_neural.compile(optimizer = 'adam', loss = 'binary_crossentropy',
                    metrics = ['binary_accuracy'])

resultado = rede_neural.evaluate(historico_exames, historico_diagnosticos)