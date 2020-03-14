
user_text1 = input()
user_text2 = input()
if type(user_text1) == str or type(user_text2) == str:
    print(str(user_text1) + " " + str(user_text2))
else:
    print("Первый ввод: {0}, второй ввод: {1}." .format(user_text1, user_text2))

