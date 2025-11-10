chess_players = [
  {'id': 19, 'name': 'Jobava', 'country': 'Georgia', 'rating': 2588, 'age': 41},
  {'id': 28, 'name': 'Caruana', 'country': 'USA', 'rating': 2781, 'age': 32},
  {'id': 35, 'name': 'Giri', 'country': 'Netherlands', 'rating': 2771, 'age': 30},
  {'id': 84, 'name': 'Carlsen', 'country': 'Norway', 'rating': 2864, 'age': 34},
  {'id': 118, 'name': 'Ding', 'country': 'China', 'rating': 2799, 'age': 32},
  {'id': 139, 'name': 'Karjakin', 'country': 'Russia', 'rating': 2747, 'age': 35},
  {'id': 258, 'name': 'Duda', 'country': 'Poland', 'rating': 2731, 'age': 31},
  {'id': 301, 'name': 'Vachier-Lagrave', 'country': 'France', 'rating': 2737, 'age': 34},
  {'id': 403, 'name': 'Nakamura', 'country': 'USA', 'rating': 2768, 'age': 36},
]

import os

def create_file(folder_path, file_name):
    try:
        file_path = os.path.join(folder_path, file_name)
        
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write("")
        
        print(f"ფაილი წარმატებით შეიქმნა: {file_path}")
        return file_path

    except FileNotFoundError:
        print("მითითებული საქაღალდე ვერ მოიძებნა!")
    except PermissionError:
        print("არ გაქვს ნებართვა ამ საქაღალდეში ფაილის შესაქმნელად!")
    except Exception as e:
        print(f"დაფიქსირდა სხვა შეცდომა: {e}")
create_file("C:/Users/s.siprashvili/OneDrive - Adjarabet/Desktop/Python/Lesson 12", "chess_players.txt")


import json

def writechessplayers(file_path,data):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError('ფაილი არ არსებობს')
        
        with open(file_path,'w',encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"მონაცემები წარმატებუთ ჩაიწერა ფაილშო: {file_path}")
    except FileNotFoundError as e:
        print(f"{e}")
    except PermissionError:
        print("წვდომა შეზღუდულია")
    except Exception as e:
        print("შეცდომა {e}")
file_path = "C:/Users/s.siprashvili/OneDrive - Adjarabet/Desktop/Python/Lesson 12/chess_players.txt"
writechessplayers(file_path,chess_players)

# 1. დაწერეთ პითონის ფუნქცია რომელიც კონტექსტის მენეჯერის გამოყენებით პარამეტრად მიიღებს ფაილის საქაღალდის მისამართს, ფაილის სახელს და შემქნის მას.

# 2. დაწერეთ პითონის ფუნქცია რომელიც წაიკითხავს პარამეტრად მიღებული ფაილის კონტენტს.

def read_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content

    except FileNotFoundError:
        return "ფაილი ვერ მოიძებნა"
    except PermissionError:
        return "ფაილის წაკითხვის ნებართვა არ გაქვს"
    except Exception as e:
        return f"დაფიქსირდა სხვა შეცდომა: {e}"
text = read_file("C:/Users/s.siprashvili/OneDrive - Adjarabet/Desktop/Python/Lesson 12/chess_players.txt")
print(text)    
    # 3. დაწერეთ პითონის ფუნქცია რომელიც პარამეტრად მიიღებს ლექსიკონს (dict) და ჩაწერს/გაანახლებს ფაილის კონტენტს.

# [
#   {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
#   {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59},
# ]

# ბოლოში უნდა ჩაემატოს მხოლოდ ორი ლექსიკონი და არა სია.

def updatechessplayers(file_path,new_data):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("ფაილი ვერ მოიძებნა")
        with open(file_path,'r',encoding='utf-8') as file:
            data = json.load(file)
        if not isinstance(data,list):
            raise TypeError('მონაცემი სია არ არის')
        if isinstance(new_data,list):
            data.extend(new_data)
        else:
            data.append(new_data)
        with open(file_path,'w',encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print('დამატებულია')
    except FileNotFoundError as e:
        print(f"შეცდომა {e}")
    except json.JSONDecodeError:
        print("empty or non-json format")
    # except Exception as e:
    #     print("შეცდომა: {e}")

new_players = [
  {'id': 568, 'name': 'Kasparov', 'country': 'Russia', 'rating': 2705, 'age': 56},
  {'id': 189, 'name': 'Karpov', 'country': 'Russia', 'rating': 2698, 'age': 59}
]

file_path = "C:/Users/s.siprashvili/OneDrive - Adjarabet/Desktop/Python/Lesson 12/chess_players.txt"

updatechessplayers(file_path,new_players)


# 4. დაწერეთ პითონის ფუნქცია, რომელიც გაანახლებს ფაილში არსებულ კონტენტს.

def overwrite_file_content(file_path, new_data):
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("ფაილი არ არსებობს")

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)

        print("ფაილის კონტენტი წარმატებით განახლდა!")

    except FileNotFoundError as e:
        print(f"შეცდომა: {e}")
    except PermissionError:
        print("არ გაქვს ნებართვა ფაილში ჩასაწერად!")
    except Exception as e:
        print(f"დაფიქსირდა შეცდომა: {e}")

file_path = "C:/Users/s.siprashvili/OneDrive - Adjarabet/Desktop/Python/Lesson 12/chess_players.txt"

new_content = [
  {'id': 900, 'name': 'sal', 'country': 'Geo', 'rating': 3500, 'age': 2},
  {'id': 901, 'name': 'nana', 'country': 'Geo', 'rating': 3550, 'age': 3}
]

overwrite_file_content(file_path, new_content)