# mapper 

import sys

for line in sys.stdin:

    line = line.lower().strip().replace('"','').replace('}','')
    items = line.split(",")
    
    topic = ""
    controversiality = ""

    for item in items:
        try: 
          field,f_value = item.split(":")
        except: 
          continue

        if field == 'link_id':
            topic = f_value 
            #print(type(topic),count)
        if field == 'controversiality':
            controversiality = f_value 
            #print(topic)

    if topic != "" and controversiality != "":
      print("{}\t{}".format(topic , controversiality))
      
      
