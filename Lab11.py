import os
import matplotlib.pyplot as plt

def student_grade(name):
    with open("data/students.txt") as id:
        student_id = None

        for line in id:
            if name in line:
                student_id = line[:3]
                break
        if not student_id:
            print("Student not found")
            return

    # Build assignment points
    with open("data/assignments.txt") as id:
        lines = id.read().splitlines()
        assignment_points = {}
        for i in range(0, len(lines), 3):
            aid = lines[i+1]
            points = int(lines[i+2])
            assignment_points[aid] = points

    # Calculate grade
    total = 0
    for file in os.listdir("data/submissions"):
        with open(os.path.join("data/submissions", file)) as f:
            sid, aid, percent = f.read().strip().split("|")
            if sid == student_id and aid in assignment_points:
                total += (int(percent) / 100) * assignment_points[aid]

    print(f"{round(total / 1000 * 100)}%")
def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph")
    choice = input("Enter your selection: ").strip()