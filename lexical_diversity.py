'''
import what we need'''

# os provides a portable way of using operating system dependent functionality
import os
from os.path import join

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk

# matplotlib is a python 2d plotting library which produces publication quality figures in a variety of hardcopy formats and interactive environments across platforms, you'll need to install it
import matplotlib.pyplot as plt

'''
preliminaries'''

# print what we're doing
print 'LEXICAL DIVERSITY'
print '================='
print '\n'

# empty list
lexical_diversity_list = []


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
        
        lexical_diversity = len(text) / len(set(text))

        # print lexical diversity
        print 'LEXICAL DIVERSITY: ' + str(lexical_diversity)
        
        # append it to list
        lexical_diversity_list.append(lexical_diversity)
        
        # skip a space
        print '\n'
        
        
        '''
        get the metadata'''
        
        


'''
graph it'''

# set up the plot
plt.plot(lexical_diversity_list)
# set up a label for the y axis
plt.ylabel('Lexical Diversity')


# show it
plt.show()
        