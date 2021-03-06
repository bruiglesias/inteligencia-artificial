# -*- coding: utf-8 -*-
#
# Programa: Detector de bordas canny
#
# Autor: Bruno P. Iglesia

import cv2

imgOriginal = cv2.imread("imagem.jpeg", 0)
imgTratada = cv2.Canny(imgOriginal, 100, 200)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)

cv2.waitKey(0)
cv2.destroyAllWindows()