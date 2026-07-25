# ASSESSMENT TASK
print("=" * 70)
print("HOWDY WIZARD, TIME FOR THE GRADE COMPUTATION")
print("WIZARDRY TASKS")
print("=" * 70)
ass1total = int(input("\nWhat is the total number of items in Assignment 1? "))
ass1score = int(input("What is thy person score? "))

quiz1total = int(input("\nWhat is the total number of items in Quiz 1? "))
quiz1score = int(input("What is thy person score? "))

act1total = int(input("\nWhat is the total number of items in Activity 1? "))
act1score = int(input("What is thy person score? "))

act2total = int(input("\nWhat is the total number of items in Activity 2? "))
act2score = int(input("What is thy person score? "))

act3total = int(input("\nWhat is the total number of items in Activity 3? "))
act3score = int(input("What is thy person score? "))
totScores = ass1score + quiz1score + act1score + act2score + act3score;
totNoi = ass1total + quiz1total + act1total + act2total + act3total;

print(f"\nTotal number of items in the Assessment Task: {totNoi}");
print(f"\nTotal score in Assessment Task: {totScores}");

finalAt = (totScores/totNoi) * 100;
print(finalAt)

compAt = int(input("\nWhat is the percentage of the Assessment Task? Limaw: "))
coverAt = compAt / 100;
perAt = coverAt * 100;

print(f"The percentage in grade for Assessment Task is {perAt}%")
print("=" * 70)

print("\nTIME FOR THE LONGGGGG EXAM WIZARD!")
print("=" * 70)
long1tot = int(input("\nWhat is the total number of items in Long Exam 1: "))
long1score = int(input("What is the score of the student? "))

long2tot = int(input("\nWhat is the total number of items in Long Exam 2: "))
long2score = int(input("What is the score of the student? "))

totExamScores = long1score + long2score;
totExamNoi = long1tot + long2tot;

print(f"\nTotal number of items: {totExamNoi}");
print(f"Total score: {totExamScores}");

compExam = int(input("What is the percentage of the Long Exams? Limaw: "))
coverExam = compExam / 100;
perExam = coverExam * 100;

print("=" * 70)
print("\nTime for the Departmental Exam")
print("=" * 70)

deptTotal = int(input("What is the total number of items in the Departmental Exam: "))
deptScore = int(input("What is the score of the student: "))
deptComp = int(input("What is the percentage of the Departmental Exam: "))

deptCover = deptComp / 100;
deptPer = (deptScore / deptTotal) * 100;

# CALCULATION OF GRADES
weightedAt = finalAt * coverAt
weightedExam = ((totExamScores / totExamNoi) * 100) * coverExam
weightedDept = deptPer * deptCover

finalGrade = (weightedAt) + (weightedExam) + (weightedDept)

# FINAL TABLE GWRAHHH
print("\n" + "=" * 70)
print("GRADE SUMMARY")
print("=" * 70)
print(f"{'Component':<20}{'Score':>10}{'Raw%':>12}{' Percentage':>10}{'Grade':>12}")
print("-" * 70)
print(f"{'Assessment Task':<20}{f'{totScores}/{totNoi}':>10}{finalAt:>11.2f}%{compAt:>9}%{weightedAt:>11.2f}%")
print(f"{'Long Exams':<20}{f'{totExamScores}/{totExamNoi}':>10}{(totExamScores/totExamNoi)*100:>11.2f}%{compExam:>9}%{weightedExam:>11.2f}%")
print(f"{'Departmental Exam':<20}{f'{deptScore}/{deptTotal}':>10}{deptPer:>11.2f}%{deptComp:>9}%{weightedDept:>11.2f}%")
print("-" * 70)
print(f"{'FINAL GRADE':<52}{finalGrade:>17.2f}%")
print("=" * 70)