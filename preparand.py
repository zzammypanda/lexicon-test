#! /usr/bin/python3
# This program uses the non-core package colorama to recolor the terminal (menu option 3)
# To install package type 'pip install colorama'

import sys
import math
import random
import datetime
from colorama import init, Fore, Style

class Character:
    name = "";
    health = 0;
    strength = 0;
    luck = 0;
        
    def __init__(self,name):
        self.name = name;
        self.health = random.randint(0,100)
        self.strength = random.randint(1,10)
        self.luck = random.randint(1,5)
            
    def __str__(self):
        return f'Name: {self.name}, Health: {self.health}, Strength: {self.strength}, Luck: {self.luck}'
    

# Print menu options
def print_menu():
    print("")
    print("0. Exit program")
    print("1. Print HelloWorld in console")
    print("2. Get user input and return user data")
    print("3. Change color of terminal (not implemented yet)")
    print("4. Print today's date")
    print("5. Print biggest value")
    print("6. Bigger or smaller than guessed")
    print("7. Write a file to disk")
    print("8. Read a file from disk")
    print("9. Let's do some math")
    print("10. Print multiplication table")
    print("11. Let's fill some arrays")
    print("12. Check if palindrome")
    print("13. Get user-defined segment")
    print("14. Sorting user values")
    print("15. Print sum of numbers")
    print("16. Create character and opponent")

# "2. Get user input and return user data"
def get_user_datas():
    first_name = input("Please submit your first name: ")
    surname = input("Please submit your surname: ")
    age = input("Please submit your age: ")
    print(f'User is {first_name} {surname}, {age}')

# "3. Change color of terminal"
def recolor_terminal(red):
    if red:
        print(Fore.RED)
    else:
        print(Style.RESET_ALL)


# "5. Print biggest value"
def print_max_data():
    n1 = input("Please submit your first number: ")
    n2 = input("Please submit your second number: ")
    print("The biggest number is: ", max(n1, n2))

# "6. Bigger or smaller than guessed"
def bigger_or_smaller():
    tries = 1
    goal = random.randint(0,100)
    number = int(input("Please guess a number between 0 and 100 (101 to quit): "))

    while number != goal and number != 101:
        if (number<goal):
            number = int(input("You guess too low, guess again (101 to quit): "))
            tries += 1
        else:
            number = int(input("You guess too high, guess again (101 to quit): "))
            tries += 1

    if (number == goal):
        print("You guessed the correct number. It took ", tries, " tries.")

# "7. Write a file to disc"
def write_file():
    content = input("Please enter file content: ")
    f = open("demofile.txt", "w")
    f.write(content)
    f.close()

# "8. Read a file from disc"
def read_file():
    f = open("demofile.txt", "rt")
    print(f.read())
    f.close()

# "9. Let's do some math functions"
def math_functions():
    number = float(input("Please input a [decimal] number: "))
    print("Square root ", math.sqrt(number))
    print("Power of two ", number ** 2)
    print("Power of ten", math.pow(number, 10))

# "10. Print multiplication table
def multiplication_table():
    print("\nb= \t" , end = '')
    for b in range (0, 11):
        print(b, "\t", end = '')
    for m in range (0, 11):
        print("\na=",m,"\t" , end = '')
        for n in range(0,11):
            print(n * m, "\t", end = '')
    print("\n")

# "11. Let's fill some arrays"
def fill_array():
    number = int(input("Please input array length: "))
    original = list()
    for i in range(number):
        original.append(random.randint(0,100))
    new = sorted(original)
    print(original)
    print(new)

#"12. Check if palindrome"
def check_palindrome():
    text = input("Please submit your text: ")
    if text == text[::-1]:
        print("This is a true palindrome.")
    else:
        print ("This is not a true palindrome.")

# "13. Get user-defined segment"
def user_segment():
    n1 = int(input("Please submit your first limit: "))
    n2 = int(input("Please submit your second limit: "))
    sequence = list(range(n1+1, n2, 1))
    print("The numbers in between are: ", sequence)

# "14. Sorting user values"
def sort_user_values():
    numbers = input("Please submit your numbers separated by ',': ").split(',')
    even = list()
    odd = list()
    for n in numbers:
        if int(n) % 2 == 0:
            even.append(int(n))
        else:
            odd.append(int(n))
    print(even)
    print(odd)

# "15. Print sum of numbers"
def add_user_data():
    numbers = input("Please submit your numbers separated by ',': ").split(',')
    sum = 0
    for i in numbers:
        sum += int(i)
    print("The sum of the numbers is ", sum)

# "16. Create character and opponent"
def create_players():
    player_name = input("Please submit name of your player: ")
    opponent_name = input("Please submit name of your opponent: ")
    player = Character(player_name)
    opponent = Character(opponent_name)
    print("Player: \t" , player)
    print("Opponent: \t", opponent)

init() # from colorama, for terminal coloring
red = True # for terminal coloring

while (True):
    try:
        print_menu()
        choice = int(input("Please submit choice: "))
        if choice == 0:
            break
        elif choice == 1:
            print("Hello World!")
        elif choice == 2: # "2. Get user input and return user data"
            get_user_datas()
        elif choice == 3: # "3. Change color of terminal between red & black"
            recolor_terminal(red)
            red = not red
        elif choice == 4:
            print("Dagens datum är: ", datetime.datetime.now().date())
        elif choice == 5: # "5. Print biggest value"
            print_max_data()
        elif choice == 6: # "6. Bigger or smaller than guessed"
            bigger_or_smaller()
        elif choice == 7: # "7. Write a file to disc"
            write_file()
        elif choice == 8: # "8. Read a file from disc"
            read_file()
        elif choice == 9: # "9. Let's do some math functions"
            math_functions()
        elif choice == 10: # "10. Print multiplication table
            multiplication_table()
        elif choice == 11: # "11. Let's fill some arrays
            fill_array()
        elif choice == 12: # "12. Check if palindrome"
            check_palindrome()
        elif choice == 13: # "13. Get user-defined segment"
            user_segment()
        elif choice == 14: # "14. Sorting user values"
            sort_user_values()            
        elif choice == 15: # "15. Print sum of numbers"
            add_user_data()
        elif choice == 16: # "16. Create character and opponent"
            create_players()
        else:
            print("Sorry, does not compute. Please try again.")

    except ValueError:
        print("Sorry, input must be numeric!")

print("Bye, bye!")
