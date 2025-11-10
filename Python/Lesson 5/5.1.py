# 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, 
# ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი; თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა დაასრულოს მუშაობა.
#  მიღებული შედეგი დაბეჭდეთ კონსოლში.

# a – append

# r – remove

# e – exit

# გამოიყენეთ მხოლოდ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.

list1 = []

while True:
    symbol = input("choose a, r or e: ")
    if symbol == 'a':
        number = int(input('enter a number: '))
        list1.append(number)
        print("list:",list1)
    elif symbol == 'r':
        number = int(input('enter a number: '))
        if number in list1:
            list1.remove(number)
        else:
            print('value not found in thelist')
        print("list: ",list1)
    elif symbol =='e':
        break
    else:
        print('wrong symbol, enter only a, r or e')



# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list_1 = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს შემდეგ ნაბიჯებს:

# a. დაბეჭდავს 210-ის ინდექსს;
 
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";

# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;

# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.

# მინიშნება: სიის გასუფთავება – arr.clear()

my_list_1 = [43, '22', 12, 66, 210, ["hi"]]
print(my_list_1)

index1 = my_list_1.index(210)
print(index1)

my_list_1[-1].append("Hello")
print(my_list_1)

my_list_1.pop(2)
print(my_list_1)

my_llist_2 = my_list_1.copy()

my_llist_2.clear()

print(my_list_1)
print(my_llist_2)



# 3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, 
# თუ იცავს დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში გამოიტანეთ "Invalid format" ტექსტი.

# მინიშნება: სრული დამთხვევისთვის გამოიყენეთ .fullmatch() მეთოდი re მოდულიდან.

import re
phone = input('input number with format:"(123) 456-789": ')
pattern = r"\(\d{3}\)\s\d{3}-\d{3}"
if re.fullmatch(pattern, phone):
    print("validformat:", phone)
else:
    print("Invalid format")