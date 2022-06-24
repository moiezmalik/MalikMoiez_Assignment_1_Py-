#ask user to enter account present value
present_value = float(input('Enter Current value of account : '))

#ask user to enter inerest rate
interest_rate = float(input('Enter Interest Rate : '))

#ask user to enter months that money will stay in account
months = int(input('Enter the Number of Months the money will stay in account : '))

#calculate the future value with arguments and return the FV
def futureValue(pv,i,m):
    future_value = pv*(1+i/100)**m
    return future_value

#Print FV
print("Your money will be $",int(futureValue(present_value,interest_rate,months)),"after",months,"months")

#Leave the program running until user enter
input('Press ENTER to exit')

