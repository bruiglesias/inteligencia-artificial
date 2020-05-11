# -*- coding: utf-8 -*-
#
# Programa: gera a moda estatística das cores das imagens
#
# Autor: Bruno P. Iglesia

import cv2
import statistics

imgBinaria = cv2.imread("tampa-binaria.png", 0)
imgTonsDeCinza = cv2.imread("tampa-cinza.png", 0)

rolBinaria = imgBinaria.ravel()
rolTonsDeCinza = imgTonsDeCinza.ravel()

print(statistics.mode(rolBinaria))
print(statistics.mode(rolTonsDeCinza))