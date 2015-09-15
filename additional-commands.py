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
print 'ADDITIONAL COMMANDS'
print '==================='
print '\n'

# words to look for
list_of_words = ['Albert', 'Kahn', 'concrete']


'''
do the additional commands from devon's guide'''

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
        print '### Words that occupy similar spaces to a given word'
        for word in list_of_words:
            word, ntext.similar(word)
        print '\n'
        
        # find the contexts that given words share
        print '### Contexts that given words share'
        print '\n'
        ntext.common_contexts(list_of_words)
        print '\n'
                
        # number of appearances of a word
        print '### Number of appearances of a given word'
        print '\n'
        for word in list_of_words:
            print word, ntext.count(word)
        print '\n'
        