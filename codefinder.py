          
def split(sequence):                            # converts the input (string) into a list
   return list(sequence) 
   
def codefinder():
    code = "5452"
    code_elements = ['5', '4', '5', '2']
    tries = 10
    correct_ratio = 0

    print("Guess the code motherfucker!")

    while tries > 0:
        current_guess = input("Guess the number! ")
        guess_elements = split(current_guess)

        correct_ratio = len(([i for i, j in zip(code_elements, guess_elements) if i == j]))
        
        # print(code_elements)
        # print(guess_elements)
        # print(correct_ratio)
        
        if correct_ratio == 4:
            print("Correct! Congratulations motherfucker!")
            return "1"
        
        else:
            tries -= 1
        
        print(f"You got {correct_ratio} positions correct!")
        print(f"You got {tries} tries left, motherfucker!")
        


    print("You fucking died")
    return "2"