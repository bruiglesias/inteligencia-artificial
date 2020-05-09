# -*- coding: utf-8 -*-
#
# Programa: redimensiona a imagem reduzindo-a pela metade.
#
# Autor: Bruno P. Iglesias


import cv2
import numpy as np

imagemOriginal = cv2.imread("imagem.jpeg")

imagemModificada = cv2.resize(imagemOriginal, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)

cv2.imshow("Resultado", imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()