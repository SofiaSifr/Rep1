# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად ერთიდაიგივე ზომის სიას (list) და zip ფუნქციის გამოყენებით
#  დააჯგუფეთ სიების ელემენტები.

# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

def group_lists(list1, list2):
    group = list(zip(list1, list2))
    return group

result = group_lists(list1,list2)
print(result)

# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს.
#  ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5] 
# output: 120

from functools import reduce

def multiply_list(numbers):
    try:
        if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
            raise TypeError("ჩაწერეთ რიცხვების სია!")

        result = reduce(lambda x, y: x * y, numbers)
        return result

    except TypeError as e:
        return str(e)
print(multiply_list([1, 2, 3, 4, 5]))


# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

kenti = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))
list3 = [1, 2, 3, 4, 5, 6, 7]
print(kenti(list3))

# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს (ending). 
# დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. 
# გაითვალისწინეთ გამონაკლისები (TypeError), თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი, რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

def filter_by_ending(words, ending):
    try:
        if not isinstance(words, list) or not isinstance(ending, str):
            raise TypeError("პარამეტრები უნდა იყოს სია და სტრიქონი!")
        
        if not all(isinstance(w, str) for w in words):
            raise TypeError("სიის ყველა ელემენტი უნდა იყოს სტრიქონი!")

        result = list(filter(lambda w: w.endswith(ending), words))
        return result

    except TypeError as e:
        return f"შეცდომა: {e}"
    except Exception as e:
        return f"დაფიქსირდა სხვა შეცდომა: {e}"
print(filter_by_ending(['hello', 'world', 'coding', 'nod'], 'ing'))