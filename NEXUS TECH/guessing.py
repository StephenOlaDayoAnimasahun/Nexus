while True:
    guess = int(input("Guess a number: "))
    
    if 1 < guess < 15:
        print("Failure!")
    elif 15 <= guess <= 30:
        print("Success!")
       
   