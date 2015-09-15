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
print 'COUNT'
print '====='
print '\n'

# set up some empty lists to make the graph later
counts_list = []

# empty dictionary for the graph
counts_dictionary_sho = {}


'''
get counts'''

# go through each ocr file
for filename in os.listdir('ocr'):
    # open it in super read mode
    with open(join('ocr', filename), 'rb') as ocr:
    
        # print filename
        print filename.replace('.txt', '')
        print '------------------'
        print '\n'
        
        # empty dictionary
        counts_dictionary_dai = {}
    
        # read it
        raw = ocr.read().decode('utf-8')
        # tokenize it
        text = nltk.word_tokenize(raw)
        

        '''
        get count'''
        
        # make sure uppercase and lowercase don't count as separate words
        text = [word.lower() for word in text]
        # prepare text for nltk processing
        ntext = nltk.Text(text)
        # number of appearances of a word
        albert = ntext.count('albert')
        print 'albert', albert
        kahn = ntext.count('kahn')
        print 'kahn', kahn
        concrete = ntext.count('concrete')
        print 'concrete', concrete
        print '\n'
                
        # append these to the list
        counts_dictionary_dai['albert'] = albert
        counts_dictionary_dai['kahn'] = kahn
        counts_dictionary_dai['concrete'] = concrete

        
        '''
        get the metadata'''
        
        # create the name of the dictionary we want to reference
        dictionary_dai = filename.replace('.txt', '').replace('.', '_')
        # grab the date from that dictionary
        year = dictionary_sho[dictionary_dai]['date']
        
        # append these to the list
        counts_dictionary_sho[year] = counts_dictionary_dai
        

'''
graph it'''

# give it a big, bold title
plt.suptitle('Counts', fontsize = 14, fontweight = 'bold')

# empty list for x values for every word
x_values = []

# go through and get the years
for key in counts_dictionary_sho:
    x_values.append(key)

# sort them    
x_values.sort()

# get the y values for albert
albert_y_values = []
for value in x_values:
    albert_y_values.append(counts_dictionary_sho[value]['albert'])

# get the y values for kahn
kahn_y_values = []
for value in x_values:
    kahn_y_values.append(counts_dictionary_sho[value]['kahn'])

# get the y values for concrete
concrete_y_values = []
for value in x_values:
    concrete_y_values.append(counts_dictionary_sho[value]['concrete'])

# set up the plot
plt.plot(x_values, albert_y_values, label='albert') 
plt.plot(x_values, kahn_y_values, label='kahn')
plt.plot(x_values, concrete_y_values, label = 'concrete')
# set up a label for the x axis
plt.xlabel('Publication Date')
# set up a label for the y axis
plt.ylabel('Counts')
# legend
plt.legend()
# show it
plt.show()