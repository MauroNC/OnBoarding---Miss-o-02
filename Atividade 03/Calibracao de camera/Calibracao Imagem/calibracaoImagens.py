
import cv2
import numpy as np
import glob

# Defina as dimensões do tabuleiro de xadrez (número de quadrados internos)
nx = 7  # número de cantos internos na direção x
ny = 5  # número de cantos internos na direção y

# Leia as imagens capturadas
image = glob.glob('local/dos/arquivos/*.png')
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Tente encontrar os cantos do tabuleiro de xadrez
ret, corners = cv2.findChessboardCorners(grayscale_image, (nx, ny), None)

if ret:
    print("Cantos encontrados!")
    # Desenhar os cantos na imagem
    cv2.drawChessboardCorners(image, (nx, ny), corners, ret)
    cv2.imshow('Chessboard com Cantos', image)
    cv2.waitKey(0)
else:
    print("Não foi possível encontrar os cantos.")
    cv2.imshow('Imagem', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()


