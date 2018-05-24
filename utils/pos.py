import urllib.request
import cv2
import os
import socket

# timeout in seconds
timeout = 1
socket.setdefaulttimeout(timeout)


def store_raw_images():
    neg_images_link = open('_pos.txt', 'r')
    neg_image_urls = neg_images_link.read()
    pic_num = 1

    if not os.path.exists('pos'):
        os.makedirs('pos')

    for i in neg_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "pos/" + str(pic_num) + ".jpg")
            img = cv2.imread("pos/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
            # should be larger than samples / pos pic (so we can place our image on it)
            resized_image = cv2.resize(img, (50, 50))
            cv2.imwrite("pos/" + str(pic_num) + ".jpg", resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))


store_raw_images()
