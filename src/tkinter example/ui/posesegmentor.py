import cv2
import mediapipe as mp
import numpy as np

class PoseSegmentor:

    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self._bg_image = None

    '''Takes img of the webcam as a input trys to find a person and then segments the img around them returns weather 
    it worked and an image'''
    def image_segmentor(self, image):
        with self.mp_pose.Pose(
                min_detection_confidence=0.65,
                min_tracking_confidence=0.65,
                enable_segmentation=True,
                smooth_segmentation=True) as pose:

            image_to_annotate = image

            cv2.resize(image_to_annotate, (400, 400))

            BG_COLOR = (255, 255, 255)  # white

            # Alot of this code was taken and modified from https://google.github.io/mediapipe/solutions/pose.html


            results = pose.process(image_to_annotate)


            annotated_image = image_to_annotate.copy()

            try:

                #annotated_image = cv2.cvtColor(annotated_image, cv2.COLOR_RGB2RGBA)

                # find where the image needs to be segmentated
                condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.14

                self._bg_image = np.zeros(annotated_image.shape, dtype=np.uint8)
                self._bg_image[:] = BG_COLOR
                annotated_image = np.where(condition, annotated_image, self._bg_image)

                return True, annotated_image

            except:
                return False, image