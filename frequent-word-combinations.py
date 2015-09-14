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
print 'FREQUENT WORD COMBINATIONS'
print '=========================='
print '\n'

# empty list for all tokens
total_tokens = []

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
        
        # go through tokens
        for token in text:
            # add them to list of total text
            total_tokens.append(token)
        
        # prepare text for nltk processing
        ntext = ntlk.Text(text)
        # return frequent word combinations
        frequent_word_combinations = ntext.collocations()
        
        print type(frequent_word_combinations)
        
