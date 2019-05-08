import random
import string
import fileinput

# def randomstring(stringLenght=int(input('enter a length of the string: '))):
#     letters=string.ascii_letters
#     return ''.join(random.sample(letters,stringLenght))
# print("random String is",randomstring())
# result=randomstring()

# f= open('out.txt','a')
# f.writelines(result)
# f.write('\n')
# f.close()
# stringlength=int(input("Enter a value of string: "))

# # result=randomstring()
# n=int(input("Enter the range to Print: "))
# for i in range(n):
#     def randomstring():
#         letters=string.ascii_letters
#         return ''.join(random.sample(letters,stringlength))
#     print(randomstring())

stringlength=int(input("Enter string length: "))
n=int(input("Enter value for Iterations: "))
# for i in range(n):
#     letters=string.ascii_letters
#     # return ''.join(random.sample(letters,stringlength))
#     print(''.join(random.sample(letters,stringlength)))

def randomstring():
    for _ in range(n):
        letters=string.ascii_letters
        print(''.join(random.sample(letters,stringlength)))
randomstring()