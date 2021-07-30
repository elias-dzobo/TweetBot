import json
from nltk.tokenize import word_tokenize
import re
import operator
from collections import Counter


# tokenize the tweet
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""
 
regex_str = [
    emoticons_str,
    r'<[^>]+>', # HTML tags
    r'(?:@[\w_]+)', # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
 
    r'(?:(?:\d+,?)+(?:\.?\d+)?)', # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
    r'(?:\S)' # anything else
]
    
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
 
def tokenize(s):
    return tokens_re.findall(s)
 
def preprocess(s, lowercase=False):
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    return tokens


# check tweet

with open('ada.json', 'r') as f:
    line = f.readline()  # read first line
    tweet = json.loads(line) #load line as a dict
    tokens = preprocess(tweet['text'])
    print(tokens)

f.close()

with open('ada.json', 'r') as f:
    count_all = Counter()
    tweets = [json.load(line) for line in f.readlines()]
    terms_all = [ preprocess(tweet['text']) for tweet in tweets]
    count_all.update(terms_all)
    print(count_all.most_common(5))

    """ tweet = json.loads(line) #load line as a dict
    terms_all = [term for term in preprocess(tweet['text'])]
    count_all.update(terms_all)
    
     """