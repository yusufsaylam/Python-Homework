##Day-3

usr_user_name = input("Please enter your username: ")
usr_user_password = input("Please enter your password: ")

user_name = "Yusuf"
user_password = "Ankara"

if user_name == usr_user_name and user_password == usr_user_password:
    print("You are now logged in!")
elif user_name != usr_user_name:
    print("This user does not exist...")
else:
    print("Your password does not match!")

##Using Dictionary 

usr_info = {"user_name" : "Yusuf", "user_password" : "Ankara"}

usr_user_name = input("Please enter your username: ")
usr_user_password = input("Please enter your password: ")

if usr_info.get("user_name") == usr_user_name and usr_info.get("user_password") == usr_user_password:
    print("You are now logged in!")
elif usr_info.get("user_name") != usr_user_name:
    print("This user does not exist...")
else:
    print("Your password does not match!")
