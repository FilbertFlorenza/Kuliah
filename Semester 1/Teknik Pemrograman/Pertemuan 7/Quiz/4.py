totalPurchasing = int(input("Input total purchasing: "))
paymentMethod = str(input("Input payment method: ")).lower()

if(totalPurchasing > 1000):
    index = "Bonus"
    if(paymentMethod == "credit card"):
        status = "Bonus Payung"
    else:
        status = "Bonus Gelas"
else:
    index = "Tidak ada Bonus"
    status = "Tidak ada Diskon"

print(f"Index= {index}\nBonus= {status}")