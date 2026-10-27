
candidates = [
    {"name": "Ravi", "marks": 85, "assessment": 90, "attendance": 92},
    {"name": "Priya", "marks": 90, "assessment": 90, "attendance": 95},
    {"name": "Arun", "marks": 85, "assessment": 90, "attendance": 92},
    {"name": "Kiran", "marks": 60, "assessment": 70, "attendance": 80}
]

qualified = []

for c in candidates:
    if (c["marks"] >= 70 and
        c["assessment"] >= 60 and
        c["attendance"] >= 75):

        c["total"] = c["marks"] + c["assessment"]
        qualified.append(c)

# Ranking: total score, assessment score,
# marks, attendance, then name alphabetically
qualified.sort(
    key=lambda c: (
        -c["total"],
        -c["assessment"],
        -c["marks"],
        -c["attendance"],
        c["name"]
    )
)

print("INTERNSHIP CANDIDATE RANKING")
print("-" * 55)

for rank, c in enumerate(qualified, start=1):
    print(
        rank, c["name"],
        "Marks:", c["marks"],
        "Assessment:", c["assessment"],
        "Attendance:", c["attendance"],
        "Total:", c["total"]
    )

print("\nNot Qualified:")
for c in candidates:
    if c not in qualified:
        print(c["name"])
