class Student:
    def __init__(self, name, age = 13, grade = "12th"):
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def get_name(self):
        return self._name
    
    @get_name.setter
    def set_name(self, new_name):
        if isinstance( new_name, str):     
            self._name = new_name
        else:
            print("Must be string")

    @property
    def get_age(self):
        return self._age
    
    @get_age.setter
    def set_age(self, add_age):
        if isinstance(add_age, int) and (11 < add_age < 18):     
            self._age = add_age
        else:
            print("Must be a number")
            

    @property
    def get_grade(self):
        return self._grade
    
    @get_grade.setter
    def set_grade(self, add_grade):
        if isinstance(add_grade, str) and add_grade in ["9th", "10th", "11th", "12th"]:     
            self._grade = add_grade
        else:
            print("Must be between 9th and 12th grade")

    # def __str__(self):
    #     return f"{self._grade}th"
        

    # def __str__(self):
    #     return f"Grade: {self._grade}"
 

# person = Student("Alice")
# person.set_age = 13
# person.set_grade = 12
# print(person.get_grade)
# print(person.get_age, person.get_grade)