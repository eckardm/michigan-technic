'''
import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk

# matplotlib is a python 2d plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms, you'll need to install it
import matplotlib.pyplot as plt

from dictionaries import dictionary_sho

'''
preliminaries'''

# print what we're doing
print 'ADDITIONAL COMMANDS'
print '=========================='
print '\n'

# words to look for
list_of_words = ['Albert', 'Kahn', 'concrete']


'''
get total words'''

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
        
        # find words that occupy similar spaces to a given word
        for word in list_of_words:
            ntext.similar(word)
        print '\n'
        
        # find the contexts that given words share
        ntext.common_contexts(list_of_words)
        print '\n'
                
        # number of appearances of a word
        for word in list_of_words:
            ntext.count(word)
        