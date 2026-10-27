
attendance = float(input("Enter attendance percentage: "))
lab = input("Are all laboratories completed? (yes/no): ").lower()
internal = float(input("Enter internal assessment marks (out of 30): "))
fees = input("Are all fees cleared? (yes/no): ").lower()

print("\n===== EXAMINATION ELIGIBILITY =====")

eligible = True

if attendance < 75:
    print("Not eligible: Attendance must be at least 75%.")
    eligible = False

if lab != "yes":
    print("Not eligible: Laboratory work is incomplete.")
    eligible = False

if internal < 15:
    print("Not eligible: Minimum 15 internal marks required.")
    eligible = False

if fees != "yes":
    print("Not eligible: Fee payment is pending.")
    eligible = False

if eligible:
    print("Congratulations! You are eligible for the final examination.")
else:
    print("You are NOT eligible for the final examination.")
