stuName=""; sc_khmer=0.0; sc_Mathematics=0.0; sc_English=0.0; tot_score=0.0
lstStudent = []
index=-1
opt=True
while opt:
    stuName = input("Enter Student Name:")
    sc_khmer = float(input("Enter Khmer Score:"))
    sc_Mathematics = float(input("Enter Mathematics Score:"))
    sc_English = float(input("Enter English Score:"))
    tot_score = float((sc_khmer + sc_Mathematics+ sc_English)/3)
    if tot_score <=30:
        print(stuName,",your great is F.")
    elif tot_score <= 40:
        print(stuName,",your great is E.")
    elif tot_score <= 50:
        print(stuName,",your great is D.")
    elif tot_score <= 60:
        print(stuName,",your great is C.")
    elif tot_score <= 80:
        print(stuName,",your great is B.")
    else:
        print(stuName,",your great is A.")         
    index+=1
    lstStudent.insert(index,{"Name": stuName, "Khmer": sc_khmer, "Mathematics": sc_Mathematics,"English":sc_English, "Total_Score":tot_score})
    pKey= input("Do you want to continue(y/n)?")
    if pKey=="y" or pKey=="Y":
        opt=True
    else:
        break