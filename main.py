'''
We're importing the random  module and using its sample  method which picks 6 random items from the characters  sequence. The items are stored in list chosen . Then we use a string join  method to join the list items to a string.
'''

import random
 
characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
chosen = random.sample(characters, 6)
password = "".join(chosen)
print(password)
