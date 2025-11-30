#Extraction of Digits Using Loops
n=5783
num=n
while num>0:
    digit= num % 10
    print(digit)
    num=num//10 

#count the no. of digits in integer
n=5873
num=n
count=0
while num>0:
    count+=1
    num=num//10
print(count)

#check number is pallindrome 
n=5873
num=n
result=0
while num>0:
    digit=num%10
    result=(result*10)+digit
    num=num//10
print(n==result)

#Armstrong Number
n=1634
num=n
result=0
node=len(str(num))
while num>0:
    digit=num%10
    power=digit**node
    result=result+power
    num=num//10
print(result==n) 

#print all factors of given no.
from math import sqrt
n=15
num=n
result=[]
for i in range(1,int(sqrt(num)+1)):
    if num % i==0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
print(sorted(result)) 

#store freq in dict
#method 1
nums=[1,2,5,4,4,5,5,7]
freq={}
for i in range(1,len(nums)):
    if nums[i] in freq:
        freq[nums[i]]+=1
    else:
        freq[nums[i]]=1
print(freq)

#method 2
nums=[1,2,5,4,4,5,5,7]
hash_map={}
n=len(nums)
for i in range(1,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map) 