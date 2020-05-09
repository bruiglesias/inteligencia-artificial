# -*- coding: utf-8 -*-
#
# Programa: Faz a soma ponderada de duas imagens.
#
# Autor: Bruno P. Iglesias

import cv2

imagem1 = cv2.imread("imagem1.bmp")
imagem2 = cv2.imread("imagem2.bmp")

imagem = cv2.addWeighted(imagem1, 0.2, imagem2, 1.0, 0)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()