import glob
import json
import os
import shutil
import zipfile
from asyncio.windows_events import NULL

import cv2
from PIL.Image import Image


class Sprite:
    _sprite_name = "Sprite"
    _list_costumes = []

    '''Adds costume to the Sprite'''
    def add_costume(self, costume):
        self._list_costumes.append(costume)

    '''Removes costume from the list of costumes'''
    def remove_costume(self, costume):
        self._list_costumes.remove(costume)

    '''Clears the costumes in the list'''
    def clear_costumes(self):
        self._list_costumes.clear()

    '''Returns list of costumes'''
    def get_list_costumes(self):
        return self._list_costumes

    '''shows all the costumes one by one (for testing)'''
    def print_costumes(self):
        for x in self._list_costumes:
            cv2.imShow(x)
            cv2.waitKey(0)

    '''search list to find the costume and returns its location'''
    def find_costume(self, costume):
        return self._list_costumes.index(costume)

    ''':return the sprites name'''
    def get_sprite_name(self):
        return self._sprite_name

    '''Changes the name of the Sprite'''
    def set_sprite_name(self, name):
        self._sprite_name = name

    '''Exports the sprite and costumes into a .sprite3 format'''
    def export(self, path):

        tempPath = path
        costumes = []

        # Create a temp folder to put the json and imgs inside
        os.mkdir(tempPath + "/" + self._sprite_name)

        index_in_list = 0

        # For each costume we create an item in the JSON for it
        for i in self._list_costumes:

            # if the costume has no name create one based on sprite name
            if i._costume_name == "":
                i._costume_name = self._sprite_name + str(index_in_list)


            item = {
                "name": i._costume_name,
                "bitmapResolution": 2,
                "dataFormat": "jpg",
                "assetId": i.getAssetId(),
                "md5ext": i.getAssetId() + ".jpg",
                "rotationCenterX": i.image.shape[1] / 2,
                "rotationCentery": i.image.shape[0] / 2,

            }

            costumes.append(item)

            index_in_list = index_in_list + 1

        # taget json
        dictionary = {
            "isStage": False,
            "name": self._sprite_name,
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": {},
            "comments": {},
            "currentCostume": 0,
            "costumes": costumes, # all the costumes get added here
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

        # Writing to sprite.json (Target JSON)
        with open(path + "/" + self._sprite_name + "/sprite.json", "w") as outfile:
            outfile.write(json_object)

        # Save all the imgs to the tmp file
        self._save_images(path + "/" + self._sprite_name)
        # Compress the file and place in the same directory
        self._zip_directory(path)
        # delete the temp folder
        self._delete_temp_file(path)

    '''Saves the IMGs of the costumes to a file path'''
    def _save_images(self, path):

        for i in self._list_costumes:
            new_path = path + "/" + i.getAssetId() + ".jpg"
            cv2.imwrite(new_path, i.image)

    '''Compress the folder directory as a ZIP and rename to end with .sprite3'''
    def _zip_directory(self, path):

        with zipfile.ZipFile(path + "/" + self._sprite_name + ".sprite3", 'w') as zipObj:

            for folderName, subfolders, filenames in os.walk(path + "/" + self._sprite_name):
                for filename in filenames:
                    zipObj.write(path + "/" + self._sprite_name + "/" + filename, filename)

    '''Delete the temp file created'''
    def _delete_temp_file(self, path):
        shutil.rmtree(path + "/" + self._sprite_name)
