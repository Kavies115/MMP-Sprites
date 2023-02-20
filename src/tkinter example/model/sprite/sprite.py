import cv2


class Sprite:

    sprite_name = ""

    def __init__(self, list_costumes):
        self.list_costumes = list_costumes

    def add_list_img(self, img):
        self.list_costumes.append(img)

    def remove_list_img(self, img):
        self.list_costumes.remove(img)

    def print_list_img(self):
        for x in self.list_costumes:
            cv2.imShow(x)
            cv2.waitKey(0)

    def export(self):

