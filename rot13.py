import codecs

phrase=input("Enter a phrase: ")
if phrase!='':
    print(codecs.encode(codecs.encode(phrase,'rot_13'),'rot_13'))
    print(codecs.encode('hello','rot_13'))
else:
    print("try again")
    
