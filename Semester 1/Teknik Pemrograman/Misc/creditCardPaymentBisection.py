def annualBalance(balance, annualInterestRate, monthlyPayment,month):
    monthlyInterestRate = annualInterestRate/12.0
    monthlyUnpaidBalance = balance - monthlyPayment
    updatedBalance = monthlyUnpaidBalance + monthlyInterestRate*monthlyUnpaidBalance

    if(month == 12):
        return updatedBalance
    
    return annualBalance(updatedBalance,annualInterestRate,monthlyPayment, month+1)

def minimumPayment(balance, annualInterestRate):
    monthlyInterestRate = annualInterestRate / 12.0
    lowerBound = balance / 12.0
    upperBound = (balance * (1+monthlyInterestRate)**12) / 12.0
    epsilon = 0.1
    while(True):
        middle = (lowerBound + upperBound) / 2
        afterBalance = annualBalance(balance, annualInterestRate,middle,1)

        if abs(afterBalance) <= epsilon:
            return middle
        elif afterBalance > epsilon:
            lowerBound = middle
        else:
            upperBound = middle
        steps += 1

print("Lowest Payment: ", round(minimumPayment(320000, 0.2),2))

