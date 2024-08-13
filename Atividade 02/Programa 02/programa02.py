import cv2

# Carregar as imagens
img_referencia = cv2.imread('D:\seubi\Documents\RAS\OnBoarding_Missao_02\Atividade 02\Imagens - Atividade 02\Tarefa-02\porta1.jpg')
img_atual = cv2.imread('D:\seubi\Documents\RAS\OnBoarding_Missao_02\Atividade 02\Imagens - Atividade 02\Tarefa-02\kirra1.jpg')

# Subtração de fundo
diferenca = cv2.absdiff(img_atual, img_referencia)

# Converter para escala de cinza
diferenca_gray = cv2.cvtColor(diferenca, cv2.COLOR_BGR2GRAY)

# Aplicar blur para reduzir ruídos
blur = cv2.GaussianBlur(diferenca_gray, (5, 5), 0)

# Aplicar threshold para binarizar a imagem
_, binarizada = cv2.threshold(blur, 50, 255, cv2.THRESH_BINARY)

# Detectar contornos
contornos, _ = cv2.findContours(binarizada, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Desenhar contornos e verificar características
resultado = img_atual.copy()
for contorno in contornos:
    x, y, w, h = cv2.boundingRect(contorno)
    # Definir um tamanho mínimo para considerar um contorno como um possível intruso
    if w > 50 and h > 50:  
        cv2.rectangle(resultado, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(resultado, "Intruso!", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

# Mostrar a imagem resultante
cv2.imshow('Deteccao de Intrusos', resultado)
cv2.waitKey(0)
cv2.destroyAllWindows()