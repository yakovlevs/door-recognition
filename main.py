import cv2
import sys

imagePath = sys.argv[1]
cascadePath = sys.argv[2]

doorCascade = cv2.CascadeClassifier(cascadePath)

image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

doors = doorCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(25, 50),
    flags=cv2.CASCADE_SCALE_IMAGE
)

print("Found {0} doors!".format(len(doors)))

for (x, y, w, h) in doors:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv2.imshow("Door found", image)
cv2.waitKey(0)
