amount=10000
print("welcome to pentagon atm")
print("insert your card")
print("1.yes 2.no")
card=int(input())
if card==1:
    print("your card is valid")
    print("select your language")
    print("1.english 2.kannada 3.telugu")
    lang=int(input())
    if lang==1:
        print("your language is english")
        print("please type your password")
        pin=int(input())
        if pin==1234:
            print("your password is valid")
            print("1.balance enquiry 2.withdraw amount")
            amt=int(input())
            if amt==1:
                print("your balance is",amount)
            elif amt==2:
                print("enter the amount you want to withdraw")
                z=int(input())
                print("your amount has been debited\nthe remaining amount is",z-amount)
        else:
            print("your password is not valid")
    else:
        print("your language is telugu ")
else:
    ("insert your card properly")