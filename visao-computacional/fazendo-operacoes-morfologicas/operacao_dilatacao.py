# -*- coding: utf-8 -*-
#
# Programa: Faz uma operação de dilatação sobre a imagem, a operação de 
# dilatação 'engrossa' objetos de cor branca em um fundo preto.
#
# Autor: Bruno P. Iglesia

import cv2
import numpy as np

imagemOriginal = cv2.imread("imagem.bmp", 0)
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.dilate(imagemOriginal, elementoEstruturante, iterations = 2)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()