# -*- coding: utf-8 -*-
#
# Programa: Carrega uma imagem e faz uma mudança de pespectiva nela
# mudando de uma visao inclinada para uma visao de cima para baixo.
#
# Autor: Bruno P. Iglesias

import cv2
import numpy as np

imagemOriginal = cv2.imread("imagem.jpeg")

pontosIniciais = np.float32([[189,87], [459,84], [192,373], [484,372]])
pontosFinais = np.float32([[0,0], [500,0], [0,500], [500,500]])
matriz = cv2.getPerspectiveTransform(pontosIniciais, pontosFinais)
imagemModificada = cv2.warpPerspective(imagemOriginal, matriz, (500, 500))

cv2.imshow("Imagem Original", imagemOriginal)
cv2.imshow("Imagem Modificada", imagemModificada)

cv2.waitKey(0)
cv2.destroyAllWindows()