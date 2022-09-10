has_high_income = False
has_good_credit = False
has_criminal_record = False

if has_high_income and has_good_credit:
    print("eligible")
elif has_high_income or has_good_credit:
    print("so so")
elif  not has_criminal_record:
    print("Ok")
else:
    print("whats can i do sometimes")
