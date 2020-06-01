import sys
user1= input("Please tell me what's your name?")
user2= input("and your name :")
user1_answer=input("%s what do you want to choose stone,paper or scissors?:" %user1)
user2_answer=input("%s what do you want to choose stone,paper or scissors?:" %user2)
#comparing the inputs
def compare(u1,u2):
    if (u1==u2):
        return ("it's a tie")
    elif u1=='stone':
        if u2=='scissors':
            return (user1,"wins:)")
        else:
            return (user2,"wins:)")
    elif u1 == 'scissors':
        if u2 == 'paper':
            return (user1, "wins:)")
        else:
            return (user2, "wins:)")
    elif u1 == 'paper':
        if u2 == 'stone':
            return (user1, "wins:)")
        else:
            return (user2, "wins:)")
    else:
        return  ("Invalid Input!,You have to ener stone, paper or scissors,please try once again")
        sys.exit()
print(compare(user1_answer,user2_answer))