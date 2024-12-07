import random
def hangman():
    words=["apple","helicopter","orange","elephant","we","hangman","monkey"];
    word=random.choice(words);
    guesses=[];
    tries=10;
    
    while tries>0:
        status="";
        for letter in word:
            if letter in guesses:
                status += letter
            else:
                status += "_"
        print(status)
        
        guess=input("guess the word what comes in your mind please")
        if guess in guesses:
            print("you already guess this letter ")
        elif guess in word:
            print("you guessed it right ")
            guesses.append(guess)
        else:
            print("you are wrong ")
            tries -= 1
        if "_" not in status:
            print("you won ")
            return
            
        print(f"{tries} tries left.")
    print("you lost the word is ",word)
hangman()