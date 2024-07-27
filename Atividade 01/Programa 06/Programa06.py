# Aplicação de Filtros de Blurring

import cv2

# Carregar a imagem
imagem = cv2.imread('imagem_webcam.jpg')# A imagem da minha webcam e tão ruim que o blur nem funciona
cv2.imshow('imagem', imagem)

# Regular Blurring
blur_regular = cv2.blur(imagem, (5,5))
cv2.imshow('regular blurring', blur_regular)

# Aplicar o gaussian blurring
blur_gaussian = cv2.GaussianBlur(imagem, (5,5), 0)
cv2.imshow('gaussian blurring', blur_gaussian)

cv2.waitKey(0)
cv2.destroyAllWindows()