# 1. კონსოლიდან შეიტანეთ მიმდევრობა. დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).
# list = input("input data: ")
# list1 = list.split()
# print(list1)
# set = set(list1)
# print(set)
# 2. პირობა იგივეა, რაც პირველ დავალებაში, ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, რომლის შეცვლაც შეუძლებელი იქნება (frozenset).
# list = input("input data: ")
# list1 = list.split()
# print(list1)
# set = frozenset(list1)
# print(set)
# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).
# set1 = (1,2,3,4)
# set2 = (5,6,7,8)
# union = set1+set2
# tuple1 = tuple(union)
# print(union)

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ უნიკალური ელემენტები სიის სახით (list).
# data = input("input your data:")
# data1 = tuple(map(int, data.split()))
# set_unique = set(data1)
# list_unique = list(set_unique)
# print(list_unique)

# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# დაბეჭდეთ შემდეგი ფორმატით:

# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11

# people = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]
# for name, age in people:
#     print(f"Name: {name}, Age: {age}")

# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# დავბეჭდოთ თანხვედრა.,

users_1 = ["Irakli", "Giorgi", "Nona", "Oto"]
users_2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
set1 = set(users_1)
set2 = set(users_2)
users_inter = set1.intersection(set2)
print(users_inter)