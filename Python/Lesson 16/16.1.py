# 1. შექმენით პითონის კლასი Car, ატრიბუტებით: ბრენდი, მოდელი და წელი. ასევე, შექმენით კლასის 
# მეთოდი car_info(), რომელიც დაბეჭდავს ატრიბუტების ინფორმაციას.
# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def car_info(self):
#         print(f"brand: {self.brand}")
#         print(f"model: {self.model}")
#         print(F"year: {self.year}")

# my_car = Car("Toyota", "Corolla", 2020)
# my_car.car_info()
# 2. Car კლასში დაამატეთ მეთოდი age_of_car, რომელიც დაითვლის მანქანის ასაკს. ავტომობილის ასაკი დაბეჭდეთ car_info() მეთოდიდან.
# from datetime import datetime

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year


#     def age_of_car(self):
#         current_year = datetime.now().year
#         return current_year - self.year
#     def car_info(self):
#         print(f"brand: {self.brand}")
#         print(f"model: {self.model}")
#         print(F"year: {self.year}")
#         print(F"car age: {self.age_of_car()} years")
# my_car = Car("Toyota", "Corolla", 2020)
# my_car.car_info()




# 3. შექმენით კლასი ElectricCar, რომელიც მემკვიდრეობით მიიღებს Car კლასს. დაამატეთ ახალი ატრიბუტი battery_life და მეთოდი battery_info(), 
# რომელიც დაბეჭდავს შემდეგ სტრიქონს "ამ მანქანის ბატარეის ხანგრძლივობა არის [battery_life] საათი".
# class ElectricCar(Car):
#     def __init__(self, brand, model, year, battery_life):
#         super().__init__(brand, model, year) 
#         self.battery_life = battery_life 
#     def battery_info(self):
#         print(f"ამ მანქანის ბატარეის ხანგრძლივობა არის {self.battery_life} საათი")

# my_electric_car = ElectricCar("Tesla", "Model 3", 2022, 12)
# my_electric_car.car_info()
# my_electric_car.battery_info()

# 4. დაამატეთ Car კლასს ატრიბუტი number_of_cars, რომელიც დაითვლის მანქანების სრულ რაოდენობას. გაზარდეთ ეს ცვლადი ყოველ ჯერზე, 
# მანქანის შექმნისას. 
# from datetime import datetime

# class car:
#     number_of_cars = 0
#     def __init__(self, brand, model, year):
#      self.brand = brand
#      self.model = model
#      self.year = year
#      car.number_of_cars += 1
#     def age_of_car(self):
#          current_year = datetime.now().year
#          return current_year - self.year
#     def car_info(self):
#          print(f"Brand: {self.brand}")
#          print(f"Model: {self.model}")
#          print(f"Year: {self.year}")
#          print(f"Car Age: {self.age_of_car()} years")
#          print(f"Total cars created: {car.number_of_cars}")

# car1 = car("Toyota", "Corolla", 2020)
# car2 = car("Honda", "Civic", 2019)
# car3 = car("Ford", "Focus", 2021)

# car1.car_info()
# car2.car_info()
# car3.car_info()



# 5. Car კლასს დაამატეთ მეთოდი total_cars(), რომელიც გამოიტანს მანქანების მთლიან რაოდენობას.

from datetime import datetime

class car:
    number_of_cars = 0

    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year

        car.number_of_cars += 1
    def age_of_car(self):
        current_year = datetime.now().year
        return current_year - self.year
    def car_info(self):
         print(f"Brand: {self.brand}")
         print(f"Model: {self.model}")
         print(f"Year: {self.year}")
         print(f"Car Age: {self.age_of_car()} years")
         print(f"Total cars created: {car.number_of_cars}")
    def total_cars(cls):
        print(f"total number of cars: {cls.number_of_cars}")
car1 = car("Toyota", "Corolla", 2020)
car2 = car("Honda", "Civic", 2019)
car3 = car("Ford", "Focus", 2021)

car1.car_info()
car2.car_info()
car3.car_info()

car.total_cars()
        