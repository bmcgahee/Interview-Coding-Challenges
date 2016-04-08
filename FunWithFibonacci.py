#Name: Ben McGahee
#Title: Fun With Fibonacci
#Date: 4/6/2016

import csv

def getNumbers(fileName): 
    try:
        openFile = open(fileName)                      #Try to open the csv and return the list of numbers
        readFile = csv.reader(openFile)
        numbers = list(readFile)
        return numbers
    except:                                            #If the file cannot be file, throw file not found exception.
        print "Cannot find the file: " + fileName

def numbersIntoList(numberBlock):
    values = []
    size = 6
    for j in range(0, size):
        number = int(numberBlock[0][j])
        values.append(number)                          #Create a regular list of numbers that are individual elements.
    return values

def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)     #Use recrusive function to add the previous two Fibonacci numbers to get the next Fibonacci number.

def getFibNumber(numberList):
    size = len(numberList)
    for i in range(0, size):
        number = numberList[i]                         #Iterate through all the numbers in the list and find the nth Fibonacci number using the fibonacci() function.
        fibNumber = fibonacci(number)
        print "Fib(" + str(number) + ")" + " = " + str(fibNumber)

def runFibonacci():
    fileName = "codingtest.csv"                        #File name is located inside the C:\Python27 folder on my laptop.
    numbers = getNumbers(fileName)                     #Open the csv file and get the block list of numbers.
    numberList = numbersIntoList(numbers)              #Convert the block list into a list of individual numbers.

    print "Here are the following Fibonacci values:"
    getFibNumber(numberList)                           #Find and print the nth Fibonacci number for all values of n inside the list.

runFibonacci()

