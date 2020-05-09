# -*- coding: utf-8 -*-
#
# Programa: Exemplo processo de equalização de histograma, programa
# carrega uma imagem e aplica o processo de equalização de histograma
# em seguida exibe os histogramas da imagem original e equalizada.
#
# Autor: Bruno P. Iglesias


import cv2
import numpy as np
from matplotlib import pyplot as grafico

imagemOriginal = cv2.imread("imagem.jpg", 0)
imagemEqualizada = cv2.equalizeHist(imagemOriginal)

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Equalizada", imagemEqualizada)

grafico.hist(imagemOriginal.ravel(), 256, [0,256])

grafico.figure();
grafico.hist(imagemEqualizada.ravel(), 256, [0,256])

grafico.show()