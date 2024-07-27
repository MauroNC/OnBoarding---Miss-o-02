# Conversão de Imagem para HSV

import cv2

# Carregar a imagem
imagem = cv2.imread('caminho/para/imagem.jpg')

# Converter a imagem para o espaço de cor HSV
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Exibir a imagem em HSV
cv2.imshow('Imagem em HSV', imagem_hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
