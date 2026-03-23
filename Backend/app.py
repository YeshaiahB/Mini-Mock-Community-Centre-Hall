StandardPriceRate = 10
MemberPriceRate = 7

from datetime import datetime

def ProduceReciept(Price, Name, Age, Date, RequestedDate):
    print(f'Here is your reciept: \n Total Price: £{Price}, \n Name: {Name}, \n Age: {Age}, \n Your appointment is on: {RequestedDate}, \n Purchase Date: {Date}')

def AskIfMember():
    IsMember = str(input("Are you a member? (Yes / No) "))
    return IsMember

def ValidateIfMember():
    IsMember = AskIfMember()
    IsMember = str.strip(str.lower(IsMember))

    if (IsMember == "yes"):
        return True, IsMember
    else:
        return False, IsMember

def GetHoursBooked():
    Hours = str.strip(input("How many hours do you want to book?"))
    return Hours

def ValidateHoursBooked(): 
    RequestedHours = GetHoursBooked()
    
    if RequestedHours.isnumeric() == True:
        return True, int(RequestedHours)
    else:
        return False, RequestedHours
    
def AskTypeOfMember():
    MemberType = str(input("What type of member are you? (Standard / Verified) "))
    return MemberType

def ValidateTypeOfMember():
    MemberType = AskTypeOfMember()
    MemberType = str.strip(str.lower(MemberType))

    if MemberType == "standard" or MemberType == "verified":
        return True, MemberType
    else:
        return False, MemberType
    

def ErrorHandler():
    print("Some of your inputs arent valid! Please try again.")
    return CalculatePrice()

def PromptMemberShipPurchase():
    print("Please head to our website to buy a membership! If you can't find it that's too bad cause it dosent exist :) ")

def CalculatePrice():
    MemberValid, IsMember = ValidateIfMember()
    HoursValid, RequestedHours = ValidateHoursBooked()

    if MemberValid == True and HoursValid == True:
        if IsMember == "yes": 
            MemberTypeValid, MemberType = ValidateTypeOfMember()

            if not MemberTypeValid:
                return ErrorHandler()

            UserName = str.strip(str(input("What is your name?")))
            Age = int(str.strip(input("How old are you?")))
            Date = datetime.now()

            print("Please fill in the day you would like to book.")
            TargetDate = datetime(FormatDateIndex(input("Year: ")), FormatDateIndex(input("Month: ")), FormatDateIndex(input("Day: ")))

            if MemberType == "standard":
                ProduceReciept(RequestedHours * StandardPriceRate, UserName, Age, Date, TargetDate.strftime("%x"))
            elif MemberType == "verified":
                ProduceReciept(RequestedHours * MemberPriceRate, UserName, Age, Date, TargetDate.strftime("%x"))
        elif IsMember == "no":
            PromptMemberShipPurchase()
    else:
        return ErrorHandler()
    
def FormatDateIndex(Number):
    return int(str.strip(Number))

CalculatePrice()