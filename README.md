# Faculty-Based-Subject-allocation-using-CSP
This GitHub repository presents a practical solution for mapping faculty to subjects within a university setting. The project tackles the subject-faculty allocation problem using a constraint satisfaction approach, specifically a hill-climbing algorithm. By implementing local search and iteratively adjusting allocations to meet constraints, this system efficiently optimizes subject-faculty assignments. The limitation of the hill climbing approach is overcome by updating the bes solution with a probability proportional to the difference in scores. 


Constraints: 

Availability_constraint: Checks that the selected faculty member is available to teach the subject

Workload_constraint:  Checks that the faculty member has not reached their maximum number of classes

Conflict_constraint: Checks that the faculty member is not already teaching a subject that conflicts with the current subject. 

Domain:  Subject names: Subject1, Subject2, Subject3

Variables: Faculty names: Faculty1, Faculty2, Faculty3

Key Features:

    Constraint Satisfaction: Utilizes a constraint satisfaction problem (CSP) framework to allocate faculty members to subjects while adhering to specific constraints and requirements.

    Hill-Climbing Algorithm: Employs a hill-climbing approach within the local search to iteratively improve subject-faculty assignments by finding the best possible allocation.

    Iterative Optimization: The system continuously refines the allocation, ensuring that faculty members are assigned to subjects that align with their expertise and constraints are satisfied.

    Scalability: Designed to handle the allocation of subjects to faculty members in a working university, making it adaptable to various educational institutions.

    Constraint Management: The project efficiently manages constraints, such as faculty availability, subject prerequisites, and workload distribution, to produce a feasible and optimized allocation.
