import collections



def duplicate_count(text):
    # Your code goes here
    # Check if the alphabet repeats
    
    frequencies = collections.Counter(text)
    repeated = {}
    count = 0
    
    for k, v in frequencies.items():
        if v > 1:
            repeated[k] = v
            count += 1
    
    
    print(count)
     
     
duplicate_count("hello kitty lll fff")