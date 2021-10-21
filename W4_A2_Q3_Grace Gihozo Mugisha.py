# a program  for mr Omondi's car inventory management
#program implement list of list and classes to success

import sys

class carRent:
    def __init__(self):
        # self.model = model
        # self.year_released = year_released
        # self.year_acquired = year_acquired
        # self. money_made = money_made
        # self.num_of_rent = num_of_rent
        # self.plate_num = plate_num
        self.car_available = [["sedan", "2014", "2018", "100000", "RAF102", "20"],
                              ["Volkswagen Golf GTI.", "2013", "2019", "120000", "RAE102", "25"],
                              ["Lexus ES 300h", "2015", "2012", "10000", "RAD102", "5"],
                              ["Hyundai i20", "2016", "2020", "15000", "RAC102", "10"],
                              ["Mazda MX-5", "2017", "2017", "140000", "RAE102", "30"]] # list of car_available

    def display_available_cars(self):
        print(self.car_available)
        print(30 * "=")
        print()
#sedan= ["Honda City", "2014", "2018", "100000", "RAF102", "20"]
# sports_car = ["Volkswagen Golf GTI.", "2013", "2019", "120000", "RAE102", "25"]
#hybrid_car = ["Lexus ES 300h", "2015", "2012", "10000", "RAD102", "5"]
#hachback_car = ["Hyundai i20", "2016", "2020", "15000", "RAC102", "10"]
#convertible_car = ["Mazda MX-5", "2017", "2017", "140000", "RAE102",  "30"]
# #print(sedan, sports_car, hybrid_car, hachback_car,convertible_car)

    def rent_car(self, requested_car):
        if requested_car in self.car_available:   # When there is demand of car rent on car_available list
            print()
            print("car is rented")
            print()
            self.car_available.remove(requested_car)  # to remove car from the list which are selected

        else:
            print("sorry, the car was already kept")

    def add_car(self, returned_car):
        self.car_available.append(returned_car)  # the car that are recturned are in car_available list
        print("thank you for returning car. go in peace and looking forward to see you again")

#This is payment program

print("each car  rent at $30 per day, the total price will be counted with discount")
name = input(" name of client: ")


def car_cost(days_):
    if days_ <= 3:
        return days_ * 30  # $30*1 or 2 days
    elif days_ <= 7:
        return (days_ * 30) - 15  # for more than 2 days but less than 1 week discount of $ 15
    else:
        return (days_ * 30) - 40  # more than 1 week the discount of 40
        print("total amount :$", (car_cost(days)))  # total amount will calculate in respect to number of days the user inserted
        print("deposit should be : $", int(car_cost(days) / 3), "or more")   # int will cancel all the decimal #calculation of minimum deposit to be made
        cash = int(input("confirm amount of cash provoided to deposit: $"))
    if cash < (car_cost(days / 3)):  # there the program confirms the amount given respect the minimum deposit
        print("insufficient amount , insert amount required") # if the amount is less than te minimum deposit

    else:
        print("amount due: $", (car_cost(days) - cash))


def print_required():
        pass


class car_driver:
    def request_car(self):
            self.car = input("the name of the car you want: ") # For writing name of car
            print(self.car)

    def return_car(self):
        car_return = input("the the name of car returned: ")
        print(car_return)


car = carRent()
person = car_driver()  # imply that car_driver is related to person
while True:  # to make the while loop continue after selected any selected choices
  print("____________________")
  print("1.display all car variable")
  print("2. rent car")
  print("3. return back car")
  print("4. exit")
  choice = int(input("choose option you want: "))
  if choice == 1:
      car.display_available_cars()

  elif choice == 2:
       car.rent_car(person.request_car())  # object car in the list calling the function rent _car with the argument person calling
       print("total amount :$", (car_cost(days_=int(input("Enter number of days you need car for rent:")))))

  elif choice == 3:
       car.add_car(person.return_car())
  elif choice == 4:
        sys.exit()















