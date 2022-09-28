
first_input = input("enter your first number: ")
second_input = input("enter your second number: ")

app_options = " 1_+\n 2_-\n 3_*\n 4_/\n 5_^\n 6_% "
if first_input.isdigit() and second_input.isdigit():
    print(app_options)
    user_operation = input('please enter you choice: ')

first_casted_input = int(first_input)
second_casted_input = int(second_input)
result = 0
is_success = False

if user_operation =="+" or user_operation == "1":
            result = first_casted_input + second_casted_input
            print(result)
            is_success = True
elif  user_operation =="-" or user_operation == "2":
            result = first_casted_input - second_casted_input
            print(result)
            is_success = True
elif  user_operation =="*" or user_operation == "3":
            result = first_casted_input * second_casted_input
            print(result)
            is_success = True
elif  user_operation =="/" or user_operation == "4":
            result = first_casted_input / second_casted_input
            print(result)
            is_success = True
elif  user_operation =="^" or user_operation == "5":
            result = first_casted_input ^ second_casted_input
            print(result)
            is_success = True
elif  user_operation =="%" or user_operation == "6":
            result = first_casted_input % second_casted_input
            print(result)
            is_success = True
else:
         print("invalid input,please try again")

print(result.__round__())
print(result.__floor__())
print("exist")

