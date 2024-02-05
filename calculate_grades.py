# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def get_grades(num_student):
    """Collect grades from the user."""
    grade_list = []
    for _ in range(num_student):
        grade_list.append(int(input('Enter a number: ')))
    return grade_list

def calculate_mean(grades):
    """Calculate the mean of the grades."""
    total = sum(grades)
    return total / len(grades)

def calculate_standard_deviation(grades, mean):
    """Calculate the standard deviation of the grades."""
    sum_of_sqrs = sum((grade - mean) ** 2 for grade in grades)
    return math.sqrt(sum_of_sqrs / len(grades))

def print_statistics(mean, standard_deviation):
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(standard_deviation, 3))
    print('****** END ******')

def print_stat():
    num_student = 5
    grades = get_grades(num_student)
    mean = calculate_mean(grades)
    standard_deviation = calculate_standard_deviation(grades, mean)
    print_statistics(mean, standard_deviation)

print_stat()