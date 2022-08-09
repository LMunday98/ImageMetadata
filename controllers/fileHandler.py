from os import walk, path, makedirs
from shutil import make_archive
from datetime import datetime

class FileHandlerController:

    dirs = {
        "img": "images/",
        "inp": "images/input/",
        "out": "images/output/",
        "dtOut": "",
    }

    allowedImgFormats = (
        ".png",
        ".jpg",
        ".jpeg",
        ".tiff",
        ".bmp",
        ".gif"
    )

    def __init__(self):
        dirs = self.dirs

        dirs_to_create = [dirs["img"], dirs["inp"], dirs["out"]]
        for dir in dirs_to_create:
            self.create_dir(dir)

        self.set_dt_out_dir()

    def set_dt_out_dir(self):
        outDir = self.dirs["out"]

        curDt = datetime.now()
        curDtStr = curDt.strftime("%Y-%m-%d %H-%M-%S")
        outDtDir = path.join(outDir, curDtStr)

        self.dirs["dtOut"] = outDtDir


    def create_dir(self, dir_path):
        print("\ncheck dir [" + dir_path + "]")

        if not path.exists(dir_path):
            print("dir [" + dir_path + "] does not exist, create")
            makedirs(dir_path)
        else:
            print("dir [" + dir_path + "] already exists, skip create")

    def create_archive(self, dir_path):
        make_archive(dir_path, "zip", dir_path)

    def check_inp_files(self, fileNames):
        numFiles = len(fileNames)

        if numFiles < 1:
            return False

        return True

    def get_dir_filenames(self, dir):
        return next(walk(dir), (None, None, []))[2]  # [] if no file

    def get_dir_path(self, dir):
        return self.dirs[dir]

    def file_is_image(self, fileName):
        imgFmts = self.allowedImgFormats

        return fileName.lower().endswith(imgFmts)