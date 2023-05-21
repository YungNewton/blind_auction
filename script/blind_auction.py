import time

dictionary = {}
print('welcome to the blind auction program')
time.sleep(1)
is_next = True
while is_next:
    name = input("what's your name? : ")
    bid = int(input(f"what's your bid {name}: "))
    dictionary[name] = bid
    is_bidder = input("is there another bidder?\nEnter 'y' for yes and 'n' for no: ")
    if is_bidder.lower() in ['n', 'no']:
        is_next = False
