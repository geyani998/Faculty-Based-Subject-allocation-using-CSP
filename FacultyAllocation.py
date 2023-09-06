import random
def faculty_scheduling(subjects, faculty, constraints):
    # Initialize the solution to a random assignment of subjects to faculty
    solution = {subject: random.choice(faculty) for subject in subjects}
    
    # Define the evaluation function
    def evaluate(solution):
        # Initialize the score to 0
        score = 0
        # Iterate over the subjects and count the number of satisfied constraints
        for subject, faculty_member in solution.items():
            for constraint in constraints:
                if constraint(subject, faculty_member, solution):
                    score += 1
        return score
    
    # Define the function for generating a new solution
    def generate_new_solution(solution):
        # Choose a random subject and a random faculty member
        subject = random.choice(list(solution.keys()))
        faculty_member = random.choice(faculty)
        # Create a new solution by assigning the subject to the faculty member
        new_solution = dict(solution)
        new_solution[subject] = faculty_member
        return new_solution
    
    # Initialize the best solution to the current solution
    best_solution = solution
    # Initialize the best score to the score of the current solution
    best_score = evaluate(solution)
 # Run the local search loop
    while True:
        # Generate a new solution
        new_solution = generate_new_solution(solution)
        # Calculate the score of the new solution
        new_score = evaluate(new_solution)
        # If the new solution is better than the current solution, update the current solution
        if new_score > best_score:
            solution = new_solution
            best_score = new_score
        # If the new solution is not better than the current solution, accept it with a probability proportional to the difference in scores
        else:
            acceptance_probability = (new_score - best_score) / best_score
            if random.uniform(0, 1) < acceptance_probability: 
                solution = new_solution
        # If the current solution is the best solution found so far, update the best solution
        if best_score > evaluate(best_solution):
            best_solution = solution
        # If no further improvements can be made, return the best solution
        if best_score == evaluate(solution):
            return best_solution
def availability_constraint(subject, faculty_member, solution):
    return faculty_member in subject.available_faculty

def workload_constraint(subject, faculty_member, solution):
    return sum(1 for s, f in solution.items() if f == faculty_member) < faculty_member.max_classes

def conflict_constraint(subject, faculty_member, solution):
    for s, f in solution.items():
        if s.conflicts_with(subject) and f == faculty_member:
            return False
    return True

# Example usage:
subjects = [Subject1, Subject2, Subject3]
faculty = [Faculty1, Faculty2, Faculty3]
constraints = [availability_constraint, workload_constraint, conflict_constraint]

solution = faculty_scheduling(subjects, faculty, constraints)





