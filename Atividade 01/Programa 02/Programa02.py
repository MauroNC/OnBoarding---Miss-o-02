# Capturar e Exibir Imagens da Webcam

import cv2

# Capturar imagem da webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Erro ao abrir a webcam.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Erro ao capturar a imagem da webcam.")
            break

        # Exibir a imagem da webcam
        cv2.imshow('Imagem da Webcam', frame)

        # Verificar se o usuário pressionou 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    # Definir o caminho e nome do arquivo para salvar a imagem
    caminho_arquivo = 'imagem_webcam.jpg'
    #não entendi direito, mas ao colocar somenta o nome tipo imagem.png, ele salva no local onde esta o prompt
            
    # Salvar a imagem capturada
    cv2.imwrite(caminho_arquivo, frame)
    print(f"Imagem salva em: {caminho_arquivo}")
            

        
    # Liberar a captura
    cap.release()
    cv2.destroyAllWindows()

