students = [("Squidward,", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

# sorts based on first column in tupple
students.sort()
for i in students:
    print(i)


grade = lambda grades:grades[1]
students.sort(key=grade)

