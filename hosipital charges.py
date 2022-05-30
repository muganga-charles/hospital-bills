def Total_in(days,daily_rate,Charges,medication_charged):#this is the sub program to capture the data from the user
    return days*daily_rate+Charges+medication_charged#this returns the total charges
def Total_out(Charges,medication_charged):#this is the sub program to capture the data from the user
    return Charges+medication_charged#this returns the total charges


take=int(input("where you addmited as an in patiet or an out patient.\nFor in-patient enter '1'\nfor an out-patient enter '2'"))#THIS IS THE MENU
while take<1 or take>2:#this is the loop to check if the user enters the correct input
    take=int(input("choose between 1 and 2"))
if take==1:#this is the if statement to check if the user chooses the in-patient
    print("---------------- in-patient-----------")
    days=int(input("enter the number of days spent in the hospital"))
    daily_rate=float(input("enter the daily rate"))
    Charges=int(input("Enter the charges for hospitala services"))
    medication_charged=int(input("Enter the Medication charges"))
    print("the Total charges for an in-patient are:",Total_in(days,daily_rate,Charges,medication_charged))#This prints the total charges
else:#this is the else statement to check if the user chooses the out-patient
    print("---------------- out-patient-----------")
    Charges=int(input("Enter the charges for hospitala services"))
    medication_charged=int(input("Enter the Medication charges"))
    print("the Total charges for an in-patient are:",Total_out(Charges,medication_charged))#this prints the total charges