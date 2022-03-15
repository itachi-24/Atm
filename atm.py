import time

# insert card option when at welcome screen 
print("Please insert your Card")

# take 5 Sec to process card
time.sleep(5)

# enter password this comming from the bank database 
password = 1234
# ask user to enter pin 
pin = int(input("Enter Your Pin"))

# check users passbook balance This is comming from the bank database here 5000
balance = 5000

# check password 
if pin==password:
    while True:
        # if password is correct give option to the user 
        print("""
            1 = Balance Enquery
            2 = Cash withdrow
            3 = Deposite Balance
            4 = Exit"""
        )

        try:
            option = int(input("Please Enter Your Choise"))

        # if user doesnot enter valid option 
        except:
            print("Please Enter Valid Option")
            print("===================================================")

        # check user responce 
        if option ==1:
            # balance enquery
            print(f"Your Current Balance is {balance}")
            print("===================================================")

        if option ==2:
            # cash withdrow 
            withderow_amount = int(input("Please Enter Withdrow Amount"))
            balance=balance - withderow_amount

            # show balance to the user after withdrow 
            print(f"Your Current balance is {balance}")
            print("===================================================")

        if option==3:
            # cash deposite 
            deposit_amount = int(input("Please enter deposite amount"))
            balance = balance + deposit_amount

            # show balance to the user after deposite 
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
            print("===================================================")
        if option == 4:
            # exit user 
            break 
# if user enter wrong pin 
else:
    print("Wrong pin please try again")

