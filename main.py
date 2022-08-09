from PIL import Image, ExifTags
from os import walk, path, makedirs
from datetime import datetime

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
    outDir,
    outDtDir
]

# create output dir with current datetime

for dir in scriptDirs:
    if not path.exists(dir):
        makedirs(dir)

# get all image files in /input dir

filenames = next(walk(inpDir), (None, None, []))[2]  # [] if no file

# parse input images metadata

for filename in filenames:
    imagePath = path.join(inpDir, filename)
    
    img = Image.open(imagePath)
    exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }

    mDatetime = exif["DateTimeOriginal"]
    print(mDatetime)