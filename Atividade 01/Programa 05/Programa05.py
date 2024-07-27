# Redimensionamento e Transformações de Imagem

import cv2

# Carregar a imagem
imagem = cv2.imread('caminho/para/imagem.jpg')

# Obter as dimensões da imagem
altura, largura, canais = imagem.shape

# Redimensionar a imagem
imagem_redimensionada = cv2.resize(imagem, (largura//2, altura//2))
cv2.imshow("Imagem Redimensionada", imagem_redimensionada)

# Aumentar o brilho da imagem
imagem_brilho = cv2.convertScaleAbs(imagem, alpha = .5, beta= 25)
cv2.imshow("Imagem com Brilho", imagem_brilho)

cv2.waitKey(0)
cv2.destroyAllWindows()