# -*- coding: utf-8 -*-
#
# Programa: gera a media estatística das cores das imagens
#
# Autor: Bruno P. Iglesi

import cv2

imgRGB = cv2.imread("tampa-rgb.jpeg")
imgTonsDeCinza = cv2.imread("tampa-tons-de-cinza.jpeg", 0)

valorMedioRGB = cv2.mean(imgRGB)
valorMedioCinza = cv2.mean(imgTonsDeCinza)

print(valorMedioRGB)
print(valorMedioCinza)