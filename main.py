import math
name = input("What is your full name: ")
sales = float(input("What was your total amount of sales this month: "))
commision = (sales * 13)/ 100
print(f' Hello {name}, this month you have sold ${sales} of merchandise, you are entitled to 13%, so your commision will be ${round(commision, 2)} ')

