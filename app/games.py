# games- Rock Paper Scissors

# import sys

user1 = input("whats your name?")
user2 = input("and Whats your name?")

user1_answer = input("%s,do you want to choose rock, paper or scissors?" % user1)
user2_answer = input("%s,Do you want to choose rock, paper or scissors?" % user2)


# part 2 if  /else

def compare(u1, u2):
    if u1 == u2:
        return "It's tie! "
    elif u1 == 'rock':
        if u2 == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif u1 == 'scissors':
        if u2 == 'paper':
            return "scissors Wins!"
        else:
            return "Rock win!"

    elif u1 == 'paper':
        if u2 == 'rock':
            return "Paper Wins!"
        else:
            return "scissors Win!"
    else:
        return "Invalid Input!You have not entered rock, paper, scissors,try again."
        sys.exit()

# part 3
print(compare(user1_answer,user2_answer))
