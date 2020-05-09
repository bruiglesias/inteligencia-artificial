# -*- coding: utf-8 -*-
#
# Programa: Converte a imagem originalmente em RGB para escala em cinza.
#
# Autor: Bruno P. Iglesias

import cv2

# Carregando imagem em RGB
imagem = cv2.imread("imagem.jpeg")

# Convertendo e exibindo a imagem em tons de cinza
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()