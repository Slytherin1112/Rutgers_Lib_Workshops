#Exercise 1
#Print out "b is larger than a.
# b-a=x" or "a and b are equal.
# a = b = x".
# x shows the result of "b-a" or the value of "a" and "b".
a = 450
b = 76
c = 23

if a > b:
    print ("a is larger than B.", "a-b=", a-b)
elif a == b:
    print("a and b are equal.", "a = b =", a)
else:
    print("a is smaller than b")


#Exercise 2
# In this program, we input a number
# check if the number is positive or
# negative or zero and display
# an appropriate message
# This time we use nested if
#a = input("Enter:")
#print(type(a))

num = int(input("Enter a number: "))
if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")

#Exercise 4: Make a small program that helps you make decisions.
#Program that tells you how much money you're making or losing in stock market
Balance = float(input("Your account balance:")) #original balance in your bank account
Bal_week1 = [float(input("Day1:")), float(input("Day2:")),float(input("Day3:")),float(input("Day4:")),float(input("Day5:"))]
My_portfolio = []
for i in Bal_week1:
    if i < Balance:
        My_portfolio.append(int(i-Balance))
    elif i > Balance:
        My_portfolio.append(int(i - Balance))
    else:
        My_portfolio.append('-')
print(My_portfolio)

#Determine how many students fail/passed an exam
grades=[70, 86, 40, 94, 100, 83, 60, 42, 70, 98, 30, 55]
passed=0
failed=0

for i in grades:
  if i>=55:
    passed += 1
  else:
    failed += 1
print("There are ",passed,"students who passed the test")
print("There are ",failed,"students who failed the test")
