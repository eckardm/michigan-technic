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
print 'LEXICAL DIVERSITY'
print '================='
print '\n'

# empty dictionary
lexical_diversity_dictionary = {}

# set up some empty lists to make the graph later
diversities = []
years = []


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
        
        # calculate the lexical diversity and store it as a variable
        lexical_diversity = len(text) / len(set(text))

        # print lexical diversity
        print '**Lexical diveristy: ' + str(lexical_diversity) + '**' + '\n'
        
        # append these to the list
        diversities.append(int(lexical_diversity))
        
        
        '''
        get the metadata'''
        
        # create the name of the dictionary we want to reference
        dictionary_dai = filename.replace('.txt', '').replace('.', '_')
        # grab the date from that dictionary
        year = dictionary_sho[dictionary_dai]['date']
        
        # append these to the list
        years.append(int(year))
        
        '''
        add to dictionary'''
        
        # add everything to the core dictionary
        lexical_diversity_dictionary[year] = lexical_diversity
        

'''
graph it'''

# give it a big, bold title
plt.suptitle('Lexical Diversity', fontsize = 14, fontweight = 'bold')

# make pairs of data from the dictionary and sort them for matplotlib
data_pairs = [[key, value] for key, value in lexical_diversity_dictionary.items()]
data_pairs.sort()

# create the x and y values
x_values = [item[0] for item in data_pairs]
y_values = [item[1] for item in data_pairs]

# set up the graph
plt.axis([min(years), max(years), 0, max(diversities) + 1])

# set up the plot
plt.plot(x_values, y_values)
# set up a label for the x axis
plt.xlabel('Publication Date')
# set up a label for the y axis
plt.ylabel('Lexical Diversity')

# show it
plt.show()


''''
Other ideas: add annotations with title for highest and lowest diversities.'''
        