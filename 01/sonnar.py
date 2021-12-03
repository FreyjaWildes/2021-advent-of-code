previous_depth = -1
increase_count = 0
"""
Let the lines be numbered: w1 w2 w3 w4
and windows be named A, B, C...
A-B = w1 - w4
B-C = w2 - w5
"""
window = [-1,-1,-1]
with open("input.txt", 'r') as input:
    for (idx,line) in enumerate(input):
        depth = int(line)
        previous_depth = window[idx % 3] 
        if (previous_depth > -1 and previous_depth - depth < 0):
            increase_count += 1
        window[idx % 3] = depth
        
print(f"Increased: {increase_count}")
