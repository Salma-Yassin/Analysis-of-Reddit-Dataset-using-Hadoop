# reducer:

import sys
out = {}

for line in sys.stdin:

    line = line.strip()
    link_id, ups , downs = line.split("\t")
    ups = int(ups)
    downs = int(downs)
    if link_id in out:
        out[link_id][0] += ups # sum upvotes related to a topic 
        out[link_id][1] += downs # sum upvotes related to a topic

    else:
        out[link_id] = []
        out[link_id].append(ups)
        out[link_id].append(downs)

# sort according to upvotes 
out_ups = sorted(out.items() , key = lambda x: x[1][0], reverse = True)

# sort according to downvotes 
out_downs = sorted(out.items() , key = lambda x: x[1][1], reverse = True)


print ("Topic that yield the highest number of upvotes")
for i in range(10): # top 10 for example
  #print ("Topic that yield the highest number of upvotes is {}\t with number of {}".format(out_ups[0], out_ups[1][0]))
  print("{}\t{}".format(out_ups[i][0], out_ups[i][1][0]))

#print ("Topic that yield the lowest number of upvotes")
#for i in range(len(out_ups)-10,len(out_ups)): # top 10 for example
  #print ("Topic that yield the highest number of upvotes is {}\t with number of {}".format(out_ups[0], out_ups[1][0]))
  #print("{}\t{}".format(out_ups[i][0], out_ups[i][1][0]))
  
#print ("Topic that yield the highest number of downvotes")
#for i in range(10): # top 10 for example
  #print ("Topic that yield the highest number of upvotes is {}\t with number of {}".format(out_ups[0], out_ups[1][0]))
  #print("{}\t{}".format(out_downs[i][0], out_downs[i][1][1]))

#print ("Topic that yield the lowest number of downvotes")
#for i in range(len(out_downs)-10, len(out_downs)): # top 10 for example
  #print ("Topic that yield the highest number of upvotes is {}\t with number of {}".format(out_ups[0], out_ups[1][0]))
  #print("{}\t{}".format(out_downs[i][0], out_downs[i][1][1]))


