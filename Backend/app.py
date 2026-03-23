StandardPriceRate = 10
MemberPriceRate = 7

def AskIfMember():
    IsMember = str(input("Are you a member?"))
    return IsMember

def ValidateIfMember():
    IsMember = AskIfMember()
    IsMember = str.strip(str.lower(IsMember))

    if (IsMember == "yes" or IsMember == "no"):
        return True, IsMember
    else:
        return False, IsMember

def GetHoursBooked():
    Hours = int(str.strip(input("How many hours do you want to book?")))
    return Hours

def ValidateHoursBooked(): 
    RequestedHours = GetHoursBooked()
    
    return True, RequestedHours
    

def CalculatePrice():
    MemberValid, IsMember = ValidateIfMember()
    HoursValid, RequestedHours = ValidateHoursBooked()

    print(MemberValid, HoursValid)

    if MemberValid == True and HoursValid == True:
        if IsMember == "yes": 
            print(f'Your total price is: {RequestedHours * MemberPriceRate}')
        elif IsMember == "no":
            print(f'Your total price is: {RequestedHours * StandardPriceRate}')
    else:
        print("Some of your inputs arent valid! Please try again.")
        return CalculatePrice()
    
CalculatePrice()