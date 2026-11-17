user_acc={"user_name":"test","password":"123"}
count=0
while count<=2:
    count+=1
    uName= input("Enter User Name:")
    pwd= input("Enter Password:")
    if user_acc["user_name"]==uName and user_acc["password"]==pwd:
        print("User Name and Password are correct.")
        break
    else:
        print("User Name and Password aren't correct.", "You have", 3-count,"times.")
    
    