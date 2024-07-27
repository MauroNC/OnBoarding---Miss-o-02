# Carregar e Exibir Imagem do disco

import cv2

# Caminho para a imagem
caminho_imagem = 'caminho/para/imagem.jpg/png'

# Carregar uma imagem do disco
imagem = cv2.imread(caminho_imagem)
if imagem is not None:
    cv2.imshow('Imagem Carregada', imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Erro ao carregar a imagem.")
