# import libraries
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
def get_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = os.path.join(folder,filename)
        images.append(img)
    return images
def resize_image(image):
    image = cv2.imread(image)
    #resize the image in 250x250 dimension
    resized_image = cv2.resize(image,(250,250),interpolation = cv2.INTER_LINEAR)
    return resized_image
def save_images_in_folder(folder,filename,img):
    cv2.imwrite(os.path.join(folder,filename), img)
    cv2.waitKey(1)       
def rotation(image):
    image = cv2.imread(image)
    #(col/2,rows/2) is the center of rotation for the image
    # M is the cordinates of the center 
    rows,cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
    dst = cv2.warpAffine(image,M,(cols,rows))
    return dst       
def translation(image):
    image = cv2.imread(image)
    rows,cols = image.shape[:2]
    quarter_rows, quarter_cols = rows / 4, cols / 4
    #shifting the image 100 pixels in both dimensions
    M = np.float32([[1,0,quarter_cols],[0,1,quarter_rows]])
    dst = cv2.warpAffine(image,M,(cols,rows))
    return dst 
def data_augmentation(input_folder):
    '''This function will apply data_augmentation on 4 resized images taken from input folder'''
    images = get_images_from_folder(input_folder)
    #apply data augmentation
    rotated_image_1 = rotation(images[1])
    rotated_image_2 = rotation(images[3])
    translated_image_1 = translation(images[2])
    translated_image_2 = translation(images[5])
    
    #saved augmented images in output folder
    save_images_in_folder(rotation_folder, 'rotated_image_1.jpg', rotated_image_1)
    save_images_in_folder(rotation_folder, 'rotated_image_2.jpg', rotated_image_2)
    save_images_in_folder(translation_folder, 'translated_image_1.jpg', translated_image_1)
    save_images_in_folder(translation_folder, 'translated_image_2.jpg', translated_image_2)
    
input_folder = 'D:/AI_labs/lab-8/Source'
resized_folder = 'D:/AI_labs/lab-8/resized'
rotation_folder = 'D:/AI_labs/lab-8/rotation'
translation_folder = 'D:/AI_labs/lab-8/translation'
#get images path from folder
images = get_images_from_folder(input_folder)

for i in images:
    file_name = i.split("\\")[1]
    #resize each image of input folder
    resized_image = resize_image(i)
    #saved the resized image of input folder into output folder
    save_images_in_folder(resized_folder, file_name, resized_image)

data_augmentation(resized_folder)
    



