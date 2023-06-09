# mapper 

import sys


for line in sys.stdin:

    line = line.lower().strip().replace('"','').replace('}','')
    items = line.split(",")
    
    topic = ""
    ups = ""
    downs = ""

    for item in items:
        try: 
          field,f_value = item.split(":")
        except: 
          continue

        if field == 'link_id':
            topic = f_value 
            #print(type(topic),count)
        if field == 'downs':
            if int(f_value) >= 0 : 
              downs = f_value 
              #print(topic)
        if field == 'ups':
            if int(f_value) >= 0 : 
              ups = f_value 

    if topic != "" and downs != "" and ups != "":

      print("{}\t{}\t{}".format(topic , ups , downs))
      
