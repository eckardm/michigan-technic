'''
import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk
from nltk.corpus import stopwords

# matplotlib is a python 2d plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms, you'll need to install it
import matplotlib.pyplot as plt

# a little word cloud generator, you'll need to install it, as well as
from wordcloud import WordCloud

from dictionaries import dictionary_sho


'''
preliminaries'''

# print what we're doing
print 'FREQUENCY DISTRIBUTION'
print '======================'
print '\n'


'''
get total words'''

# not total with stopwords
stopwords = stopwords.words('english')

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
        
        # calculate a frequency distribution for words in the text
        fdist = nltk.FreqDist(just_words)
        
        # view the top most 50 words
        print fdist.items()[:50]
        print '\n'
        
        # plot the top most 50 words
        fdist.plot(50, cumulative=True)
        
        # generate a word cloud image
        wordcloud = WordCloud().generate(raw)
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.show()
        
        # view the words in a text that only occur once
        print fdist.hapaxes()
        print '\n'