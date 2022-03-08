import cv2

cap = cv2.VideoCapture('.\src\carroprata6.jpg')
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int((width / 2) - 50)
    cy = int((height / 2.5) - 10)


    pixel_center = hsv_frame[cy, cx]

    

    h_value = pixel_center[0]
    s_value = pixel_center[1]
    v_value = pixel_center[2]

    if (s_value <= 20) and (v_value >= 230):
        color = "BRANCO"
    elif (v_value < 230) and (s_value <= 57):
        color = "PRATA"
    elif (v_value < 65):
        color = "PRETO"
    elif (h_value <= 7) or (h_value >= 170):
        color = "VERMELHO"
    elif (h_value >= 8) and (h_value <= 20): 
        color = "LARANJA"
    elif (h_value >= 21) and (h_value <= 35):
        color = "AMARELO"
    elif (h_value >=36) and (h_value <= 84):
        color = "VERDE"
    elif (h_value >= 85) and (h_value <= 133):
        color = "AZUL"
    elif (h_value >= 134) and (h_value <= 148):
        color = "VIOLETA"
    elif (h_value >= 149) and (h_value <= 169):
        color = "ROSA"
    else:
        color = "Nao identificado"


    pixel_center_BGR = frame[cy, cx]
    b, g, r = int(pixel_center_BGR[0]), int(pixel_center_BGR[1]), int(pixel_center_BGR[2])

    print(pixel_center)
    cv2.putText(frame, color, (10,120), 0, 1, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (0, 0, 255), 3)

    print(color)

    cv2.imshow("Display window", frame)
    key = cv2.waitKey(0)
    if key == 27:                   #fecha a imagem quando aperta ESC
        break


cap.release()
cv2.destroyAllWindows()











