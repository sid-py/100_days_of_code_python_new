from art import logo # importing the art module

print(logo) # Printing the logo art


blind_auc = {}

continue_bid = True
while continue_bid == True:
    name = input("What is your name? \n")
    bid_val = int(input("What is your bid? \n$"))
    blind_auc[name] = bid_val
    other_bidders = input("Are there other bidders (yes/no)?")
    if other_bidders == "no":
        continue_bid = False

print(blind_auc)

# Finding and printing the winner
max_name = None  # Temporary variable to store max bidder name 
max_bid = None # Temporary variable to store max bid amount 
for name, bid in blind_auc.items(): # Looping over the dictionary
    if max_bid is None or bid > max_bid: # Condition to check the max bid
        max_bid = bid 
        max_name = name 
        
print(f"The winner is {max_name} with bid amount of ${max_bid}!") # Printing the result