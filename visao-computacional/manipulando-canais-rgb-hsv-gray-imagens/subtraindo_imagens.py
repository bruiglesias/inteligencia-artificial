# -*- coding: utf-8 -*-
#
# Programa: Subtrai duas imagens, ideal para rastreio de objetos.
#
# Autor: Bruno P. Iglesias


import cv2

imagemObjetoPosicao1 = cv2.imread("objeto-posicao-1.bmp")
imagemObjetoPosicao2 = cv2.imread("objeto-posicao-2.bmp")

imagem = cv2.subtract(imagemObjetoPosicao1, imagemObjetoPosicao2)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()