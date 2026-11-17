students = [
    {"id": 1, "name": "Sok", "gender": "male", "score": 25},
    {"id": 2, "name": "Ryta", "gender":"female", "score": 23},
    {"id": 3, "name": "Dara", "gender":"male","score": 24},
    {"id": 4, "name": "Bopha", "gender":"female","score": 26},
]
num_elements= len(students)
opt=""
while True:
    opt = input("Option:\n"+"1. Show all students list\n"+"2. Show Female Students list\n"+"Choose 1 or 2?")
    if opt=="1" or opt=="2":
        for index in range(num_elements):
            stu_profile=""
            if opt=="1":
                for key, value in students[index].items():
                    stu_profile +=   key +": " + str(value) + "\t" 
            else:
                if students[index]["gender"] =="female":
                    for key, value in students[index].items():
                        stu_profile +=   key +": " + str(value) + "\t" 
            print(stu_profile+ "\n___________________________________________________")
        break