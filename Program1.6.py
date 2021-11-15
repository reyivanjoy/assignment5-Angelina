print("Section 8. GRADING SYSTEM - Polytechnic University of the Philippines")
grade = float(input("Final Grade: "))
if grade >=96.5 and grade <=100:
    print("Grade Mark: 1.0")
    print("Excellent")
elif grade >=93.5 and grade <=96.4:
    print("Grade Mark: 1.25")
    print("Excellent")
elif grade >=90.5 and grade <=93.4:
    print("Grade Mark 1.50")
    print("Very Good")
elif grade >=87.5 and grade <=90.4:
    print("Grade Mark: 1.75")
    print("Very Good")
elif grade >=84.5 and grade <=87.4:
    print("Grade Mark: 2.00")
    print("Good")
elif grade >=81.5 and grade <=84.4:
    print("Grade Mark: 2.75")
    print("Good")
elif grade >=78.5 and grade <=81.4:
    print("Grade Mark: 2.50")
    print("Satisfactory")
elif grade >=75.5 and grade <=78.4:
    print("Grade Mark: 2.75")
    print("Satisfactory")
elif grade >=74.5 and grade <=75.4:
    print("Grade Mark: 3.00")
    print("Passing")
elif grade >=64.5 and grade <=74.4:
    print("Grade Mark: 5.00")
    print("Failure")
else:
    print("May be Incomplete(INC.), Withdrawn(W), or Dropped(D)")
