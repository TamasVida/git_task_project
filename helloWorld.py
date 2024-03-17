# git_task_project
# Practise Task 3.
# New user login function added

name = input("What is your name?: ")

message = (f"Very nice to see you again {name}!")
print(message)

login_attempt = 0
while login_attempt < 3:
    user_name = input("Please enter your username: ")
    password = input("Please enter your password")
        
    if user_name == "admin" and password == "password":
        print(f"Welcome back {name}!")
        break
    else:
        print("Your login details are incorrect, would you like to try again?")
    login_attempt += 1
    continue
