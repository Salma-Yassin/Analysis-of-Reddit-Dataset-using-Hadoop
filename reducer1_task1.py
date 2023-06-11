import sys

# reducer 1

out = {}


for line in sys.stdin:
    line = line.strip()
    subreddit_id, count , link_id = line.split("\t")
    count = int(count)

    if subreddit_id in out:
        out[subreddit_id][0] += count 
        out[subreddit_id][1].append(link_id)

    else:
        out[subreddit_id] = []
        out[subreddit_id].append(count)
        out[subreddit_id].append([link_id])


out = sorted(out.items() , key = lambda x: x[1][0], reverse = True)

for i in range(6):
  print("{}\t{}\t{}".format(out[i][0], out[i][1][0], out[i][1][1]))


