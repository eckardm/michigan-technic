import os
from os.path import join

# where is the folder of ocr files?
ocr_folder = 'ocr'

# go through each file in that folder
for ocr_file in os.listdir(ocr_folder):
    ocr = open(join(ocr_folder, ocr_file), 'r')
    for line in ocr:
        with open('ocr-total.txt', 'ab') as ocr_total:
            ocr_total.write(line)
