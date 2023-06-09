import sys

# mapper 2

for line in sys.stdin:
    
    line =line.strip()
    subreddit_id, sub_count, list_links = line.split("\t")
    
    print("{}\t{}\t{}".format(subreddit_id, sub_count, list_links))

