# age = 56
# n = 1
# while (n <= 3):
#     guess_age = int(input("Input your guess age:"))
#     n += 1
#     if guess_age > age :
#         print("try smallere ...")
#     elif guess_age < age :
#         print("try bigger...")
#     else:
#         print("you got it")

age = 56
n = 1
while True:
    guess_age = int(input("Input your guess age:"))
    if n%3 == 0:
        choice = input("y n:")
        if choice == "y":
            n=1
            continue
        else:
            print ("byebye")
            break
    if guess_age > age :
        print("try smallere ...")
    elif guess_age < age :
        print("try bigger...")
    else:
        print("you got it")
    n += 1





