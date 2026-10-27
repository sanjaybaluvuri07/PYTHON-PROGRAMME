
teams = {}

n = int(input("Enter number of teams: "))

for i in range(n):
    name = input(f"Enter team {i + 1} name: ")
    teams[name] = {
        "played": 0,
        "won": 0,
        "drawn": 0,
        "lost": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0
    }

matches = int(input("Enter number of matches: "))

for i in range(matches):
    print(f"\nMatch {i + 1}")

    team1 = input("Enter first team: ")
    team2 = input("Enter second team: ")

    if team1 not in teams or team2 not in teams or team1 == team2:
        print("Invalid team names! Match skipped.")
        continue

    score1 = int(input(f"Goals scored by {team1}: "))
    score2 = int(input(f"Goals scored by {team2}: "))

    if score1 < 0 or score2 < 0:
        print("Invalid score! Match skipped.")
        continue

    teams[team1]["played"] += 1
    teams[team2]["played"] += 1

    teams[team1]["goals_for"] += score1
    teams[team1]["goals_against"] += score2

    teams[team2]["goals_for"] += score2
    teams[team2]["goals_against"] += score1

    if score1 > score2:
        teams[team1]["won"] += 1
        teams[team1]["points"] += 3
        teams[team2]["lost"] += 1

    elif score2 > score1:
        teams[team2]["won"] += 1
        teams[team2]["points"] += 3
        teams[team1]["lost"] += 1

    else:
        teams[team1]["drawn"] += 1
        teams[team2]["drawn"] += 1
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1

# Calculate goal difference
for name in teams:
    teams[name]["goal_difference"] = (
        teams[name]["goals_for"] -
        teams[name]["goals_against"]
    )

# Rank teams according to competition policy
ranking = sorted(
    teams.items(),
    key=lambda item: (
        item[1]["points"],
        item[1]["goal_difference"],
        item[1]["goals_for"]
    ),
    reverse=True
)

print("\n========== TOURNAMENT RANKINGS ==========")
print("Rank Team       P  W  D  L  GF  GA  GD  Points")

for rank, (name, data) in enumerate(ranking, start=1):
    print(
        f"{rank:<5}{name:<11}"
        f"{data['played']:<3}"
        f"{data['won']:<3}"
        f"{data['drawn']:<3}"
        f"{data['lost']:<3}"
        f"{data['goals_for']:<4}"
        f"{data['goals_against']:<4}"
        f"{data['goal_difference']:<4}"
        f"{data['points']}"
    )
