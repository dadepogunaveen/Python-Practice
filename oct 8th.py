str=input("enter a string")
print(str)
if str.isalpha():
    print("contains only alphabets")
elif str.isdigit():
    print("contains only digits")
elif str.isalnum():
    print("contains both")
else:
    print("other character")

str=("if you think you can or you can't, you are right")
print(str)
str1=("you")
print(str.count("you"))
print(str.index("you"))
print(str1 in str)
print(str.find("you"))
print(str.rindex("you"))
print(str.rfind("you"))
print(str.find("python"))
print(str.index("python"))

str=("rohan is a good boy")
print(str)
str1=str.replace("good","bad")
print(str1)
print(str.startswith("rohan"))
print(str.startswith("rohit"))
print(str.endswith("boy"))
print(str.endswith("girl"))