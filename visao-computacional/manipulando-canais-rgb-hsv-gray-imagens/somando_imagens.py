# -*- coding: utf-8 -*-
#
# Programa: Carrega duas imagem e soma as duas dando o efeito de 
# objetos terem sido adicionados a imagem
#
# Autor: Bruno P. Iglesias

import cv2

imagem_numero_1 = cv2.imread("imagem1.bmp")
imagem_numero_2 = cv2.imread("imagem2.bmp")

imagem = cv2.add(imagem_numero_1, imagem_numero_2)

cv2.imshow("Resultado", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()