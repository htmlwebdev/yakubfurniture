import glob
import os
import re
from PIL import Image
BASE_DIR = os.path.dirname((os.path.abspath(__file__))).replace("\\", "/")


def recursivefolders(folder_dir):
    for folder in glob.glob(folder_dir+"/*"):
        if os.path.isdir(folder.replace('\\', '/')):
            print(folder)
            recursivefolders(folder)
        if folder.endswith('.webp'):
            print(folder)
            im = Image.open(folder).convert("RGB")
            im.save(folder.replace(".webp",".jpg"), "jpeg")


recursivefolders(BASE_DIR)
