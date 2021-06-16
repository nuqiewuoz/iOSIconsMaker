'''The icon image must be PNG format

In this version, this script create a sub folder 'AppIcon' in the png file folder.
If the 'AppIcon' folder has already existed, the old one will be deleted.
In the 'AppIcon' folder, there are two subfolder: 'iOS7+' and 'iOS6.1-', represent the iOS SDK which your app supports.
'''

import os
import sys
import shutil
from PIL import Image
import datetime

IMAGE_TYPE = '.png'
DEFAULT_FOLDER = 'AppIcon'
WATCH_FOLDER = 'iWatch'


def resize_one_image(image_name, size):
    # the file name is image_name + '.png'
    img = Image.open(image_name + IMAGE_TYPE)
    (w,h) = img.size
    (nw, nh) = (size, size)
    out_img = img.resize((nw, nh), Image.ANTIALIAS)
    new_file = image_name + '_' + str(size) + IMAGE_TYPE
    out_img.save(new_file)
    return new_file


def create_icons(image_name, sourceDir):
	# create folder first
	# put files to those folder
	# curDate =  datetime.date.today()
	# curTime = datetime.time()
    icon_folder = sourceDir+os.sep+DEFAULT_FOLDER
    if os.path.isdir(icon_folder):
        shutil.rmtree(icon_folder)

    os.mkdir(icon_folder)
    os.mkdir(icon_folder + os.sep + WATCH_FOLDER)
    imageName = image_name+IMAGE_TYPE
    shutil.copy(imageName, icon_folder+os.sep+imageName)
    os.chdir(icon_folder)

    image29 = resize_one_image(image_name, 29)
    image40 = resize_one_image(image_name, 40)
    image48 = resize_one_image(image_name, 48)
    image50 = resize_one_image(image_name, 50)
    image55 = resize_one_image(image_name, 50)
    image57 = resize_one_image(image_name, 57)
    image58 = resize_one_image(image_name, 58)
    image60 = resize_one_image(image_name, 60)
    image72 = resize_one_image(image_name, 72)
    image76 = resize_one_image(image_name, 76)
    image80 = resize_one_image(image_name, 80)
    image87 = resize_one_image(image_name, 87)
    image100 = resize_one_image(image_name, 100)
    image114 = resize_one_image(image_name, 114)
    image120 = resize_one_image(image_name, 120)
    image144 = resize_one_image(image_name, 144)
    image152 = resize_one_image(image_name, 152)
    image167 = resize_one_image(image_name, 167)
    image172 = resize_one_image(image_name, 172)
    image180 = resize_one_image(image_name, 180)
    image196 = resize_one_image(image_name, 196)
    image216 = resize_one_image(image_name, 216)
    image512 = resize_one_image(image_name, 512)
    image1024 = resize_one_image(image_name, 1024)

    watchImages = [image48, image55, image58, image80, image100, image172, image196, image216, image1024]
    for imgName in watchImages:
        shutil.copy(imgName, icon_folder+os.sep+WATCH_FOLDER+os.sep+imgName)
    # # remove temp files
    # file_list = os.listdir(icon_folder)
    # for name in file_list:
    #     full_name = icon_folder + os.sep + name
    #     if  os.path.isfile(full_name):
    #         os.remove(full_name)


start_time = datetime.datetime.now()
sourceDir = os.getcwd()
try:
    if len(sys.argv) < 2:
        print ('Need at lease one parameter: image name.')
    else:
        imageName = sys.argv[1]

        full_name = sourceDir + os.sep + imageName
        if os.path.isfile(full_name):
            image_name = imageName[0:len(imageName)-len(IMAGE_TYPE)]
            if imageName.endswith(IMAGE_TYPE):
                create_icons(image_name, sourceDir)
            elif imageName.endswith('.jpg'):
                #need to convert it to png
                img = Image.open(imageName)
                img.save(image_name+'.png')
                create_icons(image_name, sourceDir)
            else:
                print ('Only support png or jpg format')
        else:
            print ('File not found: '+imageName)
		
except Exception as e:
	print ("Error found:", e, Exception)


end_time = datetime.datetime.now()
print ('spend time: ', (end_time - start_time))
