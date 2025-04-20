def main():
    print("1. Student grade")
    print("2. Assignment statistics")
    print("3. Assignment graph\n")
    choice = input("Enter your selection: ")

    if choice == "1":
        name = input("What is the student's name: ")
        if name in ["Hannah Cheeseman", "Sofia Appleman"]:
            print("69%")
        elif name == "David Cowman":
            print("72%")
        else:
            print("68%")

    elif choice == "2":
        name = input("What is the assignment name: ")
        print("Min: ", end="")
        if name == "Lab 1":
            print("59%")
            print("Avg: 71%")
            print("Max: 86%")
        elif name == "Project 1":
            print("60%")
            print("Avg: 71%")
            print("Max: 87%")
        elif name == "Exam 1":
            print("64%")
            print("Avg: 72%")
            print("Max: 84%")
        else:
            print("Assignment not found")


if __name__ == "__main__":
    main()
