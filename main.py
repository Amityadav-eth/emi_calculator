def calculate_emi(principal, interest_rate, tenure):
    monthly_interest_rate = interest_rate / 12 / 100
    emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** tenure / ((1 + monthly_interest_rate) ** tenure - 1)
    return emi

def calculate_monthly_components(principal, interest_rate, tenure):
    emi = calculate_emi(principal, interest_rate, tenure)
    monthwise_components = []
    remaining_balance = principal
    
    for month in range(1, tenure + 1):
        interest = remaining_balance * interest_rate / 12 / 100
        principal_paid = emi - interest
        remaining_balance -= principal_paid
        monthwise_components.append((month, emi, principal_paid, interest, remaining_balance))
    
    return monthwise_components
principal = float(input("enter your principal amount:"))
interest =float(input("enter your interest rate:"))
tenure=int(input("enter your tenure period in months:"))

emi_components = calculate_monthly_components(principal, interest,tenure)
print("Month | EMI     | Principal   | Interest   | Remaining Balance")
print("--------------------------------------------------------------")
for month, emi, principal, interest, balance in emi_components:
    print(f"{month:5d} | {emi:.2f} | {principal:.2f} | {interest:.2f} | {balance:.2f}")
