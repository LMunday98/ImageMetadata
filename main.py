from sys import exit

from controllers.fileHandler import FileHandlerController
from models.image import ImageModel

fh = FileHandlerController()

inpDir = fh.get_dir_path("inp")
dtOutDir = fh.get_dir_path("dtOut")

fileNames = fh.get_dir_filenames(inpDir)

if not fh.check_inp_files(fileNames):
    print("no images in input dir")
    exit("stopping script\n")

fh.create_dir(dtOutDir)

filecnt = 0
for fileName in fileNames:

    print("parsing file " + str(filecnt))

    if not fh.file_is_image(fileName):
        print("file is not an image\n")
        filecnt = filecnt + 1
        continue

    imgModel = ImageModel(filecnt, fileName)
    imgModel.read_image(inpDir)
    imgModel.parse_image()
    imgModel.parse_font_size()
    imgModel.draw_txt()
    imgModel.save_image(dtOutDir)

    filecnt = filecnt + 1

fh.create_archive(dtOutDir)