# reduce:
import sys
out = {}

for line in sys.stdin:

    line = line.strip()
    topic, score  = line.split("\t")
    score = int(score)

    if topic in out: # grouping on the topic as a key
        out[topic][0] += score

    else:
        out[topic] = []
        out[topic].append(score)

for key in out.keys():
  print("{}\t{}".format(key, out[key][0]))
