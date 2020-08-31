import itertools,random
cards = [{"♦":"diamond"},{"♣":"club"},{"♥":"heart"},{"♠":"spade"}]
deck = list(itertools.product(range(1,14),cards))

random.shuffle(deck)

no_of_cards = int(input("enter the number of cards you want"))
print("You got:",end="")
print(" ")
for i in range(no_of_cards):
    print(deck[i][0] ,"of", deck[i][1])
