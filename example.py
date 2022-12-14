rainy = input("is the weather rainy? yes/no\n " )

if rainy == "yes":
    print("stay indoor")
    power = input("do you have the power in the house ? yes/no\n") 
    if power =="yes"  :
        print("watch netflix")
    else :
        print("read novel")    
     
elif rainy == "no" :
    print("go out")
    too_hot = input("is it too hot ? yes/no\n")
    if too_hot =="yes":
        print("visit mall")
    else:
        print("visit garden")    
     














