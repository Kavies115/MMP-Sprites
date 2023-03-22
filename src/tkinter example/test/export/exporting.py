import unittest
import cv2
import os
from sprite.costume import Costume
from sprite.sprite import Sprite


class CostumeTest(unittest.TestCase):

    # def test_add_img_to_costume(self):
    #     path = os.path.realpath("resource/testing/walter1.png")
    #
    #     img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
    #
    #
    #
    #     costume = Costume(img)
    #
    #
    #     cv2.imshow("office", costume.img)
    #
    #     cv2.waitKey(0)
    #
    #     print("hello")


    # def test_add_not_img_to_costume(self):
        # path = os.path.realpath("resource/testing/walter1.png")
        #
        # img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter4.png")
        #
        # costume = Costume(img)
        #
        # cv2.imshow("office", costume.img)
        #
        # print("hello")

    def test_export_test(self):
        img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter4.png")

        c1 = Costume(img)
        c1.assetId = "walter1"

        s1 = Sprite()
        s1.sprite_name = "Walter"

        s1.add_costume(c1)

        s1.export("C:\\Users\\Kavie\\Desktop\\testting")
