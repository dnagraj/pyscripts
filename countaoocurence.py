# n="Thsisisdndfhasdhhfghdfghhfghfghfg"

# conut=0
# for i in n:
#     if i=='g':
#         conut=conut+1
# print(str(conut))

def countoccurence(str,word):
    a=str.split(" ")
    conut=0
    for i in range(0,len(a)):
        if word==a[i]:
            conut=conut+1
    else:
        print("Please check again with another word: ")
    
    return conut
    
str=input("Enter a string : ")
word=input("eter a word for : ")
print(countoccurence(str,word))