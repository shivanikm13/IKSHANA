import os
import cv2
from keras.preprocessing.image import img_to_array
orig = 'neworig'
seg = 'newseg'


class Loader:
    def __init__(self):
        self.x_data=[]
        self.y_data=[]

    def load(self):
        ori = os.listdir()
        for i in ori:
            img = cv2.imread()
            img = cv2.resize(img)
            self.x_data.append(img_to_array(img))
            # print(orig+'/'+i)
            img = cv2.imread()
            img = cv2.Canny(img, 100, 150)
            img = cv2.dilate(img, None, iterations=5)
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
            img = cv2.resize(img, (256, 256))
            # print(seg+'/'+i)
            self.y_data.append(img_to_array(img))
            

        return self.x_data, self.y_data
