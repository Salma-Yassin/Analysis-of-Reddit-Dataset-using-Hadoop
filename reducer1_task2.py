# reducer:

import sys
out = {}

for line in sys.stdin:

    line = line.strip()
    link_id, controversiality = line.split("\t")
    controversiality = int(controversiality)
    if link_id in out:
        out[link_id][0] += controversiality
        out[link_id][1] += 1

    else:
        out[link_id] = []
        out[link_id].append(controversiality)
        out[link_id].append(1)


out = {k:v for k,v in sorted(out.items() , key = lambda x: x[1][1], reverse = True)}

for key in out.keys():
  print("{}\t{}\t{}".format(key, out[key][0], out[key][1]))

