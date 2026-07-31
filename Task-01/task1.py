# Name : Jambucha Akshaybhai Mansukhbhai 
# task 1


# 1. Sum of Two Numbers - Take input & print their sum.

a=int(input("Enter a first numbers :"))
b=int(input("Enter a second numbers :"))
sum = a + b
print(f"sum of this two numbers {a} and {b} is : {sum}")



# 2. Odd or Even Checker - Check if a number is odd/even.

a=int(input("Enter a number : "))
if a % 2 == 0 :
    print(f"Given number {a} is EVEN.")
else :
    print(f"Given number {a} is ODD.")



# 3. Factorial Calculation - Using a loop or recursion.

# ----------------Using a loop-------------------------
a=int(input("Enter a number : "))
factorial=1
while a>=1 :
    factorial= factorial * a
    a-=1
print("factorial of given number is : ",factorial)

# ----------------Using a recursion---------------------
a=int(input("Enter a number : "))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial(n-1)
print("factorial of given number is : ",factorial(a))



# 4. Fibonacci Sequence - Generate first n numbers.

x=int(input("Enter a number : "))
a,b=0,1
def Fibonacci(n):
    global a,b
    if n<=0:
        return
    else:
        print(a,end=" ")
        a,b=b,(a+b)
        Fibonacci(n-1)
print(f"first {x} numbers of fibonacci sequence is : ",end=" ")
Fibonacci(x)



# 5. String Reverse - Reverse user-input string.

str=input("Enter a string : ")
print(f"String before reverse is :{str} ")
print(f"String after reverse is :{str[ : :-1]} ")



# 6. Palindrome Check - Is the word same forward & backward?

str=input("Enter a string : ")
print("Given word is Palindrome") if str==str[: :-1] else print("Given word is not Palindrome")



# 7. Leap Year Check - Check if a given year is leap year.

year=int(input("Enter a year : "))
if year % 400 ==0 :
    print(f"{year} is a leap year.")
elif year % 100 ==0:
    print(f"{year} is not a leap year.")
elif year % 4 ==0:
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not a leap year.")



# 8. Armstrong Number - Example: 153 --> 1^3 + 5^3 + 3^3 = 153.

a=int(input("Enter a number : "))
count=0
i=a
while i>0 :
    i=int(i/10)
    count+=1

sum=0;i=a
while i>0:
    x = i%10
    sum= sum + (x**count)
    i=int(i/10)
print(f"given number {a} is armstrong number.") if sum==a else print(f"given number {a} is not a armstrong number.")