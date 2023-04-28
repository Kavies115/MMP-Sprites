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

        BG_COLOR = (255, 255, 255)  # white

        with self.mp_pose.Pose(
                min_detection_confidence=0.65,
                min_tracking_confidence=0.55,
                enable_segmentation=True,
                smooth_segmentation=True) as pose:

            image_to_annotate = image

            cv2.resize(image_to_annotate, (400, 400))


            # some of this code was taken and modified from https://google.github.io/mediapipe/solutions/pose.html


            results = pose.process(image_to_annotate)

            segmented_image = image_to_annotate.copy()

            try:

                # take the segmented mask and convert it into a way NumPy can understand
                mask = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.14

                self._bg_image = np.zeros(segmented_image.shape, dtype=np.uint8)
                self._bg_image[:] = BG_COLOR
                segmented_image = np.where(mask, segmented_image, self._bg_image)

                return True, segmented_image

            except:
                return False, image
