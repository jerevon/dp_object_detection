# dp_object_detection
this folder included files for preprocessing files (resize with same aspect ratio) and preparation files for object detection with deep learning 
resizer: to resize image with smaller dimension and same aspect ratio as original image.
reason: large dimension (4000 * 6000) image could not be trained with tensorflow object detection API 
### file ####
## train and test folders 
contain images and handmade annonation files
### csv files ###
train_labels.csv--> convert train XML files (annotation files) to .csv files
test_labels.csv --> convert test XML (annotation files) to .csv files
