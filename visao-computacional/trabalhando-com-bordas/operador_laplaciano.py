# -*- coding: utf-8 -*-
#
# Programa: Apresanta o realce de bordas utilizando o operador laplaciano.
#
# Autor: Bruno P. Iglesias

import cv2

imgOriginal = cv2.imread("imagem.jpeg", 0)
imgTratada = cv2.Laplacian(imgOriginal, cv2.CV_8U)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)


# exemplo de realce de boarda utilizando o oprador laplaciano

imgOriginal = cv2.imread("lua.jpeg", 0)
imgFiltrada = cv2.Laplacian(imgOriginal, cv2.CV_8U)
imgRealcada = cv2.subtract(imgOriginal, imgFiltrada)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Filtrada", imgFiltrada)
cv2.imshow("Realcada", imgRealcada)

cv2.waitKey(0)
cv2.destroyAllWindows()
