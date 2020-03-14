try:
    user_text = input("Insert the number: ")
    user_text = int(user_text)
    if user_text > 0:
        print(1)
    elif user_text < 0:
        print(-1)
    elif user_text == 0:
        print(0)
except ValueError:
    print("It's necessary to insert an integer")


