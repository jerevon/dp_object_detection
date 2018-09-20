import glob, os#
# current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
print (current_dir)

current_dir = '/home/psajg1/PHD-DATA/generate_images'
# change the directory fo4r generate txt file
percentage_test = 100 # based on your own data and requirements

# create aand truncate train.txt and test.txt
file_train = open('train_generate.txt', 'w')
#file_test = open('test.txt', 'w')

# populate train.txt and test.txt

counter = 1
index_test = round(100/percentage_test)

for pathAndFilename in glob.iglob(os.path.join(current_dir, '*.JPG')):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_train.write(current_dir + '/' + title + '.JPG' + '\n')
    else:
        file_train.write(current_dir + '/' + title + '.JPG' + '\n')
        counter += 1

