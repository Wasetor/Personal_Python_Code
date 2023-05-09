username = input("Enter Username: ").lower()
password = input("Enter Password: ")

# want to write some block of codes that will check if username and password are correct
user_username: str = input("Enter Username: ").lower()
user_password = input("Enter Password: ")
# I will have to use condition statements to check the correcteness
if user_password == password and user_username == username:
    print("log in successful")
elif user_password != password and user_username != username:
    print("Incorrect username and password")
elif user_username != username:
    print("Incorrect Username")
else:
    print("Incorrect password")