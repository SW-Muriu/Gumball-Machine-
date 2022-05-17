# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# constructor for a gumball machine.

# Instance variables:
# capacity - type integer. tells how many gumballs the machine has
# money - type float.
# tells how much money the machine has. starts at 0.
# gumballs - type list[str]. randomizes several gumballs of
# different colors. the colors choices are: red, green, or blue. length depends on capacity fed by user.

# instance methods:
# report(): accepts no arguments. reports the current status of the machine
# e.g: if class is instantiated with capacity = 5, sample output is:
#    Gumball Machine Report:
#   * Gumballs in machine: 5
#  * Money in machine: $0.00

# dispense(coin_value): accepts an argument, a coin value. determines if the coin is a quarter, $0.25. then
# removes a random gumball and displays it to the user. increases money amount by coin value.  if coin is not a
# quarter, rejects transaction. if machine is empty, no gumball is dispensed and coin is rejected.
#  * count_gumballs_by_type(type): accepts a string, color of gumball and prints the number of gumballs of that
# type left in machine.

import random


class Gumball_Machine:
    def __init__(self, capacity):
        self.capacity = capacity  # user will input the capacity - first instance variable
        self.money = 0.00  # money starts at $0.00 - second instance variable
        types = ["red", "green", "blue"]  # gumball types for random sampling
        self.gumballs = []  # - third instance variable
        for i in range(capacity):  # for every gumball in the given capacity, add a random type
            self.gumballs.append(''.join(random.choice(types)))
        print(f"Gumball Machine created with {capacity} random gumballs")  # announce machine has been created

    def report(self):  # report
        print("Gumball Machine Report:")
        print(f"* Gumballs in machine: {self.capacity}")
        print(f"* Money in machine: ${'{:.2f}'.format(self.money)}")  # format money to 2 decimal places

    def dispense(self, coin_value):
        if coin_value != 0.25:  # if coin is not a quarter (invalid)
            print("Invalid coin, no gumball will be dispensed")
        else:  # if coin is a quarter (valid)
            random.shuffle(self.gumballs)  # shuffle the machine to randomize gumballs
            try:
                gumball_type = self.gumballs[-1]  # take the last gumball
                self.gumballs.pop()  # remove it from machine
                self.capacity = len(self.gumballs)  # reset capacity of machine to less one gumball
                self.money = self.money + coin_value  # increase money in machine by coin value
                print(f"Accepting {coin_value}; dispensing a {gumball_type} gumball")
            except IndexError:  # if coin is valid but machine is empty
                print("Machine is empty, no gumball will be dispensed")

    def count_gumballs_by_type(self, type):
        count = self.gumballs.count(type)  # returns the count of given gumball type
        print(f"There are {count} gumballs of type {type} in the machine")


# test code with only 5 balls
machine = Gumball_Machine(8)
machine.report()
print("")
machine.count_gumballs_by_type("red")
print("")
machine.count_gumballs_by_type("green")
print("")
machine.count_gumballs_by_type("blue")
print("")
