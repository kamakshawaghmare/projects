Balance="25000"
print("Balance")
print("welcome")
step=input("enter the step:")
if step=="please enter your ATM card":
    print("correct")
    language=input("enter the language:")
    if language=="Hindi" or language=="English":
        print("right")
        number=int(input("enter the number:"))
        if number >10 and number<99:
            print("yes")
            pin=int(input("enter your 4 digits pin:"))
            if pin>0:
                print("correct pin")
                Account=input("please enter your account type:")
                if Account=="saving" :
                    print(Account)
                    Transaction=input("please select Transaction:")
                    if Transaction=="withdrawal":
                        print("withdrawal")
                        Amount=int(input(" please enter your amount:"))
                        if Amount>100 or Amount<25000:
                            print("yes")
                            print("take your amount")
                        else:
                            print("Amount is not correct")
                    else:
                        print("No withdrawal")
                else:
                    print("No saving account")
            else:
                print("incorrect pin")
        else:
            print("incorrect number")
    else:
        print("incorrect language")
else:
    print("incorrect step")