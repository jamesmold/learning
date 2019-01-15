import pandas as pd

#these are the values in the table
results = [("tie", "paper", "rock"),
            ("paper", "tie", "scissors"),
            ("rock", "scissors", "tie")]

tab = pd.DataFrame(results, columns = ["rock", "paper", "scissors"], index = ["rock", "paper", "scissors"]) #and this creates the column and row headers for the table

while True:

    p1 = input("Player 1 input: ")
    if p1 == "q":
        break
    else:
        p2 = input("Player 2 input: ")

    if tab.loc[p1,p2] == p1: #this uses p1 and p2 response to lookup the value (winner) in the table
        print("Player 1 wins with", p1)
    else:
        print("Player 2 wins with", p2)