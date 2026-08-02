# (a) Create student records
students = {}

# (b) Menu-driven student manager
while True:
    print("\n1. Add student")
    print("2. Update mark")
    print("3. Search student")
    print("4. Display averages and grades")
    print("5. Highest average")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        sid = input("Enter student ID: ")
        name = input("Enter name: ")
        marks = []
        for i in range(3):
            mark = int(input(f"Enter mark {i+1}: "))
            while mark < 0 or mark > 100:
                mark = int(input(f"Enter mark {i+1}: "))
            marks.append(mark)
        students[sid] = {"name": name, "marks": marks}
        print("Student added.")

    elif choice == "2":
        sid = input("Enter student ID: ")
        if sid in students:
            index = int(input("Enter mark number (1-3): ")) - 1
            if 0 <= index < 3:
                mark = int(input("Enter new mark: "))
                while mark < 0 or mark > 100:
                    mark = int(input("Enter new mark: "))
                students[sid]["marks"][index] = mark
                print("Mark updated.")
        else:
            print("Student not found.")

    elif choice == "3":
        sid = input("Enter student ID: ")
        if sid in students:
            print(students[sid])
        else:
            print("Student not found.")

    elif choice == "4":
        print("\nStudent Records:")
        for sid in students:
            total = 0
            for m in students[sid]["marks"]:
                total += m
            avg = total / 3

            if avg >= 80:
                grade = "A"
            elif avg >= 70:
                grade = "B"
            elif avg >= 60:
                grade = "C"
            elif avg >= 50:
                grade = "D"
            else:
                grade = "F"

            print(sid, "-", students[sid]["name"],
                  "Average:", round(avg, 2), "Grade:", grade)

    elif choice == "5":
        highest = -1
        for sid in students:
            total = 0
            for m in students[sid]["marks"]:
                total += m
            avg = total / 3
            if avg > highest:
                highest = avg

        print("Highest average student(s):")
        for sid in students:
            total = 0
            for m in students[sid]["marks"]:
                total += m
            avg = total / 3
            if avg == highest:
                print(sid, "-", students[sid]["name"],
                      "Average:", round(avg, 2))

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")