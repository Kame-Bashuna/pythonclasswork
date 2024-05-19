def add(x,y):
    result=x+y
    return result

    add=1000+2000
    print(add)

def substract(x,y):
   result=x-y
   return result
   
   substract=1000-50
   print(substract)


def divide(x,y):
   result=x/y
   return result

   divide=200/10
   print(divide)  


def multiply(x,y):
   result=x*y
   return result

   multiply=10*2
   print(multiply) 

def remainder(x,y):
   result=x%y
   return result

   remainder=100%20
   print(remainder)

def powerOf(x,y):
   result=x**y
   return result

   powerOf=10**2
   print(powerOf)

def  sum(*numbers):
   total=0
   for number in numbers:
      total+=number
      return total 

def multiply(*numbers):
   total=0
   for number in numbers:
      total*=number
      return total 


#  def create_sentence(**words): 
#    sentence=" " 
#    for word in words.values():
#       sentence +=word
#       sentence +=" "
#    return sentence


 def sum_and_greet(*args,**kwargs):
    total=0
    for x in args:
        total+=x

    f=kwargs["first_name"]
    l=kwargs["last_name"]
    greeting=f"Hello {f} {l} the sum of your number is {total}"  
    return greeting
             



