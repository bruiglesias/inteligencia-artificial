# -*- coding: utf-8 -*-
#
# Programa: Separa a imagens em seus canais RGB, salva em arquivos
# separados, em seguidar une novamente os canais formando a imagem original.
#
# Autor: Bruno P. Iglesias


import cv2

# Carregando imagem RGB e segmentando canais
imagem = cv2.imread("imagem.jpeg")
azul, verde, vermelho = cv2.split(imagem)

# Exibindo imagens dos canais separados
cv2.imshow("Canal R", vermelho)
cv2.imshow("Canal G", verde)
cv2.imshow("Canal B", azul)

# Salvando imagens dos canais separados
cv2.imwrite("imagem-canal-vermelho.jpeg", vermelho)
cv2.imwrite("imagem-canal-verde.jpeg", verde)
cv2.imwrite("imagem-canal-azul.jpeg", azul)

# Combinando os tres canais em uma unica imagem
imagem = cv2.merge((azul, verde, vermelho))
cv2.imshow("Imagem", imagem)

cv2.waitKey(0)
cv2.destroyAllWindows()

