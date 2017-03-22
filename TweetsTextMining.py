__author__ = 'Xian Teng'
### ============= Descriptions ========== ###
### Analyze tweet contents

import re
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

### ====================== text mining ============================ ###
## extract emotion strings
emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

## extract 3 types of tokens hashtags, words, and words with - '
regex_str = [
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)", # hash-tags
    r"(?:[a-z][a-z'\-_]+[a-z])", # words with - and '
    r'(?:[\w_]+)', # other words
]

# removed_str = [
#     emoticons_str,
#     r'<[^>]+>', # HTML tags
#     r'(?:@[\w_]+)', # @-mentions
#     r'http[s]?:\\/\\/(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+', # URLs
# ]

url_str = r'http[s]?:\\/\\/(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
mention_str = r'(?:@[\w_]+)'

# removed_re = re.compile(r'('+'|'.join(removed_str)+')', re.VERBOSE | re.IGNORECASE)
# emoticon_re = re.compile(r'^'+emoticons_str+'$', re.VERBOSE | re.IGNORECASE)
tokens_re = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)


## tokenize all terms
def tokenize(s):
    return tokens_re.findall(s)

# def removed_set(s):
#     return removed_re.findall(s)

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via'] ## punctuation + stop words + 'rt' and 'via'

def preprocess(s):
    s = re.sub(emoticons_str,"",s) ## delete emoticons
    s = re.sub(url_str,"",s) ## delete urls
    s = re.sub(mention_str,"",s) ## delete @mentions
    tokens = tokenize(s) ## remain only 3 types of tokens - hashtags, words, words with -
    tokens = [token.lower() for token in tokens] ## to lower
    tokens = [token for token in tokens if token not in stop] ## delete stop words
    return tokens

## counts term frequency
def term_frequency(df_tweet):
    count_all = Counter()
    for i in range(0,len(df_tweet)):
        terms = [term for term in preprocess(df_tweet['text'].iloc[i]) if term not in stop]
        count_all.update(terms)
    print(count_all.most_common(10))

### ====================== text mining ============================ ###

### ====================== open problems ====================== ###
# token length constraints
# other language like french
# token frequency constraints

