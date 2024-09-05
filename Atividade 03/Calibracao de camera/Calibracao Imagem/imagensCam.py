import cv2

#Inicializa a captura de video e o contador de imagens salvas
cap = cv2.VideoCapture(0)
num = 0

# Loop infinito para capturar imagens
while cap.isOpened():
    ret, img = cap.read()
    if not ret:
        break

    cv2.imshow('Img', img) # Exibe o Video em uma janela

    k = cv2.waitKey(1) & 0xFF 

    if k == 27:  # Pressionar a tecla 'esc' para sair do loop
        break
    elif k == ord('s'):  # Pressionar a tecla 's' para salvar a imagem
        cv2.imwrite('imagem' + str(num) + '.png', img)
        print("image salva!")
        num += 1
    else:
        print("Tecla pressionada invalida. Pressione 'esc' para sair ou 's' para salvar.")

# Libera a captura de video e fecha todas as janelas
cap.release()
cv2.destroyAllWindows()