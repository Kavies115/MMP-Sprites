#    Copyright (c) 2022
#    Author      : Bruno Capuano
#    Create Time : 2022 June
#    Change Log  :
#    – Open a local camera feed using OpenCV
#    – Show the original camera feed and the background removed feed
#
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining a copy
#    of this software and associated documentation files (the "Software"), to deal
#    in the Software without restriction, including without limitation the rights
#    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#    copies of the Software, and to permit persons to whom the Software is
#    furnished to do so, subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be included in
#    all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#    THE SOFTWARE.

import cv2
import cvzone
import mediapipe as mp
from cvzone.SelfiSegmentationModule import SelfiSegmentation

segmentor = SelfiSegmentation()

# open camera
cap = cv2.VideoCapture(0)

while True:
    # read image
    ret, img = cap.read()

    #resize office to 640×480
    img = cv2.resize(img, (320, 240))
    green = (0, 255, 0)
    imgNoBg = segmentor.removeBG(img, green, threshold=0.35)

    # show both images
    cv2.imshow('office',img)
    cv2.imshow('office no bg',imgNoBg)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# close camera
cap.release()
cv2.destroyAllWindows()