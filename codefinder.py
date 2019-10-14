"""Codefinder Minigame
You have to guess the number within a certain numer of tries.
The game tells you the number of positions you guessed correctly after each try.
   """

# TODO: make variables into parameters

def codefinder():
    code_elements = ['5', '4', '5', '2']
    tries = 10
    correct_ratio = 0
    
    
    print("Guess the 4-digit code.")

    while tries > 0:
        current_guess = input("Guess: ")
        guess_elements = list(current_guess)
        all_elements = zip(code_elements, guess_elements)

        correct_ratio = len(([code_digit for code_digit, guess_digit in all_elements if code_digit == guess_digit]))
        
        if correct_ratio == 4:
            print("Correct!")
            return True
        
        else:
            tries -= 1
        
        print(f"You got {correct_ratio} positions correct!")
        print(f"You got {tries} tries left!")
        


    print("You ran out of tries")
    return False

codefinder()
    