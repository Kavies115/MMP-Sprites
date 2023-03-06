# me - this DAT
# scriptOp - the OP which is cooking

import numpy as np
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    enable_segmentation=True
)


cap = cv2.VideoCapture(0)


s, image = cap.read()
if image is not None:
    image = cv2.cvtColor(image, cv2.COLOR_RGBA2RGB)
    image *= 255
    image = image.astype('uint8')
    results = pose.process(image)
    cv2.imshow('office',image)

    if results.segmentation_mask is not None:
        rgb = cv2.cvtColor(results.segmentation_mask, cv2.COLOR_GRAY2RGB)
        rgb = rgb * 255
        rgb = rgb.astype(np.uint8)
        cv2.imshow('office', image)

