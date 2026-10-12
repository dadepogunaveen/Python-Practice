a=("Welcome to Pentagon ATM")
print(a)
b=input("Please insert your card:")
print(b)
if b:=1:
    print("your card is inserted")
else:
    print("please insert your card corretly")
c=input("Select your language\nEnglish:\nkannada:\ntelugu:\n:")
print(c)
if c:="english":
    print("your language english is selected")
elif c:="kannada":
    print("your language kannada is selected")
elif c:="telugu":
    print("your language telugu is selected")
d=input("enter your pin:")
if d:=1234:
    print("your pin is valid")
else:
    print("your pin is not valid")
e=input("select the option:\nbalance enquiry\nwithdraw your amount\n:")
print(e)
if e:="balance enquiry":
    print("your balance is 3,000")
else:
    print("okay")
f=int(input("enter the amount you want to withdraw:"))
if f<=3000:
    print("your amount has be debited\nplease take your card and take your amount")
else:
    print("insufficient fund")
g=("visit again ,thank you")
print(g)