# reduce:

import sys
out = {}

for line in sys.stdin:

    line = line.strip()
    topic, score  = line.split("\t")
    score = int(score)

    if topic in out:   # grouping on the topic as a key
        out[topic][0] += score 

    else:
        out[topic] = []
        out[topic].append(score)


out = {k:v for k,v in sorted(out.items() , key = lambda x: x[1], reverse = True)}

i = 0
for key in out.keys(): # print top 20 topics with their scores
  if i > 20:
    break
  print("{}\t{}".format(key.capitalize(), out[key][0]))
  i = i+1
