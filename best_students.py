# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

# TODO: Use 'extract method' refactoring technique to improve this code.
# TODO: If required, use 'replace temp variable with query' technique to make it easier to extract methods.

class Employer:
    def __init__(self, name):
        self.name = name

    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        return self.gpa

    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students

    def process_graduation(self):
        passed_students = self.get_passed_students()
        self.print_graduated_students(passed_students)
        self.send_congrat_emails(passed_students)
        self.send_info_to_top_employers(passed_students)

    def get_passed_students(self):
        min_gpa = 2.5
        return [s for s in self.students if s.get_gpa() > min_gpa]

    def print_graduated_students(self, passed_students):
        print('*** Student who graduated ***')
        for s in passed_students:
            print(s.name)
        print('****************************')

    def send_congrat_emails(self, passed_students):
        for s in passed_students:
            s.send_congrat_email()

    def send_info_to_top_employers(self, passed_students):
        top_10_percent_students = self.get_top_percent_students(passed_students, 0.9)
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for employer in top_employers:
            employer.send(top_10_percent_students)

    def get_top_percent_students(self, students, percentile):
        students.sort(key=lambda s: s.get_gpa(), reverse=True)
        index = int(len(students) * (1 - percentile))
        return students[:index]

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2, 'kami'), Student(3, 'sarah')]
school = School(students)
school.process_graduation()