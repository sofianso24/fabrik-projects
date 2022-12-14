analyse = float(input("enter your analyse mark :"))
algorithms = float(input("enter your algorithms mark :"))
database = float(input("enter your database mark :"))
if analyse > 20 or algorithms > 20 or database > 20:
    print("enter a mark less than 20")
else :     
    sum = analyse + algorithms + database 
    average = round(sum/3,2) 
    if analyse <= 5 or algorithms <= 5 or database <= 5 :
        print("you are exclude")     
    elif average < 10 :  
        print("your average score is :",average," ,you have failed")
    elif 10 <= average < 15 :  
        print("your average score is :",average, ",good")
    elif 15 <= average <= 20 :
        print("your average score is :",average,",verry good")
    else : 
        print("not found")    

