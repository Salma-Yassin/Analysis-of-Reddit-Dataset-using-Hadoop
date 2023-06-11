# reducer 2:

import sys
from collections import Counter


out = {}


for line in sys.stdin:

    line = line.lower().strip().replace(']','').replace('[','').replace("'",'')
    # sub_count reltated to the top 10 choosed subreddit
    subreddit_id, sub_count, list_links = line.split("\t")
    list_links= list_links.split(",")
    
    top_topics = Counter(list_links).most_common(5) # return most common topic 

  
    print("{}\t{}".format(subreddit_id, top_topics))

