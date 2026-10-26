#ATM Flow Assignment

#Stored / Databse Values
'''liUserPass = 1234
liMenuChoice = 0
liUserBal = 50000

#UserInput Values
aiUserPass = 0
aiWithDrawAmt = 0
aiDepositAmt = 0

#Checkpoints
lbIsPassMatch = False
IsCardInserted = "N"

print("Welcome to Bank Of Maharashtra")

IsCardInserted = input("Please INsert the Card \n")

if(IsCardInserted == "Y"):
    
    aiUserPass = int(input("Please Insert PIN : "))

    if(liUserPass == aiUserPass):

        liMenuChoice = int(input("Please Select the Service :\n"
                                 "1. Check Balance\n"
                                 "2. Withdraw Cash\n"
                                 "3. Deposit Cash\n"
                                 "4. Exit"))

        if(liMenuChoice == 1):
            print("Balance : " , liUserBal)

        elif(liMenuChoice == 2):
            aiWithDrawAmt = int(input("Please Enter The Amount : "))

            if(aiWithDrawAmt <= liUserBal):
                liUserBal = liUserBal - aiWithDrawAmt

                print("Please Collect The Cash \nTransaction is Successful")
                print("Available Balance : ", liUserBal)
                
            else : 
                print("Insufficient Balance")

        elif(liMenuChoice == 3):
            aiDepositAmt = int(input("Please Enther The amount to Deposit : "))

            liUserBal = liUserBal + aiDepositAmt

            print("Transaction is Successful")
            print("Available Balance : ", liUserBal)
            
        elif(liMenuChoice == 4):
            print("Thank you for using the ATM. \nTransaction completed.")

        else :
            print("Invalid Choice")
    else :
        print("Incorrect PIN")

else :
    print("Please Insert Your Card")'''

    