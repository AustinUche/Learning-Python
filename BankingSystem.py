print("Welcome to The German Bank")
ask = input("Do you have an account?Type Y or N ")
lower_ask = ask.upper()
at = "@"
com = ".com"
if lower_ask == "Y":
    email_log = input("Enter your email: ")
    if at in email_log and com in email_log:
        pass_log = input("Enter your password: ") 
        print("Login Successful")
    else:
        print("Invalid email")
else:
    email_sign = input("Enter email: ")
    if at in email_sign and com in email_sign:
        pass_sign = input("Enter password: ")
        pass_sign_confirm = input("Confirm password: ")
        if pass_sign == pass_sign_confirm:
            print("Account created successfully")
        else:
            print("Passwords must match")
    else:
        print("Invalid email")