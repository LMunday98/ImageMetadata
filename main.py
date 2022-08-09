from sys import exit

from controllers.threadController import ThreadController
from controllers.fileHandler import FileHandlerController
from models.timer import TimerModel
from models.image import ImageModel

scriptTimer = TimerModel("main script")
scriptTimer.start()

print("starting script...")

fh = FileHandlerController()
tc = ThreadController()

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

    imgModel = ImageModel(filecnt, fileName, inpDir, dtOutDir)
    tc.add_thread((imgModel, ))

    filecnt = filecnt + 1

tc.start_threads()

fh.create_archive(dtOutDir)

print("stopping script...")

scriptTimer.stop()
scriptTimer.duration()