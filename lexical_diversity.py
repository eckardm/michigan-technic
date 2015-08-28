'''
import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# import the dictionaries we created earlier
# go through the ocr directory and get the filename
for filename in os.listdir('ocr'):
    # create the dictionary name
    dictionary = filename.replace('.', '_')
    # and import the dictionary
    from dictionaries import dictionary
    

'''
get total words'''


'''
get unique words'''


'''
get lexical diversity'''


'''
graph it'''