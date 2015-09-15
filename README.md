# michigan-technic
HathiTrust text mining is easy! All you need is a collection! 

  1. Create or get a link to a public collection in HathiTrust.
  2. Run **get-ocr.py** to scrape HathiTrust and get the OCR on your local machine. This will take a while.
  3. Run **make-dictionaries.py**. This will get basic metadata for each volume in that collection.

From there, you can do some basic text analysis:

  * Run **lexical-diversity.py** to get an idea of the lexical diversity over time.
  * Run **frequent-word-combinations.py** to see freqent word combinations in each issue.
  * Run **word-occurences-in-context.py** to see a concordance for words in a list. *Note, you'll need to edit [this line](https://github.com/eckardm/michigan-technic/blob/master/word-occurences-in-context.py#L22) with the words you'd like to look for, and capitalization doesn't matter.*
