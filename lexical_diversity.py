'''
import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk


'''
what are we doing?'''

# print what we're doing
print 'LEXICAL DIVERSITY'
print '================='
print '\n'


'''
get total words'''

# go through each ocr file
for filename in os.listdir('ocr'):
    # open it in super read mode
    with open(join('ocr', filename), 'rb') as ocr:
    
        # print filename
        print filename
        print '----------------------'
        print '\n'
    
        # read it
        raw = ocr.read().decode('utf-8')
        # tokenize it
        text = nltk.word_tokenize(raw)
        # print the filename and total words
        print 'Total words: ' + str(len(text))


        '''
        get unique words'''
        
        # make sure uppercase and lowercase don't count as separate words
        text = [word.lower() for word in text]
        # print the filename and unique words
        print 'Unique words: ' + str(len(set(text)))

        
        '''
        get lexical diversity'''

        # print lexical diversity
        print 'LEXICAL DIVERSITY: ' + str(len(text) / len(set(text)))
        
        # skip a space
        print '\n'


        '''
        graph it'''