pin=2580
amount=5000
pin_number=int(input("enter the pin_number:"))
if pin_number==pin:
    print("1.deposite\n2.with_drawal\n3.balance_Enquire")
    choice=int(input("Enter the your choice:"))
    if choice==1:
      deposite_amount=int(input("Enter the deposite amount:"))
      amount1=deposite_amount+amount
      print("your current balance amount is",amount1)
    elif choice==2:
        wth_drawal=int(input("Enter the wth_drawal_amount"))
        amount2=amount-wth_drawal
        print("you current balence is",amount2)
    elif choice==3:
         print("your current amount:",amount)
    else:
        print(" you are worng input Number given:")

else:
    print("user  Enter worng pin")



