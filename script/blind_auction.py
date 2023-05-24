import time
import os

dictionary = {}
winner = ''
the_max = 0
time.sleep(1)
is_next = True
while is_next:
    os.system('clear')
    print('welcome to the blind auction program')
    name = input("what's your name? : ")
    bid = int(input(f"what's your bid {name.lower()} : $ "))
    dictionary[name] = bid
    is_bidder = input("is there another bidder?\nEnter 'y' for yes and 'n' for no: ")
    if is_bidder.lower() in ['n', 'no']:
        os.system('clear')
        is_next = False
for i in dictionary:
    if dictionary[i] > the_max:
        the_max = dictionary[i]
        winner = i
time.sleep(1)
print('____________________________________')
print()
print(f"The winner of the Auction was {winner} with a bid of {the_max}!")
