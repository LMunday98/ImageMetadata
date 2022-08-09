from venv import create
from PIL import Image, ExifTags, ImageFont, ImageDraw
from os import walk, path, makedirs
from datetime import datetime
from sys import exit
from shutil import make_archive

from models.image import ImageModel

# dir create func

def create_dir(dir_path):
    if not path.exists(dir_path):
        makedirs(dir_path)

metadataDtField = "DateTimeOriginal"

imgDir = "images/"
inpDir = path.join(imgDir, "input/")
outDir = path.join(imgDir, "output/")

curDt = datetime.now()
curDtStr = curDt.strftime("%Y-%m-%d %H-%M-%S")
outDtDir = path.join(outDir, curDtStr)

# add dirs to script dirs to create if not present

scriptDirs = [
    imgDir,
    inpDir,
    outDir
]

# create output dir with current datetime

for dir in scriptDirs:
    create_dir(dir)

# get all image files in /input dir

filenames = next(walk(inpDir), (None, None, []))[2]  # [] if no file

# parse input images metadata

numImgs = len(filenames)

if numImgs < 1:
    print("no images in input dir")
    exit("stopping script\n")

create_dir(outDtDir)

filecnt = 0
for filename in filenames:

    print("parsing file " + str(filecnt) + " of " + str(numImgs))

    if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
        print("file is not an image\n")
        filecnt = filecnt + 1
        continue

    imgModel = ImageModel(filecnt, filename)
    imgModel.read_image(inpDir)
    imgModel.parse_image()
    imgModel.parse_font_size()
    imgModel.draw_txt()
    imgModel.save_image(outDtDir)

    filecnt = filecnt + 1

make_archive(outDtDir, "zip", outDtDir)