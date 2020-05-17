# from random import randint
# random_num = randint(0, 100)
# if random < 30:
#     print("Bạn trông bình thường")
# elif random_num <30 


# Bài toán BMI
# height = int(input("Enter height in centimeters: "))
# weight = int(input("Enter weight in kg: "))

# bmi = weight/((height/100)**2) 

# if bmi < 16:
#    print("severely underweight")

# elif bmi >= 16 and bmi < 18.5:
#    print("underweight")

# elif bmi >= 18.5 and bmi < 25:
#    print("Normal")

# elif bmi >= 25 and bmi < 30:
#    print("overweight")

# elif bmi >=30:
#    print("Obese")

# Bài toán Factorial
# n=int(input("Input a number to compute the factiorial : "))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(n))

# Bài tập turtle
# from turtle import*
# speed(-1)
# for i in range(3,7):
#     for j in range(i):
#         forward(100)
#         left(360/i)
# mainloop()

# n = 5
# for x in range(1, (n+5) //2 + 1):
#     for y in range( (n+5) //2 - x):
#         print(" ", end = "")
#     for z in range( (x*2)-1 ):
#         print("*", end = "")
#     print()

# for x in range( (n+5)// 2 + 1, n + 5):
#     for y in range(x - (n+5) //2):
#         print(" ", end = "")
#     for z in range( (n+5 - x) *2 - 1):
#         print("*", end = "")
#     print()

# Bài tập multiplication table
# n = int(input("Enter a number"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j*i, end ="\t") 
#     print("\n")  

# Number từ 0 đến 19:
# for i in range(20):
#     print(i, end=" ")

# Enter a number = 17
# n = int(input(""))
# for i in range(n):
#     print(i, end=" ")


# Number 1’s and 0’s, consecutively
# for i in range(21):
#     if i%2 == 0:
#         print("1", end=" ")
#     else:
#         print("0", end=" ")

# Enter a number 19
# n = int(input(""))
# for i in range(21):
#     if i%2 == 0:
#         print("1", end=" ")
#     else:
#         print("0", end=" ")

n = int(input("Enter a number"))
for i in range(1,n+1):
    if i%2 ==0:
        for j in range(1,n+1):
            if j%2 == 0:
                print("0", end="  ")
            else:
                print("1", end="  ")
        print("\n")
    else:
        for j in range(1,n+1):
            if j%2 == 0:
                print("1", end="  ")
            else:
                print("0", end="  ")
        print("\n")



