'''
first things first, import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# adds a progress meter to your loops in a second
from tqdm import *


'''
preliminaries'''

# where is the folder of ocr files?
ocr_folder = 'ocr'


'''
get ocr for entire run'''

# go through each file in the ocr folder
for ocr_file in tqdm(os.listdir(ocr_folder)):
    print '\n'
    # open the ocr file
    ocr = open(join(ocr_folder, ocr_file), 'r')
    # go through each line in the ocr file
    for line in tqdm(list(ocr)):
        # open the ocr total file
        with open('ocr-total.txt', 'ab') as ocr_total:
            # write it to the ocr total file
            ocr_total.write(line)
    # close the ocr file
    ocr.close()
            