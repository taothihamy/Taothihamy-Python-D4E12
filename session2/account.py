account_username = "mindx"
account_password = "mindx123"

running = True
while running:
    username = input("username")
    password = input("password")
    if username == account_username and password == account_password:
        print("Welcome")
        break
        print("break sẽ giúp nó dừng thay cho running = false")
    else:
        print("sai acc rồi kaka")