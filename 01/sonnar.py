input = open("input.txt", 'r')
lines = input.readlines()

if len(lines) < 4 :
    exit(0)

previous_depth = -1
increase_count = 0
"""
Let the lines be numbered: w1 w2 w3 w4
and windows be named A, B, C...
A-B = w1 - w4
B-C = w2 - w5
"""
window = [-1,-1,-1,-1]
for l in range(len(lines)):
    depth = int(lines[l])
    previous_depth = window[l % 3] 
    if (previous_depth > -1 and previous_depth - depth < 0):
        increase_count += 1
    window[l % 3] = depth
        
print("Increased: {0}".format(increase_count))
input.close()
