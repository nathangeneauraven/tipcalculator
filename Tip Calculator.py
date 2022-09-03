print("Welcome to the tip calculator.")
bill_total = input("What was the total bill?\n $")
tip = input("What percentage tip would you like to give? 10%, 12%, or 15%\n")
tip_rate_calc = int(tip) / 100
tip_total_calc = float(bill_total) * float(tip_rate_calc)

bill_and_tip_amount = float(bill_total) + float(tip_total_calc)
total_people = input("How many people will be splitting the bill?\n")

split_bill = float(bill_and_tip_amount) / int(total_people)
rounded_bill = round(split_bill, 2)
print(f"Each person should pay: ${rounded_bill}")
