# -*- coding: utf-8 -*-
#
# Programa: segmenta o objeto e envolve-o em um circulo
#
# Autor: Bruno P. Iglesias

import cv2
import numpy as np

imagemRGB = cv2.imread("puzzle.bmp")
imagemTonsDeCinza = cv2.imread("puzzle.bmp", 0)

tipo = cv2.THRESH_BINARY
ret, imgBinarizada = cv2.threshold(imagemTonsDeCinza, 127, 255, tipo)

modo = cv2.RETR_TREE;
metodo = cv2.CHAIN_APPROX_SIMPLE;

contornos, hierarquia = cv2.findContours(imgBinarizada, modo, metodo)

objeto = contornos[0]

# Obtendo o ponto central e raio da circunferencia
(x,y), raio = cv2.minEnclosingCircle(objeto)

centro = (int(x), int(y))
raio = int(raio)

# Desenhando a circunferencia na imagem imagemRGB
cv2.circle(imagemRGB, centro, raio, (0, 255, 0), 2)

cv2.imshow("Circunferencia Envolvente", imagemRGB)

print(x, y, raio)

cv2.waitKey(0)
cv2.destroyAllWindows()