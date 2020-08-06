import random

pc_choice = random.randint(1,3)

if pc_choice == 1:
    pc_choice_name = "Rock"
elif pc_choice == 2:
    pc_choice_name = "Paper"
else:
    pc_choice_name = "Scissors"

k = 0
j = 0

while True:
    user_choice = (int(input("To choose Rock press 1\n"
       "To choose Paper press 2\n"
       "To choose Scissors press 3\n"
       "--------------------------------\n"
       "Choice : ")))

    if user_choice == pc_choice:
        print("Tie!!")
    elif (user_choice == 1 and pc_choice == 3) or (user_choice == 2 and pc_choice == 1) or (user_choice == 3 and pc_choice == 2):
        print("User Won!!")
        k += 1
        if k == 3:
            break
    else:
        print("PC Won!!")
        j += 1
        if j == 3:
            break

    print("PC Choice --> ", pc_choice_name)
    print("USER : {} - PC : {}\n".format(k,j))

print("PC Choice --> ", pc_choice_name)
print("USER : {} - PC : {}\n".format(k,j))