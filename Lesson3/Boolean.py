print("Hello World!") 
print('Have a good day.')
print("I am ",35," years old.")
x= int(3);
print ("x=",x);
x="sophea"
print("x=",x)
name= "In Sophea"
age=39
adress='Phnom Penh'
print("My Name is "+name," Age="+str(age)," adress="+adress)
#use f-string
print(f"My name {name},My Age{age},\nMy Address{adress}")
pi=3.14159
print(f"{pi:.3f}")
lstNumber=['a',123,'c',"d"]
print(lstNumber)
print(lstNumber[1])
lstNumber.insert(4,"e")
print(lstNumber[4])
day_of_week=("Mon","Tue","Wed","Thu","Fri","Sat","Sun")#fixed data
m,t,w,th,f,s,su=day_of_week
print(f)
num={"a","b","c"}
x=-1
for item in num:
    x+=1
    print(x,item)
    