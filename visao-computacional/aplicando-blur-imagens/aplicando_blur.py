# -*- coding: utf-8 -*-
#
# Programa: Apresenta algumas formas de aplicação de blur em imagens
#
# Autor: Bruno P. Iglesias

import cv2

# forma 1: aplicação do blur do opencv
imgOriginal = cv2.imread("imagem.jpeg")
imgTratada = cv2.blur(imgOriginal, (5,5))

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)


# forma 2: aplicação de blur gaussiano
imgOriginal = cv2.imread("imagem.jpeg")
imgTratada = cv2.GaussianBlur(imgOriginal, (5,5), 0)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)


# forma 3: aplicacao do blur mediano
imgOriginal = cv2.imread("moedas.jpeg")
imgTratada = cv2.medianBlur(imgOriginal, 5)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)


# forma 4: aplicando filtro bilateral
imgOriginal = cv2.imread("moedas.jpeg")
imgTratada = cv2.bilateralFilter(imgOriginal, 9, 75, 75)

cv2.imshow("Original", imgOriginal)
cv2.imshow("Tratada", imgTratada)


cv2.waitKey(0)
cv2.destroyAllWindows()