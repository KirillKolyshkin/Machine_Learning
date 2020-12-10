import os
import cv2
import numpy as np

base_dir = os.path.dirname(__file__) + "/"
firstPath = os.path.join(base_dir + 'deploy.prototxt')
secondPath = os.path.join(base_dir + 'weights.caffemodel')
model = cv2.dnn.readNetFromCaffe(firstPath, secondPath)

if not os.path.exists('faces'):
    os.makedirs('faces')

if not os.path.exists('images'):
    os.makedirs('images')

for file in os.listdir(base_dir + 'images'):
    file_name, file_extension = os.path.splitext(file)
    if file_extension in ['.png', '.jpg']:
        image = cv2.imread(base_dir + 'images/' + file)
        (h, w) = image.shape[:2]
        # форматируем картинку под входные данные сетки
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (500, 500)))
        model.setInput(blob)
        # список распознанных лиц
        detections = model.forward()
        # обработка каждого конткретного распознования
        for i in range(0, detections.shape[2]):
            # получаем координаты предполагаемого лица
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")
            confidence = detections[0, 0, i, 2]
            # выбираем уровень точности, по которому решаем лицо это или нет
            if confidence > 0.8:
                frame = image[startY:endY, startX:endX]
                cv2.imwrite(base_dir + 'faces/' + str(i) + '_' + file, frame)
               
# link for two files for model:
# https://github.com/opencv/opencv/blob/master/samples/dnn/face_detector/deploy.prototxt
# https://github.com/nhatthai/opencv-face-recognition/blob/master/src/face_detection_model/weights.caffemodel
