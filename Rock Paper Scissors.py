import random

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Welcome to Rock Paper Scissors Game !!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

j=int(input("Enter the number of points you wanna play -->"))

print(f"Whoever scores more points in {j} rounds wins >>>")
c=0
p=0

for k in range(j):
    print("______________________________________________")
    i=int(input("Enter 1 for Rock | 2 for Scissors | 3 for Paper\nEnter your choice-->"))
    
    d={1:"Rock",2:"Scissors",3:"Paper"}
    r=random.randint(1,3)

    


    if i==r:
        print(f"You choose {d[i]} and Computer also choose {d[r]} soo its a Tie")
        print("______________________________________________")
    elif (i==1 and r==2) or (i==2 and r==3) or (i==3 and r==1):
        print(f"You choose {d[i]} and Computer choose {d[r]} soo You Wins")
        print("______________________________________________")
        p+=1
    else:
        print(f"You choose {d[i]} and Computer choose {d[r]} soo Computer Win")
        print("______________________________________________")
        c+=1
        
print(f"Final score, You : {p}| Computer : {c}")
if c>p:
    print("Computer wins")
elif c==p:
    print("Its a Tie")
else:
    print("Congrats!! You Wins")


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Thanks for Playing !!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




