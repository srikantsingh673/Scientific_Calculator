''' Scientific Calculator by Rishu '''

import math
import statistics
from itertools import permutations
from itertools import combinations
import numpy as np
from scipy import stats
def get():
    fn = int(input("Enter the First Number : "))
    sn = int(input("Enter the Second Number : "))
    return (fn, sn)

#functions part

def add():
    x, y = get()
    return (x+y)

def sub():
    x, y = get()
    return (x-y)

def multi():
    x, y = get()
    return (x*y)
    
def div():
    x, y = get()
    return (x/y)

def ando():
    x, y = get()
    return (x and y)

def oro():
    x, y = get()
    return (x or y)

def noro():
    x, y = get()
    return (not y)
def fact():
    x = int(input("Input a Number you want to find factorial : "))
    return (math.factorial(x))

def fibo(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else: 
		return fibo(n-1) + fibo(n-2)

def fibon():
    x = int(input("Enter a Number you want to find Fibonacci series : "))
    print(fibo(x))

 
def permu():
    lst = []
    n = int(input("Enter the Number of Elements you want to take input for Permutation : "))
    print("\n Enter Element and then Press Enter > ")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    a=permutations(lst) 
    for i in a: 
       print(i)
    return i

def reve():
    n = int(input("Input a Number you want to Reverse : "))
    revs = 0

    while(n > 0):
	    a = n % 10
	    revs = revs * 10 + a
	    n = n // 10
    print(revs)

def combi():
    lst = []
    n = int(input("Enter the Number of Elements you want to take input for Combinations : "))
    print("\n Enter Element and then Press Enter > ")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    m = int(input("\n Enter the Length you want for COmbination > "))
    a=combinations(lst,m) 
    for i in a: 
       print(i)
    return i

def mmm():
    lst = []
    n = int(input("Enter the Number of Elements you want to take input to find Mean Median and Mode  : "))
    print("\n Enter Element and then Press Enter > ")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    a=np.mean(lst)
    b=np.median(lst)
    c=stats.mode(lst)
    print("Mean : ",a)
    print("Median : ",b)
    print("Mode : ",c)

def dvsd():
    lst =[]
    n = int(input("Enter the Number of Elements you want to find Variance an Standard deviation : "))
    print("\n Enter Element and then Press Enter > ")
    for i in range(0, n):
        ele = int(input())
        lst.append(ele)
    print("Variance : % s"
      %(statistics.variance(lst)))
    std = np.std(lst)
    print("Standard deviation : ",std)

#main

print('''
    1. Addition 
    2. Substraction
    3. Multiplication
    4. Division
    5. AND Operation2q
    6. OR Operation
    7. NOR Operation 
    8. Factorial 
    9. Fibonacci 
    10. Permutation 
    11. Integer reverse
    12. Combination
    13. Mean, median and mode
    14. Dictionary, variance and standard deviation

''')

#Conditions and function calling part

choice = int(input("Enter Your Choice : "))
if choice==1:
    result=add()
    print(result)
elif choice==2:
    result=sub()
    print(result)
elif choice==3:
    result=multi()
    print(result)
elif choice==4:
    result=div()
    print(result)
elif choice==5:
    result=ando()
    print(result)
elif choice==6:
    result=oro()
    print(result)
elif choice==7:
    result=noro()
    print(result)
elif choice==8:
    result=fact()
    print(result)
elif choice==9:
    result=fibon()
    print(result)
elif choice==10:
    result=permu()
    print(result)
elif choice==11:
    result=reve()
    print(result)
elif choice==12:
    result=combi()
    print(result)
elif choice==13:
    result=mmm()
    print(result)
elif choice==14:
    result=dvsd()
    print(result)

else:
    print("Invalid Choice")
print("\n")
