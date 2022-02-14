print("Welcome to the pizza deliveries")

#Here i store the size input as S, M and L, so that i may use those variables later in the code.
size = input("What size pizza would you like? S, M, or L: ")

#Here i store the price into those variables i want to store in S, M and L.
S = 50
M = 80
L = 100

#Here we store the variables Y and N for pepperoni to later be able to assign a call to them.
pepperoni = input("Would you like some pepperoni? Y or N: ")

cheese = input("Would you like some cheese? Y or N: ")

#Here the if statement sums up the total needed with the variables stored for them to make it easier.
#For Small sized pizzas
if size == "S" and pepperoni == "Y" and cheese == "Y":
    print("Your final bill is $75")
    
if size == "S" and pepperoni == "N" and cheese == "N":
    print("Your final bill is $50")
    
if size == "S" and pepperoni == "Y" and cheese == "N":
    print("Your final bill is $65")
    
if size == "S" and pepperoni == "N" and cheese == "Y":
    print("Your final bill is $65")
 
#For Medium sized pizzas.
if size == "M" and pepperoni == "Y" and cheese == "Y":
    print("Your final bill is $120")
    
if size == "M" and pepperoni == "N" and cheese == "N":
    print("Your final bill is $80")
    
if size == "M" and pepperoni == "Y" and cheese == "N":
    print("Your final bill is $105")
    
if size == "M" and pepperoni == "N" and cheese == "Y":
    print("Your final bill is $95")
 
#And for Large sized pizzas.
if size == "L" and pepperoni == "Y" and cheese == "Y":
    print("Your final bill is $135")
    
if size == "L" and pepperoni == "N" and cheese == "N":
    print("Your final bill is $100")
    
if size == "L" and pepperoni == "Y" and cheese == "N":
    print("Your final bill is $125")
    
if size == "L" and pepperoni == "N" and cheese == "Y":
    print("Your final bill is $115")
    
#You always just have to store the right amounts in your variables always. Or the program won't work.