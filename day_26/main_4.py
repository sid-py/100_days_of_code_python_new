import random

names = ["Alex", "Annemarie", "Jeaneatte", "Sarah", "Robert", "Patrick", "Jenny"]


students_score = {name:random.randint(1,100) for name in names }

passed_students = {name: score for (name, score) in students_score.items() if score > 40}

print(passed_students)