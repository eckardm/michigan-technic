'''
first things first, import the python modules we'll need, listed in the order you'll need them'''

# urllib2 opens URLs, it comes with python
import urllib2

# beautifulsoup pulls data out of html and xml files, you'll need to install it
from bs4 import BeautifulSoup

# re provides regular expression matching operations
import re

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk


'''
go through each of the volumes in a collection, make dictionary entries for title, date, id'''

# defines a function to make the dictionaries based on one argument, a collection url
def make_dictionaries(collection_url):


    '''
    find the volumes'''
    
    # opening and reading the collection url
    collection = urllib2.urlopen(collection_url).read()
    # creating soup for it, which basically means pulling data out of it
    collection_soup = BeautifulSoup(collection)
    
    # finding all of the results (they are denoted in two ways)
    # row result
    row_results = collection_soup.find_all('div', {'class': 'row result'})
    # row result alt
    row_result_alts = collection_soup.find_all('div', {'class': 'row result alt'})
    
    '''
    make a way to get dictionary entries for row results and row result alts'''
    
    # function to get dictionary entries
    def get_row_results(div_class_attribute_value):
    
        # finding all of the results
        row_results = collection_soup.find_all('div', {'class': div_class_attribute_value})
        
        # make an emply list we'll use later
        dictionaries = []
        
        # go through row results
        for row_result in row_results:
            # find the title, remove articles from beginning
            title = re.sub('Item\s\d+\:\s', '', row_result.find('h4', {'class': 'Title'}).text).lstrip('The ').lstrip('An ').lstrip('A ')
            # find the date
            date = int(row_result.find('span', {'class': 'Date'}).text.replace('Published ', ''))
            # find the id, replaces the period because python doesn't like periods in variable names
            id = row_result.find('input', {'class': 'id'})['value']
           
            
            # '''
            # tokenize the ocr for row results'''
            
            # # open ocr
            # ocr = open('ocr/' + id + '.txt', 'r')
            # # read and decode data
            # ocr_data = ocr.read().decode('utf-8')
            # # tokenize
            # ocr_tokens = nltk.word_tokenize(ocr_data)
            # # close the ocr
            # ocr.close()
            
            
            '''
            make dictionary for row result'''
            
            # replaces the period in the id because python doesn't like periods in variable names
            dictionary_name = id.replace('.', '_')
            # initialize dictionary
            id = {}
            # add the title
            id['title'] = title
            # add the date
            id['date'] = date
            # add the id
            id['id'] = row_result.find('input', {'class': 'id'})['value']
            # # add the tokens
            # id['ocr'] = ocr_tokens
                        
            # append the dictionary to our list
            dictionaries.append(id)
            
            
        '''
        write dictionaries to file for reference later'''
        
        # go through each dictionary in the list
        for dictionary in dictionaries:
            # opening file so that we can append to it
            with open('dictionaries.py', 'a') as dictionaries_file:
                # writing the dictionaries
                dictionaries_file.write(dictionary_name + ' = ' + str(id))
                # and skipping a space
                dictionaries_file.write('\n')
        
        
    '''
    do this for row results'''
    
    # row result
    get_row_results('row result')
    # row result alt
    get_row_results('row result alt')


'''
run it'''        
        
# note: my collection only has 42 items, so i set the url to the url that shows 50 items per page so they were all included
# note: to see collections in hathitrust, or to create your own, go here: https://babel.hathitrust.org/cgi/mb?colltype=updated
# note: if you have more than 100 items (the max), you'll have to tweak this code to go to the next page when getting volumes
        
# to run this, change 'https://babel.hathitrust.org/cgi/mb?a=listis;c=397666231;sort=title_a;pn=1;sz=50' to the url for your collection (you can also change the variable name if you like)
michigan_technic = 'https://babel.hathitrust.org/cgi/mb?a=listis;c=397666231;sort=title_a;pn=1;sz=50'

# run it!
make_dictionaries(michigan_technic)
