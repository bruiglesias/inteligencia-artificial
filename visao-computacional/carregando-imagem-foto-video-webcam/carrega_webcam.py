# -*- coding: utf-8 -*-
#
# Programa: Carrega da webcam para o programa utilizando
# opencv e o exibe-o em uma janela.
#
# Autor: Bruno P. Iglesias

import cv2

# 0 é o index da webcam instalada no computador
captura = cv2.VideoCapture(0)

while True:
  ret, frame = captura.read()
  cv2.imshow("Imagem", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

captura.release()
cv2.destroyAllWindows()