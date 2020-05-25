# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 16:05:06 2018

@author: Nawar
"""

import pandas as pd
import numpy as np
import os
import shutil

dtypes = {
        'image': 'str',
        'level': 'int',
        
}
train_df = pd.read_csv("trainLabels.csv", dtype = dtypes)

'''
Create the subfolders with the given labels from the data frame
'''
def create_folders():
    categories = np.unique(train_df.level.values)
    for i in categories:
        folder = '/media/husam/Data/project_2018/train_pre_sep/' + str(i)
        if not os.path.exists(folder):
            print('created folder', i)
            os.mkdir(folder)
        else:
            print( str(i), ' exists!')
            


'''
function to move the images to their corresponding folder
'''
def move_files():
    failed = 0
    for i, row in train_df.iterrows():
        filename = r"/media/husam/Data/project_2018/train_pre_sep/{}/{}.jpeg".format(row.level, 
                                      row.image )
        oldfile = r"/media/husam/Data/project_2018/train_pre/{}.jpeg".format(row.level )
        if not os.path.exists(filename):
#            try:
               os.rename(oldfile, filename)
#               print('moved {}.jpeg to {}'.format(row.image, row.level))
#            except:
               failed +=1
 #       else:
 #           print('{}.jpeg is in {}'.format(row.image, row.level))
    
    print('failed on {} files'.format(failed))


create_folders()
move_files()

