# ImageMetadata

## Specification

This project parses image files and adds the timestamp from the metadata onto the image, before saving and zipping.

## Setup

1. Clone to repo locally.

2. Run the `make run` command and create the inital dirs.

3. Insert images into the `/images/input/` dir.

4. Run the `make run` command again to parse the images, which will be put into the `/images/output/` dir with a timestamp for the created dir and archive.

## Project Stucture
```
/
├── controllers/
│   ├── fileHandler.py
│   └── threadController.py
├── images/
│   ├── input/
│   └── output/
├── main.py
├── Makefile
├── models/
│   ├── image.py
│   └── timer.py
└── README.md
```
