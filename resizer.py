import numpy as np
import cv2
import os
import imutils

#
# class AspectAwarePreprocessor:
#     def __init__(self, width, height, inter = cv2.INTER_AREA):
#         # store taget image width, height and interpolation
#         self.width = width
#         self.height = height
#         self.inter = inter
#
#     def preprocess(self,image):
#         (h, w) = image.shape[:2]
#         dW = 0
#         dH = 0
#
#         if w < h:
#             image = imutils.resize(image, width=self.width, inter = self.inter)
#             dH = int((image.shape[0] - self.height)/2.0)
#
#         else:
#             image = imutils.resize(image, height = self.height, inter = self.inter)
#             dW = int((image.shape[1] - self.width)/2.0)
#
#         (h, w) = image.shape[:2]
#         image = image[dH:h-dH, dW:w-dW]
#         return cv2.resize(image, (self.width, self.height), interpolation=self.inter)

# TO DO: CHANGE THE DIRECTORY OF THE IMAGE FILES
dirname = ['']
image_dir = 'E:\\PHD_data_2018\\maize field\\maize field_29-05-2018'
filedir = os.listdir(image_dir)
imagefiles = filter(lambda element: '.JPG' in element, filedir)
print imagefiles
print 'There are {} images needed to be converted'.format(len(imagefiles))
for image_file in imagefiles:
    image_file = os.path.join(image_dir, image_file)
    image = cv2.imread(image_file)
    image = imutils.resize(image, width=800, inter = cv2.INTER_AREA)
    cv2.imwrite(image_file, image)
    print '{} was converted'.format(image_file)
print 'task done !!!'

