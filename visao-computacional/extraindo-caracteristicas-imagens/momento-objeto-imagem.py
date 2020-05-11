# -*- coding: utf-8 -*-
#
# Programa: obtem o momento do objto da imagem
#
# Autor: Bruno P. Iglesis



import cv2
import numpy as np

imagem = cv2.imread("quadrado.bmp", 0)
momentos = cv2.moments(imagem)

print(momentos)