# Define weightage for each component
exam_weight = 0.5
assignment_weight = 0.3
project_weight = 0.2

# Function to safely get a valid number input
#use def to declare the function
def get_valid_input(prompt):
    while True:
        try:
            # Try to convert the input to float
            return float(input(prompt))
        except ValueError:
            # If conversion fails, show an error message and ask again
            print("Invalid input. Please enter a numeric value.")

# Input marks for each component with error handling
exam_marks = get_valid_input("Enter exam marks: ")
assignment_marks = get_valid_input("Enter assignment marks: ")
project_marks = get_valid_input("Enter project marks: ")

# Calculate weighted average
final_marks = (exam_marks * exam_weight) + (assignment_marks * assignment_weight) + (project_marks * project_weight)

# Determine grade based on final marks
if 90 <= final_marks <= 100:
    grade = 'A'
elif 80 <= final_marks < 90:
    grade = 'B'
elif 70 <= final_marks < 80:
    grade = 'C'
elif 60 <= final_marks < 70:
    grade = 'D'
else:
    grade = 'F'

# Print final marks and grade
print(f"Final Marks: {final_marks:.2f}")
print(f"Grade: {grade}")
