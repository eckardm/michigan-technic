'''
first things first, import the python modules we'll need, listed in the order you'll need them'''

# os provides a portable way of using operating system dependent functionality
import os

# urllib2 opens URLs, it comes with python
import urllib2

# beautifulsoup pulls data out of HTML and XML files, you'll need to install it
from bs4 import BeautifulSoup

# re provides regular expression matching operations
import re

# time provides various time-related functions, we'll be using it to wait
import time
        
        
'''
go through each of the volumes in a collection, click the plain text link and scrape it'''

# defines a function to get ocr based on one argument, a collection url
def get_volume_ocr(collection_url):

    
    '''
    make directory for ocr'''
    
    # constructing the output path
    os.mkdir('ocr-bread')


    '''
    get the volume urls'''
    
    # opening and reading the collection url
    collection = urllib2.urlopen(collection_url).read()
    # creating soup for it, which basically means pulling data out of it
    collection_soup = BeautifulSoup(collection)
    
    # finding all of the full text links by searching for anchors with a class of fulltext icomoon-document-2 (i have no idea what icomoon-document-2 means)
    full_text_urls = collection_soup.find_all('a', {'class': 'fulltext icomoon-document-2'})
    
    # creating an empty list so that we can populate it with volume urls
    volume_urls = set()
    # going through all of the full text urls
    for full_text_url in full_text_urls:
        # creating the volume url by appending the full text url to the hathitrust babel base url
        volume_url = 'https://babel.hathitrust.org' + full_text_url['href']
        # and then appending that url to the volume url list we created earlier
        volume_urls.add(volume_url)
    
    
    '''
    get the volume id and store that as a variable, because we'll use it later'''
    
    # going through all of the volume urls
    for volume_url in volume_urls:
        # and picking out volume identifier (always the last 18 characters)
        item_id_string = volume_url.split('=')[-1]
        
        
        
        
        '''
        go to each volume url and figure out how many pages it has'''
        
        # opening and reading the volume url
        volume = urllib2.urlopen(volume_url).read()
        # creating soup for it, which basically means pulling data out of it
        volume_soup = BeautifulSoup(volume)
        
        # finding the go to last link by searching for anchors with an id of action-go-last
        action_go_last = volume_soup.find('a', {'id': 'action-go-last'})    
       
        # getting the url, which contains the last page number
        action_go_last_url = action_go_last['href']
        # using a regex to look for what's between 'seq=' and ';'
        number_of_sequence_or_fileid = int(re.search('seq=(\d{1,4})', action_go_last_url).group(1))
        

        '''
        output the ocr to text file for each volume'''
        
        # we'll need to loop through each page, so initializing a counter at 0
        sum = 0
        # then we'll go through each page (and eventually adding one to go to the next one), as long as the number of the pages we're on is less than or equal to the total number of pages
        while sum <= number_of_sequence_or_fileid:
            
            # creating the url for the page
            page_url = 'https://babel.hathitrust.org/cgi/pt?id=' + item_id_string + ';view=1up;seq=' + str(sum)
         
            # going to it and reading it, accounting for 503 errors
            while True:
                try:
                    page = urllib2.urlopen(page_url).read()
                    # making soup from it
                    page_soup = BeautifulSoup(page)
                    # then finding the link to the plain text
                    pt_plain_text = page_soup.find('a', {'data-tracking-action': 'PT Plain Text'})
                    # getting the link
                    pt_plain_text_url = pt_plain_text['href']
                    # creating the url for the ocr
                    ocr_url = 'https://babel.hathitrust.org' + pt_plain_text_url
                    # going to it and reading it
                    ocr = urllib2.urlopen(ocr_url).read()
                    # making soup from it
                    ocr_soup = BeautifulSoup(ocr)
                    # finding the ocr
                    page_item_page_text = ocr_soup.find('div', {'class': 'page-item page-text'})
                    # and, if it has something there
                    if page_item_page_text is not None:
                        # getting rid of all the html tags
                        page_item_page_text = re.sub(r'\<(.*)?\>', '', str(page_item_page_text))
                        # printing it to the terminal(just for fun)
                        print page_item_page_text
                        # and file unique to each volume
                        output_text = 'ocr-bread\\' + item_id_string + '.txt'
                        # opening the file at that path so that we can append to it
                        with open(output_text, 'a') as text_file:
                            # and writing the ocr!
                            text_file.write(page_item_page_text)
                    # incrementing the sum
                    sum += 1
                    # and giving the hathitrust servers a chance to catch their breath
                    time.sleep(1)      

                # if it doesn't work, wait a bit a try again    
                except:
                    time.sleep(10)
                    continue
                    
                # exiting the loop
                break
        

'''
run it'''        
        
# note: my collection only has 42 items, so i set the url to the url that shows 50 items per page so they were all included
# note: to see collections in hathitrust, or to create your own, go here: https://babel.hathitrust.org/cgi/mb?colltype=updated
# note: if you have more than 100 items (the max), you'll have to tweak this code to go to the next page when getting volumes
        
# to run this, change 'https://babel.hathitrust.org/cgi/mb?a=listis;c=397666231;sort=title_a;pn=1;sz=50' to the url for your collection (you can also change the variable name if you like)
michigan_technic = 'https://babel.hathitrust.org/cgi/mb?a=listis;c=397666231;sort=title_a;pn=1;sz=50'
bread = 'http://babel.hathitrust.org/cgi/mb?a=listis;c=858234468'

# run it!
get_volume_ocr(bread)


'''
once this runs, we'll also need to set up a dictionaries for each volume that includes metadata (title, date, id)and the tokenized ocr'''
