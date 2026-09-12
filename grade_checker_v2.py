def check_grade(score):
    if score >= 80:
        return "Grade A"
    elif score >= 75:
        return "Grade B+"
    elif score >= 70:
        return " Grade B"
    elif score >= 65:
        return "Grade C+"
    elif score >= 60:
        return "Grade C"
    elif score >=50:
        return "Pass"
    else:
        return "Fail"
while True: 
    name = input("Enter your name: ")
    score = int(input("Enter your score: "))
    grade = check_grade(score)
    print()
    print("----- UDA Grade Report-----")
    print("student:", name)
    print("score:", score)
    print("Result:", grade)
    again = input("Check another student? (yes/no): ").lower()
    if again == "no":
        print("Thanks for using UDS Grade Checker!👋")
        break