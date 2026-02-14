while True:
    income = input("Enter your income(yes/no): ").strip().lower()
    if income not in ["yes", "no"]:
        print("Please enter yes or no only.")
        continue
    break

while True:
    credit_score = input("Enter your credit score(yes/no): ").strip().lower()
    if credit_score not in ["yes", "no"]:
        print("Please enter yes or no only.")
        continue
    break

while True:
    student = input("Are you a student?(yes/no): ").strip().lower()
    if student not in ["yes", "no"]:
        print("Please enter yes or no only.")
        continue
    break

while True:
    criminal_record = input("Do you have a criminal record?(yes/no): ").strip().lower()
    if criminal_record not in ["yes", "no"]:
        print("Please enter yes or no only.")
        continue
    break
if (income == "yes" and credit_score == "yes" or student == "yes" and not criminal_record == "yes"):
    print("You are eligible for the loan.")
elif income == "no" and credit_score == 'yes' or student == "no" and not criminal_record == "no":
    print("you are not eligible for the loan cuz of insufficient income.")
elif income == "yes" and credit_score == "no":
    print("you are not eligible for the loan cuz of low credit score.")
elif income == "yes" and credit_score == "yes" and student == "no" and criminal_record == "yes":
    print("you are not eligible for the loan cuz of criminal record.")
elif income == 'yes' and credit_score == 'yes' and student == 'yes' and not criminal_record == 'yes':
    print("You are eligible for the loan with special student benefits.")
else:
    print("Enter only 'yes' or 'no' answers.")