admitted = []
not_admitted = []

# Credit grades attainable for each subject
credit_grades = ["A", "B", "C"]

# Required subjects per department
cs_required_subjects = ["English", "Mathematics", "Physics", "Chemistry", "ICT"]
mc_required_subjects = ["English", "Literature", "Government", "History", "Mathematics"]

# Function to evaluate the candidate
def evaluate_candidate(name, dept, jamb_score, interview_passed, subjects):
    if dept == "Computer Science":
        required_subjects = cs_required_subjects
    elif dept == "Mass Communication":
        required_subjects = mc_required_subjects

    # Check if the candidate has the required credits in each subject
    has_required_credits = True
    for subject in required_subjects:
        grade = subjects.get(subject, "F")
        if grade not in credit_grades:
            has_required_credits = False
            break

    # Determine if the candidate is admitted based on the department
    if dept == "Computer Science":
        passed = jamb_score >= 250 and has_required_credits and interview_passed
    elif dept == "Mass Communication":
        passed = jamb_score >= 230 and has_required_credits and interview_passed


    if passed:
        admitted.append(name)
        print(f"{name} is admitted into {dept}.")
    else:
        not_admitted.append(name)
        print(f"{name} is NOT admitted into {dept}.")

candidates = [
    ["Faith", "Computer Science", 255, True, {"English": "B", "Mathematics": "A", "Physics": "C", "Chemistry": "B", "ICT": "A"}],
    ["John", "Mass Communication", 228, True, {"English": "B", "Literature": "A", "Government": "B", "History": "C", "Mathematics": "C"}],
    ["Mira", "Mass Communication", 230, True, {"English": "B", "Literature": "B", "Government": "C", "History": "D", "Mathematics": "C"}],
    ["Uche", "Computer Science", 260, True, {"English": "A", "Mathematics": "B", "Physics": "B", "Chemistry": "C", "ICT": "A"}]
]

# Evaluate all candidates
for candidate in candidates:
    name, dept, jamb_score, interview_passed, subjects = candidate
    evaluate_candidate(name, dept, jamb_score, interview_passed, subjects)

# Display admitted and not admitted candidates
print("\nAdmitted:", admitted)
print("Not Admitted:", not_admitted)

