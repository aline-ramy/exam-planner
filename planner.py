subjects = []
count = int(input("How many subjects? "))

for i in range(count):
    name = input("Subject name: ")
    days_left = int(input("Days until the exam: "))
    difficulty = int(input("Difficulty from 1 to 5: "))
    subjects.append((name, days_left, difficulty))

total = 0
for name, days_left, difficulty in subjects:
    hours = difficulty * 0.5
    total += hours
    print(f"{name}: {hours} hours/day for {days_left} days")

print (f"Total study time per day: {total} hours")