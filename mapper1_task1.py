import sys

# mapper 

for line in sys.stdin:

    line = line.lower().strip().replace('"','').replace('}','').replace('{','')
    items = line.split(",")
    
    link_id = ""
    subreddit_id = ""
    subreddit = ""

    for item in items:
        try: 
          field,f_value = item.split(":")
        except: 
          continue

        if field == 'link_id':
            link_id = f_value 
            #print(type(topic),count)
        if field == 'subreddit_id':
            subreddit_id = f_value 
            #print(topic)
        if field == 'subreddit':
            subreddit = f_value 


    if link_id != "" and subreddit != "":
      print("{}\t{}\t{}".format(subreddit, 1 , link_id))
      
