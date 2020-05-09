# -*- coding: utf-8 -*-
#
# Programa: Trabalhando com histograma de imagens
#
# Autor: Bruno P. Iglesias


import cv2
import numpy as np
from matplotlib import pyplot as grafico

# gera o histograma da imagem
imagem = cv2.imread("imagem.bmp", 0)
grafico.hist(imagem.ravel(), 256, [0,256])
grafico.show()


# esse trecho separa a imagem em 3 canais e gera o grafico com 
# os valores de cada canal
azul, verde, vermelho = cv2.split(imagem)

grafico.hist(azul.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(verde.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(vermelho.ravel(), 256, [0,256])

grafico.show()

