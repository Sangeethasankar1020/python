#using random model - word cuisene

import random
words=["mango","apple","orange","banana","kiwi"]

print("guess the word{}".format(words))
word=random.choice(words)
print(word)

while True:
    user =input("Enter word")
    if user not in words:
        print("this word not in list")
        continue
    if user==word:
        print("you guessed{}".format(word))
        play_again=input("do you want to continue [y/n]")

        if play_again=="y":
            continue
        else:
            break
    else:
        print("sorry ! try again")
