'''
import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk

from dictionaries import dictionary_sho


'''
preliminaries'''

# print what we're doing
print 'DISPERSION PLOT'
print '==============='
print '\n'

# words to look for
list_of_words = ['Albert', 'Kahn', 'concrete']


'''
get dispersion plot'''

# go through each ocr file
for filename in os.listdir('ocr'):
    # open it in super read mode
    with open(join('ocr', filename), 'rb') as ocr:
    
        # print filename
        print filename.replace('.txt', '')
        print '------------------'
        print '\n'
    
        # read it
        raw = ocr.read().decode('utf-8')
        # tokenize it
        text = nltk.word_tokenize(raw)
        
        # prepare text for nltk processing
        ntext = nltk.Text(text)
        # display a graphical view of where a given list of words appears
        ntext.dispersion_plot(list_of_words)
        