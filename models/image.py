from os import path
from PIL import Image, ImageFont, ImageDraw, ExifTags

class ImageModel:

    inpDir = ""
    outDir = ""

    imgIndex = 0
    fileName = ""
    imgObj = {}

    dtField = "DateTimeOriginal"
    imgTxt = ""

    imgFraction = 0.50

    font = {}
    fontSize = 1
    fontStyle = "Keyboard.ttf"

    def __init__(self, _imgIndex, _fileName, _inpDir, _outDir):
        self.imgIndex = _imgIndex
        self.fileName = _fileName
        self.inpDir = _inpDir
        self.outDir = _outDir

    def start(self):
        imgIndexTxt = str(self.imgIndex)
        print("starting image thread for index [" + imgIndexTxt + "]")
        
        self.read_image()
        self.parse_image()
        self.parse_font_size()
        self.draw_txt()
        self.save_image()

    def read_image(self):
        imgIndexTxt = str(self.imgIndex)
        print("reading image for index [" + imgIndexTxt + "]")

        inpDir = self.inpDir
        fileName = self.fileName

        inpImagePath = path.join(inpDir, fileName)
        self.imgObj = Image.open(inpImagePath)

        return True

    def parse_image(self):
        imgIndexTxt = str(self.imgIndex)
        print("parsing image for index [" + imgIndexTxt + "]")

        img = self.imgObj
        dtField = self.dtField

        exif = {
            ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS
        }
        
        if dtField not in exif:
            print("dtField [" + dtField + "] does not exist in image exif\n")
            print(exif)
            return False

        imgDt = exif[dtField]
        self.imgTxt = imgDt.replace(":", "-")

        return True

    def parse_font_size(self):
        imgIndexTxt = str(self.imgIndex)
        print("parsing font size for index [" + imgIndexTxt + "]")

        imgSize = self.imgObj.size
        imgFraction = self.imgFraction
        imgTxt = self.imgTxt

        fontSize = self.fontSize
        fontStyle = self.fontStyle

        font = ImageFont.truetype(fontStyle, fontSize)
        while font.getsize(imgTxt)[0] < imgFraction * imgSize[0]:
            # iterate until the text size is just larger than the criteria
            fontSize += 1
            font = ImageFont.truetype(fontStyle, fontSize)

        # optionally de-increment to be sure it is less than criteria
        fontSize -= 1
        font = ImageFont.truetype(fontStyle, fontSize)

        self.font = font

    def draw_txt(self):
        imgIndexTxt = str(self.imgIndex)
        print("drawing image text for index [" + imgIndexTxt + "]")

        img = self.imgObj
        imgTxt = self.imgTxt
        font = self.font

        draw = ImageDraw.Draw(img)

        draw.text(
            (0, 0),
            imgTxt,
            (235, 232, 52), # yellow
            font=font
        )


    def save_image(self):
        imgIndexTxt = str(self.imgIndex)
        print("saving image for index [" + imgIndexTxt + "]")

        outDir = self.outDir
        fileName = self.fileName
        img = self.imgObj

        outImagePath = path.join(outDir, fileName)
        img.save(outImagePath)

        return True