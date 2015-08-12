'''
first things first, import the python modules we'll need, listed in the order you'll need them'''

# urllib2 opens URLs, it comes with python
import urllib2

# beautifulsoup pulls data out of html and xml files, you'll need to install it
from bs4 import BeautifulSoup

# nltk is a leading platform for building python programs to work with human language data, you'll need to install it
import nltk
from nltk import word_tokenize


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
    get dictionary entries for row result'''
    
    # go through row results
    for row_result in row_results:
        # find the title
        
        # find the date
        
        # find the id
        
        # tokenize the ocr
        
        
        '''
        make dictionary'''
        
        # make a dictionary
        
        # append the dictionary to our list
    
    '''
    get dictionary entries for row result alt'''
    
    # go through row result alts
    for row_result_alt in row_result_alts:
        # find the title
        
        # find the date
        
        # find the id
        
        # tokenize the ocr
        
        
        '''
        make dictionary'''
        
        # make a dictionary
        
        # append the dictionary to our list


    '''
    write dictionaries to file for reference later'''


'''
run it'''        
        
# note: my collection only has 42 items, so i set the url to the url that shows 50 items per page so they were all included
# note: to see collections in hathitrust, or to create your own, go here: https://babel.hathitrust.org/cgi/mb?colltype=updated
# note: if you have more than 100 items (the max), you'll have to tweak this code to go to the next page when getting volumes
        
# to run this, change 'https://babel.hathitrust.org/cgi/mb?a=listis;c=397666231;sort=title_a;pn=1;sz=50' to the url for your collection (you can also change the variable name if you like)
michigan_technic = 'https://babel.hathitrust.org/cgi/mb?a=listis;c=397666231;sort=title_a;pn=1;sz=50'

# run it!
make_dictionaries(michigan_technic)
