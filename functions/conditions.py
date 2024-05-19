#without condition
def print_numbers(n):
    numbers=range(n)
    for numbers in numbers:
        print(numbers)

#if statement
def print_even_numbers(n):
    number=range(n)
    for number in numbers:
        if number%2 ==0:
            print(number)

#ifelse statement
def odd_or_even(n):
    numbers=range(n)
    for number in numbers:
        if number %2==0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")

#elif ataement
def check_divisibilty(n):
    numbers=range(n) 
    for number in numbers:
        if number%3==0:
            print(f"{number} is divisble by 3")
        elif number%5==0:
            print(f"{number} is divisible by 5")
        elif number%7==0:
            print(f"{number} is divisible by 7")
        else:
            print(f"{number} is not divisble by 3,5,7")   

#while loop 
def count_down(n):
    x=0
    while n>x:
        print(n)
        n-=1  

#break statement
def count_down_five(n):
    x=0
    while n>x:
        print(n)
        if n==5:
            break
        n-=1    

#continue  statement
def divisible_by_seven(n):
    x=1
    while x<=n:
         x+=1 
         if x%7!=0:
            continue
         print(f"{x} divisible by 7")   

#1Using while statement write ,continue and if statement write function prints all odd numbers btn 0 and 100

#2create functionnamed fizzbuzz
#for numbers divisible by 3 print fizz
##for numbers divisible by 5 print buzz
#for all other numbers print fizzbuzz
#use elif,if else

#1
def odd_num(n):
    x=0
    while x<n:
        x+=1
        if x% 2==0:
            continue
        print(f"{x} is an odd number")

#2
def divisible_by_three_five(n):
    numbers=range(n)
    for number in numbers:
        if number%3==0:
            print(f"{number} fizz")
        elif number%5==0:
            print(f"{number} buzz")  
        else:
            print(f"{number} fizzbuzz")      














     
       
           








