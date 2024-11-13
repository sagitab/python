#
#greeting="Hello, world!"
#print("length",len(greeting),greeting[0],greeting[-1])
"""first_name="sagi"
last_name="sensay"
fullName=first_name+" "+ last_name
print(f"{fullName}")
quote="To be or not to be, that is the question"
print(quote.upper())
print(quote.lower())
word = 'Python'
print("\n",word[0:3])
print("\n",word[-3:len(word)])
print(word[::-1])
sentence="yo yona"
print(sentence.replace("yona","sagi"))
text = 'The quick brown fox jumps over the lazy dog'
if "dog" in text:
    print("yes")
list=["banana","appel","fig"]
list.append("sagi")
list.pop(0)
print(list)   
animals = ['cat', 'dog', 'rabbit', 'hamster'] 
print(animals[0])
print(animals[-1])
print(len(animals))
nums=[5, 10, 15, 20, 25]
nums[1]=12
print(nums)
nums.pop()
print(nums)
first_ten_numbers = list(range(1, 11))
print(first_ten_numbers[0:5])
print(first_ten_numbers[-3:])
print(first_ten_numbers[::-1])
list=[]
for i in range(1,6):
    list.append(i**2)
print(list)  
fruits = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
item="apple"
counter=0
for i in fruits:
    if i==item:
        counter+=1
print(counter)         
colors = ['red', 'blue', 'green', 'yellow', 'blue']
color="blue"
for i in range(len(colors)):
    if colors[i]==color:
        print("the index-",i)
        exit(0)
list1=[1, 2, 3]
list2=[4, 5, 6]
list3=list1+list2
print(list3)
numbers = [1, 2, 2, 3, 4, 2]
def removeNum(num):
        
    i = 0
    while i < len(numbers):
        if numbers[i]==num:
                numbers.pop(i)
                if i>0:
                    i-=1
        i+=1
                    
removeNum(1)
print(numbers)            
numbers = [133, 22, 2, 33, 42, 21]
for i in range(len(numbers)-2):
    first=numbers[i]
    second=numbers[i+1]
    if first>second:""" 
def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
print(factorial(4))