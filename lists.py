# A python function that takes an argument as a list, list a=[2,4,6,8] and remove the second last item
# from the list and returns the whole list without the removed item

a=[2,4,6,8]
def numbers(a):
   y= a.pop(2)
   print (y)

numbers([2,4,6,8])


# A python program that has a list days=["Monday","Tuesday","Friday","Monday"] and counts number occurences of  Monday

days=["Monday","Tuesday","Friday","Monday"]
x=days.count("Monday")
print(x)

# A function called smallest that accepts a list of unsorted integers and returns the smallest number in the list e.g smallest[3,6,8,2,4,1,5,7]

small=([3,6,8,2,4,1,5,7])
def smallest():
    a.sort()
    print(a[0])
    return min(a)
smallest()

# function that using range function returns a list containing all the numbers between 100 and 200 that are divisible by 7

def divisible_by_seven():
    x=[]
    for y in range(100,200):
        if y%7==0:
         x.append(y)
         print(x)
divisible_by_seven()

    # write a python program that takes in two inputs (as integers) from a user and adds them.checks if sum is greater than 10,less than 10 or equal to 10 and prints a statement after each check

def sum():
       num1= int(input("Enter number1:"))
       num2= int(input("Enter number2:"))
       sum=num1+num2
       if sum>10:
        print("sum is greater than 10")
       
       elif sum<10:
        print("sum is less than 10")
                                            
       elif sum==10:
          print("equal to 10")
sum()
        



# Function that takes in one argument which is a list,a=[1,2,3,4,5] and returns True if 4 is present in the list and False if not present in the list

a=[1,2,3,4,5]    
def nums(a):
 if 4 in a:
      print(True) 
 else:
       False
nums(a)
        
        
        # A function that takes in an argument which is a list fruits=["apples","grapes","pineapple"] and removes the last fruit from the list then returns the list without the removed fruit

fruits=["Apples","grapes","Pinneaple"]
def  greens(fruits):
  fruits.pop()
  print(fruits)
greens(["Apples","grapes","pinnaples"])

#  A python program that takes in a list of cars car=['Ford','BMW','Volvo'] and returns a sorted list
def car():
    cars=["Ford","BMW","Volvo"]
    cars.sort()
    print(cars)
car()
    
          
            





    