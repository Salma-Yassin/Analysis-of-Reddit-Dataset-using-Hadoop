import sys
import ssl
import nltk

# Added to solve certifcate verify error
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
   ssl._create_default_https_context = _create_unverified_https_context

# Download data required by nltk
#nltk.download('stopwords')
#nltk.download('averaged_perceptron_tagger')

from nltk.corpus import stopwords
from os import linesep
from collections import Counter
from nltk.tag import *

# Define list of stopwords
stop_words = stopwords.words('english')

# define a list of characters that need to be cleaned from the given strings
special_char = ['.' , '*']
# Extending thw stopword list.
extended_stopwords = ['us','mine','til']
stop_words.extend(extended_stopwords)

# define an output dictionary
out = {}

# for each
for line in sys.stdin:

    line = line.lower().strip().replace('"','')
    
    for key in special_char:
      line=line.replace(key,'')

    items = line.split(",")

    topic = ""
    subreddit = ""
    score = ""


    for item in items: # loop over each of the fields
        try:
          # split item to get field and value
          field,f_value = item.split(":") # check if the value associated with the field exists to avoid errors
        except: 
          continue

        if field == 'body':
            body = f_value
            body1= body.lower().split(' ')
            rem_stop_body = []
            pos_tags = nltk.pos_tag(body1) # take each of the words
            
            
            for token, tag in pos_tags: # exclude words that are not nouns or non-alphabatic 0r are stopwords
              if tag[0].upper() != "N" or not token.isalpha() or token.lower() in stop_words:
                 continue
              rem_stop_body.append(token)



            fd = {}

            if len(rem_stop_body) != 0: # check for empty body 
              for word in rem_stop_body:
                c = 0
                if word in fd:
                  c = fd[word] + 1
                else:
                    c = 1
                    fd[word]= c  
              
              max_w = sorted(fd.items(), key=lambda x: x[1], reverse= True)
              topic = max_w[0][0]

        if field == 'subreddit':
            subreddit = f_value
        if field == 'score':
            score = f_value


    if subreddit != "" and topic != "" and score != "": # check if all three required fields exist
      print("{}\t{}".format(topic , score))

    
