# #slicing
#
# str="RajaRamMohanRoy"
# print(str)
# print(len(str))
# print(str[7])
# print(str[2:8])
# print(str[3:11:2])
# print(str[-2:-8])
# print(str[-3:13])
# print(str[::])
# print(str[::3])
# print(str[13:-11:-1])
# print(str[-12:-2])
# print(str[::-1])
# print(str[::-4])
# #print(str[2:8:0])

str=input("enter a name")
print(str)
str1=""
for i in str:
    if i==" ":
        pass
    else:
        str1=str1+i
print(str1)