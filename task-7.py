
# Comprehensive Smart Campus Management Simulation

students = []
events = []
resources = [
    ["Computer Lab", 2, 0],
    ["Seminar Hall", 1, 0],
    ["Projector", 5, 0]
]

while True:
    print("\n===== SMART CAMPUS MANAGEMENT =====")
    print("1. Add Student")
    print("2. Record Attendance")
    print("3. Enter Marks")
    print("4. Register for Event")
    print("5. Allocate Resources")
    print("6. Summary Report")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ").strip()
        roll = input("Enter roll number: ").strip()

        if not name or not roll:
            print("Name and roll number cannot be empty.")
        elif any(s[1] == roll for s in students):
            print("Roll number already exists.")
        else:
            # Tuple stores student identity
            student = (roll, name)

            # Nested list: attendance and marks
            students.append([student, 0, 0, []])
            print("Student added successfully.")

    elif choice == "2":
        roll = input("Enter roll number: ").strip()
        found = False

        for student in students:
            (sid, name) = student[0]  # Tuple unpacking

            if sid == roll:
                status = input("Present or Absent (P/A): ").upper()

                if status == "P":
                    student[1] += 1
                    print("Attendance recorded.")
                elif status == "A":
                    print("Absence recorded (no present-day added).")
                else:
                    print("Invalid attendance status.")

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "3":
        roll = input("Enter roll number: ").strip()
        found = False

        for student in students:
            (sid, name) = student[0]

            if sid == roll:
                try:
                    mark = float(input("Enter marks (0-100): "))

                    if 0 <= mark <= 100:
                        student[2] += mark
                        student[3].append(mark)
                        print("Marks recorded.")
                    else:
                        print("Marks must be between 0 and 100.")
                except ValueError:
                    print("Enter a valid number.")

                found = True
                break

        if not found:
            print("Student not found.")

    elif choice == "4":
        roll = input("Enter roll number: ").strip()
        name_found = ""

        for student in students:
            (sid, name) = student[0]

            if sid == roll:
                name_found = name
                break

        if name_found:
            event_name = input("Enter event name: ").strip()

            if event_name:
                events.append((roll, name_found, event_name))
                print("Event registration successful.")
            else:
                print("Event name cannot be empty.")
        else:
            print("Student not found.")

    elif choice == "5":
        print("\nAvailable Resources:")
        for i, (name, total, allocated) in enumerate(resources, start=1):
            print(i, name, "Available:", total - allocated)

        try:
            number = int(input("Choose resource number: "))
            quantity = int(input("Enter quantity to allocate: "))

            if 1 <= number <= len(resources) and quantity > 0:
                resource = resources[number - 1]

                if quantity <= resource[1] - resource[2]:
                    resource[2] += quantity
                    print("Resource allocated successfully.")
                else:
                    print("Insufficient resources available.")
            else:
                print("Invalid resource number or quantity.")
        except ValueError:
            print("Enter valid numbers.")

    elif choice == "6":
        print("\n===== CAMPUS SUMMARY REPORT =====")
        print("Total Students:", len(students))
        print("Event Registrations:", len(events))

        print("\nStudent Details:")
        for student in students:
            (roll, name) = student[0]
            attendance = student[1]
            marks = student[3]

            average = sum(marks) / len(marks) if marks else 0

            print("Roll:", roll)
            print("Name:", name)
            print("Present Days:", attendance)
            print("Average Marks:", round(average, 2))

        print("\nEvent Registrations:")
        for roll, name, event_name in events:
            print(name, "-", event_name)

        print("\nResource Summary:")
        for name, total, allocated in resources:
            print(name, "Allocated:", allocated,
                  "Available:", total - allocated)

    elif choice == "7":
        print("Exiting Smart Campus Management. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
