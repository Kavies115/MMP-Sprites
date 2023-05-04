import unittest

import cv2

from sprite.costume import Costume
from sprite.sprite import Sprite


class SpriteTest(unittest.TestCase):

    # def test_remove_costumes_to_sprite_list(self):
    #     img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
    #     img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
    #     img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")
    #
    #     costume1 = Costume(img1)
    #     costume1.set_costume_name("costume 1")
    #
    #     costume2 = Costume(img2)
    #     costume2.set_costume_name("costume 2")
    #
    #     costume3 = Costume(img3)
    #     costume3.set_costume_name("costume 3")
    #
    #     sprite_tmp = Sprite()
    #
    #     sprite_tmp.add_costume(costume1)
    #     sprite_tmp.add_costume(costume2)
    #     sprite_tmp.add_costume(costume3)
    #
    #     sprite_tmp.remove_costume(costume2)
    #
    #     list = [costume1, costume3]
    #
    #     self.assertEqual(list, sprite_tmp.get_list_costumes())

    def test_add_costumes_to_sprite_list(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)

        list = [costume1]

        self.assertEqual(sprite.get_list_costumes(), list)
        sprite.clear_costumes()

    def test_add_costumes_to_sprite_list_add(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)

        list = [costume1, costume2, costume3]

        sprite.add_costume(costume3)

        self.assertEqual(sprite.get_list_costumes(), list)

    def test_remove_one_costumes_to_sprite_list_add(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)
        sprite.add_costume(costume3)

        list = [costume1, costume3]

        sprite.remove_costume(costume2)


        self.assertEqual(sprite.get_list_costumes(), list)

    def test_remove_all_costumes_to_sprite_list_add(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)
        sprite.add_costume(costume3)

        list = []

        sprite.remove_costume(costume1)
        sprite.remove_costume(costume2)
        sprite.remove_costume(costume3)

        self.assertEqual(sprite.get_list_costumes(), list)

    def test_remove_and_add_costumes_to_sprite_list_add(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)

        list = [costume2, costume3]

        sprite.remove_costume(costume1)

        sprite.add_costume(costume3)

        self.assertEqual(sprite.get_list_costumes(), list)

    def test_remove_costumes_not_in_to_sprite_list_add(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)

        list = [costume1, costume2]

        sprite.remove_costume(costume3)

        self.assertEqual(sprite.get_list_costumes(), list)

    def test_clear_costumes_to_sprite_list(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        list = []

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)
        sprite.add_costume(costume3)

        sprite.clear_costumes()

        self.assertEqual(sprite.get_list_costumes(), list)

    def test_find_costumes_to_sprite_list_In_list(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)
        sprite.add_costume(costume3)

        # Should be at index 1
        self.assertEqual(sprite.find_costume(costume2), 1)

    def test_find_costumes_to_sprite_list_No_in_list(self):
        img1 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter1.png")
        img2 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter2.png")
        img3 = cv2.imread("C:\\Users\\Kavie\\Desktop\\testting\\walter3.png")

        costume1 = Costume(img1)
        costume1.set_costume_name("costume 1")

        costume2 = Costume(img2)
        costume2.set_costume_name("costume 2")

        sprite = Sprite()

        sprite.add_costume(costume1)
        sprite.add_costume(costume2)

        costume3 = Costume(img3)
        costume3.set_costume_name("costume 3")

        # If it cant find a match should return False
        self.assertEqual(sprite.find_costume(costume3), False)

    def test_sprite_name(self):
        sprite = Sprite()

        sprite.set_sprite_name("Test_Name")

        # If it cant find a match should return False
        self.assertEqual(sprite.get_sprite_name(), "Test_Name")

    def test_sprite_name_Longer_than_25_char(self):
        sprite = Sprite()

        sprite.set_sprite_name("abcdefghijklmnopqrstuvwxyz0123456789")

        # If it cant find a match should return False
        self.assertEqual(sprite.get_sprite_name(), "abcdefghijklmnopqrstuvwxy")

    def test_sprite_name_no_char(self):
        sprite = Sprite()

        sprite.set_sprite_name("")

        # If it cant find a match should return False
        self.assertEqual(sprite.get_sprite_name(), "Sprite")

    def test_sprite_name_didnt_set_name(self):
        sprite = Sprite()

        # If it cant find a match should return False
        self.assertEqual(sprite.get_sprite_name(), "Sprite")
