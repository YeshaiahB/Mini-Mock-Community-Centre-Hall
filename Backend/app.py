StandardPriceRate = 10
MemberPriceRate = 7

def AskIfMember():
    IsMember = str(input("Are you a member?"))
    return IsMember

def ValidateIfMember():
    IsMember = AskIfMember()
    IsMember = str.strip(str.lower(IsMember))

    if (IsMember == "yes"):
        return True, IsMember
    else:
        return False, IsMember

def GetHoursBooked():
    Hours = int(str.strip(input("How many hours do you want to book?")))
    return Hours

def ValidateHoursBooked(): 
    RequestedHours = GetHoursBooked()
    
    return True, RequestedHours
    
def AskTypeOfMember():
    MemberType = str(input("What type of member are you? Standard or Verified "))
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

            if MemberType == "standard":
                print(f'Your total price is: {RequestedHours * StandardPriceRate}')
            elif MemberType == "verified":
                print(f'Your total price is: {RequestedHours * MemberPriceRate}')
        elif IsMember == "no":
            PromptMemberShipPurchase()
    else:
        return ErrorHandler()
    
CalculatePrice()