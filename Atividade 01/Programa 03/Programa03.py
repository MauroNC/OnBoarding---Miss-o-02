# Analisar e Exibir Dimensões das Imagens

import cv2

# Carregar a imagem
imagem = cv2.imread('caminho/para/imagem.jpg/png')

# Obter as dimensões da imagem
altura, largura, canais = imagem.shape
print(f'Dimensões da imagem: {altura}x{largura}x{canais}')

# Exibir a imagem original
cv2.imshow('Imagem Original', imagem)

# Converter a imagem para escala de cinza
imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
altura_cinza, largura_cinza = imagem_cinza.shape
print(f'Dimensões da imagem em escala de cinza: {altura_cinza}x{largura_cinza}')

# Exibir a imagem em escala de cinza
cv2.imshow('Imagem em Escala de Cinza', imagem_cinza)
cv2.waitKey(0)
cv2.destroyAllWindows()
