import os

import cv2


def resize():
    count = 1
    for file_type in ['target']:
        for img in os.listdir(file_type):
            try:
                current_image_path = str(file_type) + '/' + str(img)
                imgggg = cv2.imread(current_image_path, cv2.IMREAD_GRAYSCALE)
                resided_image = cv2.resize(imgggg, (25, 50))
                cv2.imwrite("target/" + "25_50_" + str(count) + ".png", resided_image)
                count += 1
            except Exception as e:
                print(str(e))


resize()
