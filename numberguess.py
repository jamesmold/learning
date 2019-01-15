import random

def game():
    while True:
        x = random.randint(1, 9) #outer loop - runs one time until player either guesses the number or quits. If player guesses, then outer loops runs again creating a new random numnber and so on..

        while True:
            p1 = input("Enter your guess: ")
            if p1 == "q":
                break #this breaks out to the inner loop, which also checks for q and when found, breaks again - quiting the game
            elif int(p1) == x:
                print("Spot on!")
                break
            elif int(p1) < x:
                print("Too low")
            else:
                print("Too high")
        
        if p1 == "q":
            break #breaks out of the outer loop - quiting the game 
        else:
            print("New game") #otherwise starts the outer loop again, resetting the random number
            continue

if __name__ == '__main__':
    game()