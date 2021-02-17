#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied
"""

input str (username)
input str (password)

while username != "admin" and password != "12345":
    username = input("What is the username and password?")
    if username != "admin" or password != "12345":
        print("Access denied")

print("Access granted")