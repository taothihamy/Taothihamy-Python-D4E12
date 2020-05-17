def hamnhap()

 a = int(input("a = "))
 b = int(input("b = "))
 c = int(input("c = "))

 return b**2 - 4*a*c
d= hamnhap()
if d < 0:
    print("phương trình vô nghiệm")
if d == 0:
    x = -b/2*a
    print("phương trình có nghiệm kép", x)
else:
    x1 = (-b + d**(1/2))/2*a
    x2 = (-b - d**(1/2))/2*a
    print("phương trình có hai nghiệm", x1, x2)


# while True:
#     print("chạy liên tục")

# account_username = "mindx"
# account_password = "mindx123"

# running = True
# while running:
#     username = input("username")
#     password = input("password")
#     if username == account_username and password == account_password:
#         print("Welcome")
#         running = False
#     else:
#         print("sai acc rồi kaka")


