"""Command Line Interface(CLI) => Python-Based login system that uses 
regular expressions to authenticate emails and validate passwords"""
import re
username = input("Enter your username: ")
print(f"Username:{username}")
count = 3
attempt = 3
counter = 4
passwordChecker = False
while True:
    email = input("Enter your email: ")
    pattern = r"^[a-z0-9]+@[a-z]+\.[a-z]{2,}$"
    n = re.search(pattern, email)
    if n:
        print(f"Email: {n.group()}")
        break
    else:
        count-=1 
        if count > 0:
            print(f"You have {count} trial(s) left")
        else:
            print("Try again later\n\n")
            break
def password_checker(user_input):
    if len(user_input) < 8:
        return "Password length must be greater than 8"
    if not re.search(r"[A-Z]", user_input):
        return "Password must contain at least an Upper Case"
    if not re.search(r"[a-z]", user_input):
        return "Password must contain at least a Lower Case"
    return "Strong Password"
while not passwordChecker:
    user = input("Enter your Password: ")
    result = password_checker(user)
    print(result)
    if result == "Strong Password":
        passwordChecker = True
    elif counter > 1:
        counter-=1
        print(f"You have {counter} attempt(s) left")
    else:
        print("Too Much Attempt, Please Try again later")
        passwordChecker = True
