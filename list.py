#prints the values of lists
nums= [5,10,15]
for i in nums:
    print(i)

#adding the '4' element at the last of the list using append
nums=[1,2,3]
x=nums.append(4)
print(x)
print(nums)

#printing all the number greater than 3
nums=[1,2,3,4,5]
for n in nums:
    if n>3:
        print(n)

        

#counting all the marking which are greater than or equal to 60
marks=[80,45,90,60,30]

count=0
for m in marks:
    if m>=60:
        count+=1

print(count)