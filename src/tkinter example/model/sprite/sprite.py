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

        tempPath = path

        costumes = []

        os.mkdir(tempPath + "/Sprite")

        # path = path + "/Sprite"
        index_in_list = 0

        for i in self.list_costumes:

            if i.costume_name == "":
                i.costume_name = self.sprite_name

            item = {
                "name": i.costume_name + str(index_in_list),
                "bitmapResolution": 2,
                "dataFormat": "jpg",
                "assetId": i.getAssetId(),
                "md5ext": i.getAssetId() + ".jpg",
                "rotationCenterX": i.image.shape[1] / 2,
                "rotationCentery": i.image.shape[0] / 2,

            }

            costumes.append(item)

            index_in_list = index_in_list + 1

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
            "sounds": [],
            "volume": 100,
            "visible": True,
            "x": 92,
            "y": 42,
            "size": 100,
            "direction": 90,
            "draggable": False,
            "rotationStyle": "all around"
        }

        # Serializing json
        json_object = json.dumps(dictionary, indent=4)

        # Writing to sample.json
        with open(path + "/Sprite" + "/sprite.json", "w") as outfile:
            outfile.write(json_object)

        self._save_images(path + "/Sprite")

        self._zip_directory(path)

        self._delete_temp_file(path)

    def _save_images(self, path):

        for i in self.list_costumes:
            new_path = path + "/" + i.getAssetId() + ".jpg"
            cv2.imwrite(new_path, i.image)

    def _zip_directory(self, path):

        with zipfile.ZipFile(path + "/Sprite.sprite3", 'w') as zipObj:

            for folderName, subfolders, filenames in os.walk(path + "/Sprite"):
                for filename in filenames:
                    zipObj.write(path + "/Sprite/" + filename, filename)

    def _delete_temp_file(self, path):
        shutil.rmtree(path + "/Sprite")
