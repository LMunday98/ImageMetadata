from venv import create
from PIL import Image, ExifTags, ImageFont, ImageDraw
from os import walk, path, makedirs
from datetime import datetime
from sys import exit

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

if len(filenames) < 1:
    print("no images in input dir")
    exit("stopping script\n")

create_dir(outDtDir)

for filename in filenames:

    inpImagePath = path.join(inpDir, filename)
    outImagePath = path.join(outDtDir, filename)
    
    img = Image.open(inpImagePath)

    imgWidth, imgHeight = img.size

    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

    if metadataDtField not in exif:
        print("dtField [" + metadataDtField + "] does not exist in image exif\n")
        print(exif)
        exit("stopping script\n")

    mDatetime = exif[metadataDtField]
    print(mDatetime)
    imgtxt = mDatetime.replace(":", "-")

    draw = ImageDraw.Draw(img)

    fontsize = 1  # starting font size
    fonttype = "Keyboard.ttf"

    # portion of image width you want text width to be
    img_fraction = 0.50

    font = ImageFont.truetype(fonttype, fontsize)
    while font.getsize(imgtxt)[0] < img_fraction * img.size[0]:
        # iterate until the text size is just larger than the criteria
        fontsize += 1
        font = ImageFont.truetype(fonttype, fontsize)

    # optionally de-increment to be sure it is less than criteria
    fontsize -= 1
    font = ImageFont.truetype(fonttype, fontsize)

    # draw.text((x, y),"Sample Text",(r,g,b))
    draw.text(
        (0, 0),
        imgtxt,
        (235, 232, 52), # yellow
        font=font
    )

    img.save(outImagePath)
    # print(outImagePath)