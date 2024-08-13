import cv2

# Carregar as imagens
img_com_carros = cv2.imread('D:\seubi\Documents\RAS\OnBoarding_Missao_02\Atividade 02\Imagens - Atividade 02\Tarefa-01\street-01.jpg')
img_sem_carros = cv2.imread('D:\seubi\Documents\RAS\OnBoarding_Missao_02\Atividade 02\Imagens - Atividade 02\Tarefa-01\street-00.jpg')

# Subtração entre as imagens
diferenca = cv2.absdiff(img_com_carros, img_sem_carros)

# Conversão para escala de cinza
diferenca_gray = cv2.cvtColor(diferenca, cv2.COLOR_BGR2GRAY)

# Aplicação de threshold
_, binarizada = cv2.threshold(diferenca_gray, 50, 255, cv2.THRESH_BINARY)

# Detecção de contornos
contornos, _ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar contornos na imagem original
resultado = img_com_carros.copy()
for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    cv2.rectangle(resultado, (x, y), (w+x, h+y), (0, 255, 0), 2)

# Exibir o resultado
cv2.imshow('Detecção de Carros', resultado)

#teste imagem
cv2.imshow('Rua com carro',img_com_carros)
cv2.imshow('Rua sem carro',img_sem_carros)
cv2.waitKey(0)
cv2.destroyAllWindows()
