import hashlib
import os
import unittest

import cv2

from sprite.costume import Costume


class CostumeTest(unittest.TestCase):
    def test_set_costume_name(self):
        img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")

        costume = Costume(img)
        costume.set_costume_name("costume 1")

        self.assertEqual(costume.get_costume_name(), "costume 1")

    def test_set_costume_name_long(self):
        img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")

        costume = Costume(img)
        costume.set_costume_name("abcdefghijklmnopqrstuvwxyz0123456789")

        self.assertEqual("abcdefghijklmnopqrstuvwxy", costume.get_costume_name())

    def test_set_costume_name_no_char(self):
        img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")

        costume = Costume(img)
        costume.set_costume_name("")

        self.assertEqual("", costume.get_costume_name())

    def test_set_costume_name_didnt_set_name(self):
        img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")

        costume = Costume(img)

        self.assertEqual("", costume.get_costume_name())

    def test_get_assetID(self):
        img = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")

        costume = Costume(img)

        hashcode = hashlib.md5(img.tobytes()).hexdigest()

        self.assertEqual(hashcode, costume.get_costume_assetId())