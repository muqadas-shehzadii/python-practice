# sample_string = input("Enter string")
# vowels = 'aeiouAEIOU'
# count = 0
# for char in sample_string:
#     if char in vowels:
#         count+=1
# print("check",count)        


# sample_string = input("Enter string: ")
# vowels = 'aeiouAEIOU'
# found_vowels = []
# for char in sample_string:
#     if char in vowels:
#         found_vowels.append(char)
# print("check", found_vowels)

# sample = input("ENter string")
# for char in sample:
#     print(char)        
# num = 1
# while num<=20:
#     if num%2 == 0:
#         print(num)
#     num+=1    
# count = 1
# total = 0
# while count<100:
#     total+=count
#     count+=1
# print(total)    
num = int(input("ENter number"))
if num > 2:
    is_prime = True
    i = 2
    while i < num:
        if num % i ==0:
            is_prime = False
        break
    i+=1
    if is_prime:
        print(num,'is prime')
    else:
        print(num,'not a prime')
else:
    print('not a prime number')                