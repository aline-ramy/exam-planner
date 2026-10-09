subject = input("subject: ")
days_left = int(input("Days until the exam: "))
difficulty = int(input("Difficultyfrom 1 to 5: "))
hours_per_day =  difficulty *0.5
print(f"Study {subject} for {hours_per_day} hours everyday for {days_left} days")