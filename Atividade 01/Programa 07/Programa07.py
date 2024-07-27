# Thresholding
#

import cv2

# Carregar a imagem
imagem_cinza = cv2.imread('imagem_webcam.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicação do regular thresholding
thresholding_regular = cv2.threshold(imagem_cinza, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('Regular thresholding', thresholding_regular)

# Aplicação do adaptive thresholding
thresholding_adaptive = cv2.adaptiveThreshold(imagem_cinza, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
cv2.imshow('Adaptive thresholding', thresholding_adaptive)

cv2.waitKey(0)
cv2.destroyAllWindows()