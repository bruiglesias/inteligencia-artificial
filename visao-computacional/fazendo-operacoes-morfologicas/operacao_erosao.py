# -*- coding: utf-8 -*-
#
# Programa: Faz uma operação de erosão sobre a imagem, a operação de 
# erosão afina objetos de cor branca em um fundo preto.
#
# Autor: Bruno P. Iglesia

import cv2
import numpy as np

imagemOriginal = cv2.imread("imagem.bmp", 0)
# usar MORPH_ELLIPSE se o objeto branco for redondo
elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
imagemProcessada = cv2.erode(imagemOriginal, elementoEstruturante, iterations = 2)

cv2.imshow("Original", imagemOriginal)
cv2.imshow("Resultado", imagemProcessada)

cv2.waitKey(0)
cv2.destroyAllWindows()