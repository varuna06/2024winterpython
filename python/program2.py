current = 0
previous = 0
add = 0
for iteration in range(11): 
    print(f"Current Number {current} Previous Number {previous} Sum: {add}")  
    previous = current 
    current = current + 1
    add = current + previous
