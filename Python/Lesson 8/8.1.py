# 1. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად n, და გამოიტანს ფიბონაჩის n რაოდენობის მიმდევრობას.
# Function with multiple arguments
# def fibonacci(n):
#     if n <= 0:
#         return []
#     seq = []
#     a, b = 0, 1
#     for _ in range(n):
#         seq.append(a)
#         a, b = b, a + b
#     return seq
# print(fibonacci(7))

# 2. დაწერეთ პითონის ფუნქცია, რომელიც მიიღებს პარამეტრად ორ სტრიქონს და შეამოწმებს არის თუ არა სტრიქონები ანაგრამები (ანაგრამი არის სიტყვა ან შესიტყვება, რომელიც წარმოიქმნება სხვა სიტყვის ან შესიტყვების ასოების გადაადგილებით). მაგ.: race და care ანაგრამებია.
# def anagram(str1, str2):
#     return sorted(str1) == sorted(str2)
# print(anagram("choco", "cocho")) 

# 3. დაწერეთ პითონის ფუნქცია რომელიც მიიღებს n რიცხვს და დააბრუნებს მის ფაქტორიალს.
# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(factorial(4))

# 4. დაწერეთ პითნის ფუნქცია რომელიც მიიღებს  ორ პარამეტრს, პირველს სტრიქონს და მეორეს სიმბოლოს. ფუნქციამ უნდა მოძებნოს სტრიქონში რამდენჯერ მეორდება პარამეტრად მიღებული სიმბოლო და დააბრუნოს  მისი რაოდენობა.
# def fun(string, char):
#     count = 0
#     for a in string:
#         if a == char:
#             count += 1
#     return count
# print(fun("sofo","o"))