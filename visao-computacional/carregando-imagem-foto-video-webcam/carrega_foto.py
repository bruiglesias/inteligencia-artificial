# -*- coding: utf-8 -*-
#
# Programa: Carrega um foto de um arquvo para o programa utilizando
# opencv e o exibe em uma janela.
#
# Autor: Bruno P. Iglesias

import cv2

imagem = cv2.imread("imagem.jpg")
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

