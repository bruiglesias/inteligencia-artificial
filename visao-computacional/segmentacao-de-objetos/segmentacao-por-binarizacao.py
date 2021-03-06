# -*- coding: utf-8 -*-
#
# Programa: segmenta a imagem por binarização 
#
# Autor: Bruno P. Iglesia

import cv2
import numpy as np

imgOriginal = cv2.imread("imagem.png", 0)

metodo = cv2.THRESH_BINARY_INV
ret, imgBinarizada = cv2.threshold(imgOriginal, 135, 255, metodo)

cv2.imshow("Imagem Original", imgOriginal)
cv2.imshow("Imagem Tratada", imgBinarizada)

cv2.waitKey(0)
cv2.destroyAllWindows()