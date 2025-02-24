#!/usr/bin/env python3

def happy_new_year():
    for i in range(10, 0, -1):
        print(i)
        print("Happy New Year!")
    # code goes here!
   
def square_integers(int_list):
    return [i ** 2 for i in int_list]
    # code goes here!

def fizzbuzz():
    for i in range(1, 101):
      if i % 3 == 0 and i % 5 == 0:
          print("FizzBuzz")
      elif i % 3 == 0:
          print("Fizz")
      elif i % 5 == 0:
          print("Buzz") 
      else:
          print(i)    
    # code goes here!

