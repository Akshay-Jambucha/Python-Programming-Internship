# Name : Jambucha Akshaybhai Mansukhbhai 
# task 2
import csv

# 1. Add Expense - Take input & save to CSV file.
def add_expense(description, amount):
    f=open("expense.csv","a",newline="")
    add=csv.writer(f)
    add.writerow([description,amount])

# 2. View Expenses - Read and display all expenses from CSV.
def check_expenses():
    with open("expense.csv","r") as f:
        for i in csv.reader(f):
            print(f"Item: {i[0]}, Amount: â‚¹{i[1]}")

# 3. Total Expenses - Calculate and display total spent.
def total_expenses():
    total=0
    with open("expense.csv","r") as f:
        for i in csv.reader(f):
            total +=int(i[1])
    print(f"Total Expenses: â‚¹ {total}")


print(": Welcome To Expense Tracker :\n")
while True :
    print("1. Add Expense")
    print("2. List of all Expenses")
    print("3. Get total expenses")
    print("4. Exit\n")
    i=int(input("Select any one :"))
    print("\n")

    if i==1:
        description=input("Enter expense description :")
        Amount=int(input("Enter amount: â‚¹"))
        add_expense(description, Amount)
    elif i==2:
        check_expenses()
    elif i==3:
        total_expenses()
    elif i==4 :
        break
    else :
        print("Please enter valid choice !")
    print("\n")
    