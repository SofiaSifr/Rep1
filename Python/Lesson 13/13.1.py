# შექმენით csv  ფაილი რომელშიც გექნებათ შემდეგი სტრუქტურის მონაცემები:

# id,name,age,grade,subject_name,mark
# 1,string,0,string,string,0
# 2,string,0,string,string,0

import csv
import os
def createcsvfile(file_path):
    try:
        folder = os.path.dirname(file_path)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)
        data = [
            ["id", "name", "age", "grade", "subject_name", "mark"],
            [1, "string", 0, "string", "string", 0],
            [2, "string", 0, "string", "string", 0]
        ]
        with open(file_path,mode ='w', newline="",encoding="utf-8") as file:
            writer=csv.writer(file)
            writer.writerows(data)
        print(f"csv ფაილი წარმატებით შეიქმნა")
    except Exception as e:
        print(f"შეცდომა: {e}")
file_path = "Downloads/students.csv"
createcsvfile(file_path)

# 1. დაწერეთ პითონის ფუნქცია, სადაც მომხარებელი შეიყვანს ინფორმაციას(id,name,age,grade,subject_name,mark) და თქვენ სტუდენტს დაამატებს csv ფაილში. დაასორტირეთ მონაცემები id-ის მიხედვით.
import os
def add_student_to_csv(file_path):
    try:
        student_id = int(input("შეიყვანეთ ID: "))
        name = input("შეიყვანეთ სახელი: ")
        age = int(input("შეიყვანეთ ასაკი: "))
        grade = input("კლასის დონე: ")
        subject_name = input("საგნის დასახელება: ")
        mark = float(input("ქულა:"))

        new_student = [student_id, name, age, grade, subject_name, mark]
        data = []
        if os.path.exists(file_path):
            with open(file_path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                data = list(reader)
        header = ["id", "name", "age", "grade", "subject_name", "mark"]
        if not data:
            data.append(header)
        else:
            if data[0] != header:
                data.insert(0, header)
        data.append(new_student)
        sorted_data = [data[0]] + sorted(data[1:], key=lambda x: int(x[0]))
        with open(file_path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(sorted_data)
        print("correct")
        
    except ValueError:
        print("შეყვანილია არასწორი ტიპის მონაცემბი")
    except PermissionError:
        print("no permission")
    except Exception as e:
        print(f"შეცდომა")

file_path = "students.csv"
add_student_to_csv(file_path)
# 2. დაწერეთ პითონის ფუნქცია, რომლის საშულებით მომხარებელს შეეძლება, როგორც ყველა, ასევე კონკრეტული სტუდენტის ინფორმაციის წაკითხვა ფაილიდან.

# 3. დაწერეთ პითონის ფუნქცია, რომელიც დაითვლის საშუალო ქულას (mark) საგნების მიხედვით.

# 4. დაწერეთ პითონის ფუნქცია, რომლის საშუალებით შესაძლებელი იქნება სტუდენტის ქულის განახლება/ცვლილება. მომხარებელი შეიყვანს სტუდენტის id, საგანს და განახლებულ ქულას.