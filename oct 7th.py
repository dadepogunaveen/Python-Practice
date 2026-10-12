# 1
# str="   jhonny is drinking   "
# str1=str.lstrip()
# str2=str.rstrip()
# str3=str.strip()
# print(str)
# print(str1)
# print(str2)
# print(str3)
#
# 2
# Removing spaces in the string
# str=input("enter a string")#" D I A"
# print(str)
# str1=""
# for i in str:
#     if i==" ":
#         pass
#     else:
#         str1=str1+i
# print(str1)
#
# 3
# str="Ramya"
# print(str)
# r1,r2,r3,r4,r5=str
# print(r1)
# print(r2)
# print(r3)
# print(r4)
# print(r5)
#
# 4
# alpha=input("enter an alphabet:")
# ascii=ord(alpha)
# print(ascii)
#
# ascii=int(input("enter a ascii value:"))
# alpha=chr(ascii)
# print(alpha)

#practise code

str=input("enter your name:")
print(str)
str1=str.upper()
print(str1)
str2=str.lower()
print(str2)
str3=str.swapcase()
print(str3)

str=" jgr gojr "
print(len(str))
str1=str.lstrip()
str2=str.rstrip()
str3=str.strip()
print(str1)
print(str2)
print(str3)

alpha=input("enter an alphabet")
ascii=ord(alpha)
print("your value of",alpha,"is",ascii)


ascii=int(input("enter an ascii values"))
alpha=chr(ascii)
print(alpha)
#
str=input("enter a name: ")
print(str)
str1=""
for i in str:
    if i==" ":
        pass
    else:
        str1=str1+i
print(str1)
