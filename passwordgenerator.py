import random
from string import digits
from string import punctuation
from string import ascii_letters

symbol = ascii_letters + digits + punctuation
secure=random.SystemRandom()
password="".join(secure.choice(symbol) for i in range(30) )
print(password)