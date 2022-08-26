class GPA:
    
    def __init__(self, d):
        self.dictionary = d
        self.grades = {"A": 4, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "D": 1.0, "F": 0.0}

    def get_gpa(self):
        total_credit = 0
        quality_points = 0
        for i in self.dictionary:
            total_credit += self.dictionary[i]
            print("Enter the grade in", end=" ")
            grade = input(i)
            grade = self.grades[grade]
            sum = grade * self.dictionary[i]
            quality_points += sum
            sum = 0
        return quality_points / total_credit


sem1 = GPA({"PF": 3, "PFL": 1, "QT": 0.5, "ICT": 2, "ICTL": 1, "Eng": 3, "PST": 2})
gpa = sem1.get_gpa()
print(gpa)
