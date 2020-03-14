answer_user = input("Hellow! I'm a new programm. I suggest you to solve an expression. Here it is : 4*100-54 = ")
answer = str(4*100-54)
print("So, I've also solved this expression. This is my answer : {0}. And this this yours : {1}." .format(answer,answer_user))
if answer_user == answer :
    print("We are both right. My congratulations! :)")
else :
    print("Your answer is wrong, sorry :(")

