"""
##############################################
# version 1.0
# this function check the annotation files XML 
# the correct files provided only one image corresponding one same named XML file
# junfeng gao @ Ghent university
# 23-07-2018
##############################################
"""

import os

def check_XML_files():
	directory = os.getcwd()
	for dirs in ['train', 'test']: # both check train and test folders
		
		print (20*'@')
		print ('CHECKING {} FOLDER'.format(dirs))
		print (20*'@')

		full_dirs = os.path.join(directory, dirs)
		files = os.listdir(full_dirs)# get all the files in the folder
		
		image_files = filter(lambda element: '.JPG' in element, files) # get all the image files
		XML_files = filter(lambda element: '.xml' in element, files) # get all the annotation files
		# compare their names, one image should have one same named XML files
		
		xml_folder = []
		omit_files = []
		count = 0
		for xml_file in XML_files:
			xml_name = xml_file.split('.')[-2]
			xml_folder.append(xml_name)

		for image_file in image_files:
			image_name = image_file.split('.')[-2] # get the second last string 
			
			if image_name in xml_folder:
				count += 1
				print ('the image file {} has found its corresponding annotation file'.format(image_file))
			else:
				omit_files.append(image_file)
				print (20*'#')
				print ('the image file {} has not found its corresponding annotation file'.format(image_file))
				print (20*'#')
		print ('there are {} image files found annotation files in {} folder with {} - files'.format(count, dirs, len(image_files)) )		
		print('all files have their annotation files' if omit_files == [] and len(image_files) == len(XML_files) else omit_files)

if __name__ == '__main__':
	check_XML_files()

				
			
