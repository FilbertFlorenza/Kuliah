def annualBalance(balance, annualInterestRate, monthlyPayment,month):
    monthlyInterestRate = annualInterestRate/12.0
    monthlyUnpaidBalance = balance - monthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance

    if(month == 12):
        return updatedBalance
    
    return annualBalance(updatedBalance,annualInterestRate,monthlyPayment, month+1)

def minimumPayment(balance, annualInterestRate, monthlyPayment):
    if(annualBalance(balance, annualInterestRate,monthlyPayment,1) <= 0):
        return monthlyPayment
    return minimumPayment(balance,annualInterestRate,monthlyPayment+10)

print("Annual Balance: ", round(annualBalance(42, 0.2, 2, 1),2))
print("Lowest Payment: ", round(minimumPayment(320000, 0.2, 10),2))

