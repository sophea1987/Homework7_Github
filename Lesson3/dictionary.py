#dicCar= {"Brand":"Ford","Year":"1994","Owner":"ABC"},
#dicCar["Year"]="2026" #change
#dicCar.pop("Owner") #Remove
#for key, value in dicCar.items():
    #print(key,value)

lstStudent=[{"Name":"n1","Score":70,"Age":25},
{"Name":"n2","Score":60,"Age":28},
{"Name":"n3","Score":80,"Age":30}]

print (lstStudent[1])

age=int(input("Enter age:"))
if age>= 18:
    print("you are greater than 18")
else:
    print("you are less than 18")