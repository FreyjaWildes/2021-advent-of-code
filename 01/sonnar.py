input = open("input.txt", 'r')
increase_count = 0
previous_depth = -1
lines = input.readlines()
for depthLine in lines:
    depth = int(depthLine)
    if (previous_depth >= 0 and (previous_depth - depth) < 0):
        increase_count += 1
    previous_depth = depth

print("Increased: {0}".format(increase_count))
input.close()
