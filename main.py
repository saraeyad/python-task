print("Hello")
welcoming_sentence = "Hello Ms/Mr"
name = input("enter your name : ")
if name.isalpha():
    pass
else: print("enter a real name")
age = input("enter your age : ")
if age.isdigit():
    pass
else: print("enter a number")
located_in = input("your address : ")
final = "Thanks for being one of our community,    Enjoy"
print(welcoming_sentence + " " + str(name) + " " + str(age)+" "+ located_in+" " + final)
if name is None and age is None and located_in is None:
    print("there is an error")
    exit()



