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
print 'FREQUENT WORD COMBINATIONS'
print '=========================='
print '\n'


'''
get frequent word combinations'''

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
        
        # make sure uppercase and lowercase don't count as separate words
        text = [word.lower() for word in text]
        
        # remove very common words from text
        clean_text = [w for w in text if w not in stopwords]
        
        # make sure it is just words
        just_words = [w for w in clean_text if w.isalpha()]
        
        # prepare text for nltk processing
        ntext = nltk.Text(just_words)
        # return frequent word combinations, or rather try to
        try:
            ntext.collocations()
        # if not, just make note of it for now
        except:
            print '**Encoding error**'
        # skip a space
        print '\n'
        