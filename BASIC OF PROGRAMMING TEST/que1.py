credit_score = int(input("credit_score="))
income = int(input("income="))
emi = int(input("emi="))
employment = input("Salaried/Self-Employed/Unemployed=")
status = ""
interest_rate = "N/A"
if credit_score < 600:
    status = "Rejected"
elif 600 <= credit_score < 750:
    status = "Review"
else:
   if income < 25000:
        status = "Rejected"
   elif emi > 0.5 * income:
        status = "Rejected"
   elif employment not in ["Salaried", "Self-Employed"]:
        status = "Rejected"
   else:
        status = "Approved"
        if credit_score >= 800:
            interest_rate = "7%"
        else:
            interest_rate = "8%"
print("Status:", status)
print("Interest Rate:", interest_rate)
