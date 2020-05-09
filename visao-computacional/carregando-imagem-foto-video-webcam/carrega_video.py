# -*- coding: utf-8 -*-
#
# Programa: Carrega um video de um arquvo para o programa utilizando
# opencv e o exibe-o em uma janela.
#
# Autor: Bruno P. Iglesias

import cv2

captura = cv2.VideoCapture("video.mp4")

while True:
  ret, frame = captura.read()
  cv2.imshow("Imagem", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

captura.release()
cv2.destroyAllWindows()