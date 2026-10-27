
teams = {}
n = int(input("Enter number of teams: "))

for i in range(n):
    print(f"\nTeam {i + 1}")
    name = input("Enter team name: ")

    size = int(input("Enter number of students: "))

    if size < 2 or size > 4:
        print("Invalid team size! Team must have 2 to 4 students.")
        continue

    students = []

    for j in range(size):
        student = input(f"Enter student {j + 1} name: ")
        score = float(input("Enter student score: "))
        students.append({"name": student, "score": score})

    round_scores = []

    for r in range(3):
        score = float(input(f"Enter Round {r + 1} score for {name}: "))
        round_scores.append(score)

    teams[name] = {
        "students": students,
        "round_scores": round_scores,
        "total": sum(round_scores)
    }

# Rank teams by total score, then final-round score
ranking = sorted(
    teams.items(),
    key=lambda item: (
        item[1]["total"],
        item[1]["round_scores"][2]
    ),
    reverse=True
)

print("\n===== HACKATHON RANKINGS =====")

for rank, (name, data) in enumerate(ranking, start=1):
    print(f"\nRank: {rank}")
    print(f"Team: {name}")
    print(f"Students: {len(data['students'])}")
    print("Student Scores:")

    for student in data["students"]:
        print(f"  {student['name']}: {student['score']}")

    print(f"Round Scores: {data['round_scores']}")
    print(f"Total Score: {data['total']}")

print("\nHackathon ranking completed!")
