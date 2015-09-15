# michigan-technic
HathiTrust text mining is easy! All you need is a collection! 

  1. Create or get a link to a public collection in HathiTrust.
  2. Run **get-ocr.py** to scrape HathiTrust and get the OCR on your local machine. This will take a while.
  3. Run **make-dictionaries.py**. This will get basic metadata for each volume in that collection.

From there, you can do some basic text analysis:

  * Run **lexical-diversity.py** to get an idea of the lexical diversity over time.
  * Run **frequent-word-combinations.py** to see freqent word combinations in each issue.
  * Run **word-occurences-in-context.py** to see a concordance for words in a list. *Note, you'll need to edit [this line](https://github.com/eckardm/michigan-technic/blob/master/word-occurences-in-context.py#L23) with the words you'd like to look for, and capitalization doesn't matter.*
  * Run **frequency-distribution.py** to do a the following: 1) view the top most 50 words; 2) view the top most 50 words plotted; 3) generate a word cloud image; and, 4) view words that only occur once.
  * Run **dispersion-plot.py** to create dispersion plots by issue for words in a list. *Note, you'll need to edit [this line](https://github.com/eckardm/michigan-technic/blob/master/dispersion-plot.py#L23) with the words you'd like to look for, and capitalization doesn't matter.*
  * Run **additional-commands.py** to run the additional commands, including the following: 1) find words that occupy similar spaces to a given word; 2) find the contexts that given words share; and 3) number of appearances of a word. *Note, you'll need to edit [this line](https://github.com/eckardm/michigan-technic/blob/master/additional-commands.py#L23) with the words you'd like to look for, and capitalization doesn't matter.*
  * Run **count.py** to get counts for particular words for each issue, and then over time. * Run **additional-commands.py** to run the additional commands, including the following: 1) find words that occupy similar spaces to a given word; 2) find the contexts that given words share; and 3) number of appearances of a word. *Note, in its current state you'll need to edit a number of places if you don't want to look for the same words I looked for. I'll try to get this fixed soon.*
