# Import the clear function from the replit module, which allows us to clear the console
from replit import clear

# Import the logo from the art module, which we'll print at the beginning of the program
from art import logo

# Print the logo to the console
print(logo)

# Initialize an empty dictionary to store the bids, where the keys are bidder names and the values are bids
bids = {}

# Define a function to prompt the user for their name and bid, and add it to the bids dictionary
def info():
    name = input("What is your name: ")
    bid = float(input("What is your bid: "))
    bids[name] = bid

# Call the info function once to get the first bid
info()

# Prompt the user if there are more bidders
more_bidders = input("Are there more bidders? (yes/no) ").lower()

# Keep calling the info function as long as there are more bidders
while more_bidders == "yes":
    clear() # Clear the console
    info() # Prompt the user for the next bid
    more_bidders = input("Are there more bidders? (yes/no) ").lower() # Prompt the user if there are more bidders

# Find the highest bid and bidder using the max function on the bids dictionary
highest_bidder = max(bids, key=bids.get)
highest_bid = bids[highest_bidder]

# Print out the name and bid of the highest bidder
print(f"The winner is {highest_bidder} with a bid of ${highest_bid:.2f}.")
