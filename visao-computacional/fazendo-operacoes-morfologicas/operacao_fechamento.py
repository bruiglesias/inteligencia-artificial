import cv2
import numpy as np

# -*- coding: utf-8 -*-
#
# Programa: reduz ruidos com pontos pretos em objeto branco com fundo 
# na cor preta
#
# Autor: Bruno P. Iglesia


imagemOriginal = cv2.imread("imagem-ruido-interno.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.morphologyEx(imagemOriginal, cv2.MORPH_CLOSE, elementoEstruturante)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()