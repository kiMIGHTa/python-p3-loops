#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i=10
    while i>0:
        print (i)
        i-=1
    print("Happy New Year!")    
        
    pass

def square_integers(int_list):
    # code goes here!
    int_list_squared= [int_item*int_item for int_item in int_list]
    print(int_list_squared)
    return int_list_squared
    

def fizzbuzz():
    # code goes here!
    i=1
    while i<=100:
        if i%3==0 and i%5==0:
            print("FizzBuzz")
        elif i%3==0:
            print("Fizz")    
        elif i%5==0:
            print("Buzz")  
        else:
            print(i)       
        i+=1    
    pass
