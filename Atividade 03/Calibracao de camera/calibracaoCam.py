import cv2
import numpy as np

# Defina as dimensões do tabuleiro de xadrez (número de cantos internos)
nx = 7  # Número de cantos internos na direção x
ny = 5  # Número de cantos internos na direção y

# Inicialize a captura de vídeo
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Erro ao acessar a câmera.")
    exit()

# Definir critérios para aprimorar a precisão dos cantos
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

while True:
    # Capturar frame da câmera
    ret, frame = cap.read()

    if not ret:
        print("Falha ao capturar imagem da câmera.")
        break

    # Converter para escala de cinza
    grayscale_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Tente encontrar os cantos do tabuleiro de xadrez
    ret, corners = cv2.findChessboardCorners(grayscale_frame, (nx, ny), None)

    if ret:
        # Aprimorar os cantos detectados
        corners_refined = cv2.cornerSubPix(grayscale_frame, corners, (11, 11), (-1, -1), criteria)

        # Desenhar os cantos na imagem
        cv2.drawChessboardCorners(frame, (nx, ny), corners_refined, ret)
        cv2.putText(frame, "Cantos encontrados!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA) 
    else:
        cv2.putText(frame, "Cantos nao encontrados.", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    # Mostrar a imagem com o resultado
    cv2.imshow('Detecção de Chessboard', frame)

    # Sair do loop ao pressionar 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar a câmera e fechar as janelas
cap.release()
cv2.destroyAllWindows()
