from random import random


bananas_count = input("how many bananas: ")

try:
    bananas_count = int(bananas_count)
except ValueError:
    print("Bad bananas count, applying default value of 5")
    bananas_count = 20

max_rotten_bananas = int(bananas_count * 0.2)

max_rotten_bananas_count = 0
while bananas_count:
    if random() >= 0.2 <= 0.5:
        print("Banana is rotten, monkey is angry")
        max_rotten_bananas_count += 1
        print("Rotten bananas count " + str(max_rotten_bananas_count))
        continue
    if max_rotten_bananas_count == max_rotten_bananas:
        print("You are heavily injured by monkey for providing too much rotten bananas")
        break
    print("Monkey is eating the banana")
    sleep(1)