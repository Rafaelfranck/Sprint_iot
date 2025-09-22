import cv2
import time
import os

# garante que a pasta data existe
if not os.path.exists("data"):
    os.makedirs("data")

# abre webcam
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Não consegui acessar a câmera!")
    exit()

window_name = "Haar Face Detection - Ajuste os sliders"
cv2.namedWindow(window_name)

# cria sliders (trackbars)
cv2.createTrackbar("scaleFactor x100", window_name, 110, 200, lambda v: None)  # 1.10..2.00
cv2.createTrackbar("minNeighbors", window_name, 5, 20, lambda v: None)         # 0..20
cv2.createTrackbar("minSize(px)", window_name, 60, 300, lambda v: None)        # 1..300

# carrega Haar Cascade padrão
cascade_path = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascade_path)

prev_time = time.time()
frames, fps = 0, 0.0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frames += 1
    now = time.time()
    if now - prev_time >= 1.0:
        fps = frames / (now - prev_time)
        prev_time, frames = now, 0

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # lê sliders
    sf_slider = cv2.getTrackbarPos("scaleFactor x100", window_name)
    scaleFactor = max(101, sf_slider) / 100.0
    minNeighbors = cv2.getTrackbarPos("minNeighbors", window_name)
    minSize = cv2.getTrackbarPos("minSize(px)", window_name)
    minSize = max(1, minSize)

    # detecção
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=scaleFactor,
        minNeighbors=minNeighbors,
        minSize=(minSize, minSize)
    )

    # desenha retângulos
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # overlay
    text = f"scale={scaleFactor:.2f} | neighbors={minNeighbors} | minSize={minSize}px | FPS={fps:.1f}"
    cv2.putText(frame, text, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow(window_name, frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('q'):  # sair
        break
    if key == ord('s'):  # snapshot
        ts = int(time.time())
        out_path = os.path.join("data", f"snapshot_{ts}.png")
        cv2.imwrite(out_path, frame)
        print(f"Snapshot salvo em {out_path}")

cap.release()
cv2.destroyAllWindows()
