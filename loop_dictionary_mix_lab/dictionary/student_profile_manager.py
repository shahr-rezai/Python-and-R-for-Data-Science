# (a) Create and display original dictionary
student = {
    "name": "Bano",
    "id": "AUW123",
    "program": "Computer Science",
    "year": 2
}
print("Original Dictionary:")
print(student)

# (b) Update year of study
student["year"] = int(input("Enter new year of study: "))

# (c) Add email
student["email"] = "bano@example.com"

# (d) Display all keys and values
print("\nStudent Information:")
for k, v in student.items():
    print(k, ":", v)

# (e) Check if phone exists
print("\nPhone Key Check:")
print("phone exists" if "phone" in student else "phone does not exist")