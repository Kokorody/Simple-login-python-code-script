credentials ={
    "KEMAS": "palembang123",
    "CCIT": "ftui",
    "G512": "strix"
}

max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in credentials:
        if credentials[username] == password:
            print("Login successful. Welcome, " + username + "!")
            break
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username not found. Please try again.")

    attempts += 1

if attempts == max_attempts:
    print("You've reached the maximum number of login attempts. Access denied.")  
