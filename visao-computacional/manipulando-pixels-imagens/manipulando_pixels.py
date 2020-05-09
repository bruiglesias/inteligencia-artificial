# -*- coding: utf-8 -*-
#
# Programa: Exemplos de operações sobre pixels de imagens
#
# Autor: Bruno P. Iglesias


import cv2

# imprime o valor do pixel localizando na linha 150 e coluna 150
# da imagem
imagem = cv2.imread("imagem.jpeg")
valorPixel = imagem[150,150]
print(valorPixel)

# converte para escala de cinza e exibe o novo valor do pixel acima
imagem = cv2.cvtColor(imagem, cv2.COLOR_RGB2GRAY)
valorPixel = imagem[150,150]
print(valorPixel)


# carrega novamente a imagem
imagem = cv2.imread("imagem.jpeg")

# valor do pixel em determinado canal RGB
valorPixel = imagem[150,150,0]
print(valorPixel)

# altera o valor RGB de um determinado pixel
imagem[150,150] = [255,255,255] 
print(imagem[150,150])

# imprime o numero de linhas, colunas e canais da imagem
print(imagem.shape)

# imprime o total de pixels da imagem
print(imagem.size)

# conta o total de pixels pretos e branco de uma imagem binária
# supondo-se que a imagem possui dimensões 500x500
imagem = cv2.imread("imagem-binaria.bmp", 0)
totalPixelsPreto = 0;
totalPixelsBranco = 0;

for x in range(0, 499):
  for y in range(0, 499):
    if imagem[x,y] == 255:
      totalPixelsBranco += 1;
    else:
      totalPixelsPreto += 1;

print(totalPixelsBranco)
print(totalPixelsPreto)

