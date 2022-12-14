a = int(input("enter the first number : "))
b = int(input("enter the second number : "))
print("enter 1 for the addition \n enter 2 for the substraction \n enter 3 for the multiplication \n enter 4 for the division \n the operator :")
operator = int(input(""))
if operator == 1 :
    sum = int(a) + int(b)
    print("the result of addition is : ",sum)
elif operator == 2 :
    sub = int(a) - int(b)
    print("the result of substraction is : " ,sub) 
elif operator == 3 :
    mult = int(a) * int(b)
    print("the result of multiplication is :" ,mult)    
elif operator == 4 :
    div = int(a) / int(b)
    print ("the result of division is ", div ) 

else :
    print("the operation not found")        

    