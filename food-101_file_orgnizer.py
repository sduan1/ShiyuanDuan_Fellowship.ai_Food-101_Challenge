import os
import shutil
relative_path = './food-101/images/'
with open('food-101/meta/labels.txt','r') as lable_file:
    labels = lable_file.read().split('\n')

labels = [x for x in labels if x != '']
for label in labels:
    label = label.lower().replace(' ', '_')
    os.makedirs('./food-101/train/'+label)
with open('food-101/meta/train.txt','r') as train_file:
    train_img_dirs = train_file.read().split('\n')

train_img_dirs = [x+'.jpg' for x in train_img_dirs if x != '']
for img_dir in train_img_dirs:
    label = img_dir.split('/')[0]
    sourse = relative_path+img_dir
    dest = './food-101/train/'+label
    try:
        shutil.move(sourse, dest)
    except:
        print('File name error. Please check the completeness of dataset')

for label in labels:
    label = label.lower().replace(' ', '_')
    os.makedirs('./food-101/test/'+label)

with open('food-101/meta/test.txt', 'r') as train_file:
    train_img_dirs = train_file.read().split('\n')

train_img_dirs = [x + '.jpg' for x in train_img_dirs if x != '']
for img_dir in train_img_dirs:
    label = img_dir.split('/')[0]
    sourse = relative_path + img_dir
    dest = './food-101/test/' + label
    try:
        shutil.move(sourse, dest)
    except:
        print('File name error. Please check the completeness of dataset')