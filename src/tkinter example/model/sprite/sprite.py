import glob
import json
import os
import shutil
import zipfile
from asyncio.windows_events import NULL

import cv2
from PIL.Image import Image


class Sprite:
    sprite_name = ""
    list_costumes = []

    def add_list_img(self, img):
        self.list_costumes.append(img)

    def remove_list_img(self, img):
        self.list_costumes.remove(img)

    def clear_list_img(self):
        self.list_costumes.clear()

    def print_list_img(self):
        for x in self.list_costumes:
            cv2.imShow(x)
            cv2.waitKey(0)

    def export(self, path):

        costumes = []

        os.mkdir(path + "/Sprite")

        # path = path + "/Sprite"

        for i in self.list_costumes:

            if i.costume_name == "":
                i.costume_name = self.sprite_name

            item = {
                "name": i.costume_name,
                "bitmapResolution": 1,
                "dataFormat": "png",
                "assetId": i.assetId,
                "md5ext": i.assetId + ".png",
                "rotationCenterX": 64,
                "rotationCentery": 64,

            }

            costumes.append(item)

        dictionary = {
            "isStage": False,
            "name": self.sprite_name,
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": costumes,
            "sounds": []
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent=4)

        # Writing to sample.json
        with open(path + "/Sprite" + "/sprite.json", "w") as outfile:
            outfile.write(json_object)

        self._save_images(path + "/Sprite")

        self._zip_directory(path)

    def _save_images(self, path):

        for i in self.list_costumes:
            new_path = path + "/" + i.assetId + ".png"
            cv2.imwrite(new_path, i.image)

    def _zip_directory(self, path):
        path = path

