print("--- student database program ---")
student_database = {
    "101": {"name": "Aisha", "marks": 85, "city": "Delhi"},
    "102": {"name": "rahul", "marks": 92, "city": "mumbai"},
    "103": {"name": "vaishali", "marks": 79, "city": "dehradun"},
    "104": {"name": "amit", "marks": 89, "city": "jaipur"}
}

roll_no = input("please enter the roll number of student(101-104): ")

if roll_no in student_database:
    student = student_database[roll_no]
    print("\n---student ki details---")
    print(f"naam: {student['name']}")
    print(f"marks: {student['marks']}%")
    print(f"city: {student['city']}")
else:
    print("\nsorry this roll no is not database.")
