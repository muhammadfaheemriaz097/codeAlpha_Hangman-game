import random
words=["Lucky","smooth","while","system","pool"]
word=random.choice(words)
guessed_letter=[]
wrong_guesses=0
max_wrong=6
print("welcome to Hangman🙋")
while wrong_guesses<max_wrong:
    display=""
    for letter in word:
        if letter in guessed_letter:     
            display+=letter
        else:
            display+="_"
    print("\nword:",display)
    print("wrong guesses left:", max_wrong-wrong_guesses)
    #check if player won
    if display==word:
        print("you win🙌")
        break
    guess=input("guess a letter: ").lower()
    if len(guess)!=1:
        print("enter one letter.")
        continue
    if guess in guessed_letter:
        print("___you already guessed that letter___")
        continue

    guessed_letter.append(guess)

    if guess in word:
        print("correct😊")
    else:
        print("wrong 😢")
        wrong_guesses+=1
    if wrong_guesses==max_wrong:    
        print("\nGame Over😬! The word was:",word)