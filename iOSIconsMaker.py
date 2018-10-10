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
IOS7_FOLDER = 'iOS7+'
IOS6_FOLDER = 'iOS6.1-'


def resizeOneImage(imageShortName, size):
	# the file name is imageShortName + '.png'
	img = Image.open(imageShortName+IMAGE_TYPE)
	(w,h) = img.size
	(nw, nh) = (size, size)
	outImg = img.resize((nw, nh), Image.ANTIALIAS)
	newFile = imageShortName+'_'+str(size)+IMAGE_TYPE
	outImg.save(newFile)
	return newFile

def createIcons(imageShortName, sourceDir):
	# create folder first
	# put files to those folder
	# curDate =  datetime.date.today()
	# curTime = datetime.time()
	iconFolder = sourceDir+os.sep+DEFAULT_FOLDER
	if os.path.isdir(iconFolder):
		shutil.rmtree(iconFolder)

	os.mkdir(iconFolder)
	os.mkdir(iconFolder+os.sep+IOS6_FOLDER)
	os.mkdir(iconFolder+os.sep+IOS7_FOLDER)
	imageName = imageShortName+IMAGE_TYPE
	shutil.copy(imageName, iconFolder+os.sep+imageName)
	os.chdir(iconFolder)

	image29 = resizeOneImage(imageShortName, 29)
	image40 = resizeOneImage(imageShortName, 40)
	image50 = resizeOneImage(imageShortName, 50)
	image57 = resizeOneImage(imageShortName, 57)
	image58 = resizeOneImage(imageShortName, 58)
	image60 = resizeOneImage(imageShortName, 60)
	image72 = resizeOneImage(imageShortName, 72)
	image76 = resizeOneImage(imageShortName, 76)
	image80 = resizeOneImage(imageShortName, 80)
	image87 = resizeOneImage(imageShortName, 87)
	image114 = resizeOneImage(imageShortName, 114)
	image120 = resizeOneImage(imageShortName, 120)
	image144 = resizeOneImage(imageShortName, 144)
	image152 = resizeOneImage(imageShortName, 152)
	image180 = resizeOneImage(imageShortName, 180)
	image512 = resizeOneImage(imageShortName, 512)
	image1024 = resizeOneImage(imageShortName, 1024)
	imageItunes = 'iTunesArtwork'+IMAGE_TYPE
	imageItunes2x = 'iTunesArtwork@2x'+IMAGE_TYPE

	os.rename(image512, imageItunes)
	os.rename(image1024, imageItunes2x)

	ios7Images = [image87, image180, image120, image60, image152, image76, image80, image40, image58, image29, imageItunes, imageItunes2x]
	ios6Images = [image57, image114, image72, image29, image50, image58, image144, imageItunes, imageItunes2x]

	for imgName in ios7Images:
		shutil.copy(imgName, iconFolder+os.sep+IOS7_FOLDER+os.sep+imgName)

	for imgName in ios6Images:
		shutil.copy(imgName, iconFolder+os.sep+IOS6_FOLDER+os.sep+imgName)

	# remove temp files
	fileList = os.listdir(iconFolder)
	for name in fileList:
		fullName = iconFolder+os.sep+name
		if  os.path.isfile(fullName):
			os.remove(fullName)

starttime = datetime.datetime.now()
sourceDir = os.getcwd()
try:
	if len(sys.argv) < 2:
		print ('Need at lease one parameter: image name.')
	else:
		imageName = sys.argv[1]

		fullName = sourceDir + os.sep + imageName
		if  os.path.isfile(fullName):
				imageShortName = imageName[0:len(imageName)-len(IMAGE_TYPE)]
				if imageName.endswith(IMAGE_TYPE):
					createIcons(imageShortName, sourceDir)
				elif imageName.endswith('.jpg'):
					#need to convert it to png
					img = Image.open(imageName)
					img.save(imageShortName+'.png')
					createIcons(imageShortName, sourceDir)
				else:
					print ('Only support png or jpg format')
		else:
			print ('File not found: '+imageName)
		
except Exception as e:
	print ("Error found:", e, Exception)


endtime = datetime.datetime.now()
print ('spend time: ', (endtime-starttime))
