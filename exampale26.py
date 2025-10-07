name=input("Enter your name:")
gender=input("Enter your gender:")
age=int(input("Enter your age:"))

product=input("Enter product:")
gram=int(input("Enter product gram:"))
print("=========================================================")

currentgram=5755
print("Current gold price(1gram):",currentgram)

TotalGold=gram*currentgram
print("TOTAL GOLD RATE:",TotalGold)
print("========================================================")

chargesgram=800
print("Making charges(1 gram):",chargesgram)

MakingCharge=chargesgram*gram
print("Total Making Charges:",MakingCharge)

TotalAmount=TotalGold+MakingCharge
print("Total Amount:",TotalAmount)
print("==================================================")

discount=0
if(gender == 'm' or gender == 'M')and age>65:
    if TotalAmount>=21000 and TotalAmount<31000:
        discount=(TotalAmount*20)/100
    elif TotalAmount>=31000 and TotalAmount<51000:
        discount=(TotalAmount*30)/100
    else:
        discount=(TotalAmount*35)/100
else:
     if TotalAmount>=21000 and TotalAmount<31000:
         discount=(TotalAmount*20)/100
     else:
         discount=(TotalAmount*25)/100

if(gender == 'f' or gender == 'F')and age>65:
    if TotalAmount>=21000 and TotalAmount<31000:
        discount=(TotalAmount*25)/100
    elif TotalAmount>=31000 and TotalAmount<51000:
        discount=(TotalAmount*35)/100
    else:
        discount=(TotalAmount*40)/100
else:
     if TotalAmount>=21000 and TotalAmount<31000:
         discount=(TotalAmount*15)/100
     elif TotalAmount>=31000 and TotalAmount<51000:
         discount=(TotalAmount*25)/100
     else:
         discount=(TotalAmount*30)/100


print("discount:",discount)
netamount=TotalAmount-discount
print("netamount:",netamount)

