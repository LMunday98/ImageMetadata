from sys import exit

from controllers.fileHandler import FileHandlerController
from models.image import ImageModel

fh = FileHandlerController()

# get all image files in /input dir

inpDir = fh.get_dir_path("inp")
fileNames = fh.get_dir_filenames(inpDir)

# parse input images metadata

numImgs = len(fileNames)

if numImgs < 1:
    print("no images in input dir")
    exit("stopping script\n")

fh.set_dt_out_dir()
dtOutDir = fh.get_dir_path("dtOut")
fh.create_dir(dtOutDir)

filecnt = 0
for filename in fileNames:

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
    imgModel.save_image(dtOutDir)

    filecnt = filecnt + 1

fh.create_archive(dtOutDir)