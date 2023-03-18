import cv2
import mediapipe as mp
import numpy as np


class PoseSegmentor:

    def __init__(self):
        self.mp_pose = mp.solutions.pose
        self._bg_image = None

    def image_segmentor(self, image):
        with self.mp_pose.Pose(
                min_detection_confidence=0.75,
                min_tracking_confidence=0.65,
                enable_segmentation=True,
                smooth_segmentation=True) as pose:

            BG_COLOR = (255, 255, 255)  # gray

            ## Alot of this code was taken and modified from https://google.github.io/mediapipe/solutions/pose.html
            image.flags.writeable = False
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            results = pose.process(image)

            # Draw the pose annotation on the image.
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            annotated_image = image.copy()

            try:
                # Segment the image
                condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.14

                self._bg_image = np.zeros(image.shape, dtype=np.uint8)
                self._bg_image[:] = BG_COLOR
                annotated_image = np.where(condition, annotated_image, self._bg_image)

                return annotated_image

            except:
                return annotated_image
