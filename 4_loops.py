# printing the letters of banana
for i in('banana'):
    print(i)

#printing numbers till 3 using while loop
i=1
while i<=3:
    print(i)
    i+=1

#making infinite loop using while    
i=1
while i<=5:
    print(i)

#use of break statement in loops
i=1    
while i<=5:
    print(i)
    break

#printing numbers till 4 using for loops
for i in range(1,5):#5 is written as it exclude from range
    print(i)
    
#printing all even number till 10       
for i in range(1,11):
    if i%2==0:
        print(i)

#efficient way of finding even numbers
for i in range(2,11,2):
    
    print(i)


# program of for loop of fabonacci series
# Fibonacci series using for loop

n = int(input("Enter the number of terms: "))
a = 0
b = 1
print("Fibonacci Series:")
for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
# write a program for star pattern 

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    
