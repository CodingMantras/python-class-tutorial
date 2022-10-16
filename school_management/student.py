from person import Person
from choices import ClassName
from helper import LoadStudentData, write_file


class Student(Person):
    school_name = 'Happy School'

    def __init__(self, fname, lname, contact, rollnum, classname):
        super().__init__(fname, lname, contact)
        self.id = 0
        self.rollnum = rollnum
        self.email = f"{self.fname}_{self.lname}@{Student.school_name.replace(' ', '')}.com"
        self.filename, self.data = LoadStudentData().load_data()

        if isinstance(classname, ClassName):
            self.classname = classname.name
        else:
            print(f"[INFO] classname should one of the following...")
            print(ClassName.get_classnames_dict())
            print("[DEFAULT] Setting classname ONE.")
            self.classname = ClassName.get_default_class()

    def get_id(self):
        if self.data == []:
            return self.id
        else:
            return self.data[-1]["id"] + 1

    def student_data(self):
        student = {}
        student["id"] = self.get_id()
        student["fname"] = self.fname.capitalize()
        student["lname"] = self.lname.capitalize()
        student["email"] = self.email
        student["rollnum"] = self.rollnum
        student["contact"] = self.get_contact()
        student["class"] = self.classname
        return student

    def print_instance_detail(self):
        print("===================================================")
        for k, v in self.student_data().items():
            print(f"{k}:{v}")

    @classmethod
    def change_schoolname(cls, schoolname):
        cls.school_name = schoolname

    def __str__(self):
        return f"{self.rollnum}-{self.fname}"


class SaveStudent:
    def __init__(self, student):
        if isinstance(student, Student):
            self.student = student.student_data()
        else:
            print("[ERROR] Unable to create new student instance...")
        self.mode = 'w'
        self.fl, self.student_data = LoadStudentData().load_data()
        self.save()

    def save(self):
        self.student_data.append(self.student)
        write_file(self.fl, self.mode, self.student_data)


class UpdateStudent:
    def __init__(self, id):
        self.id = id
        self.mode = 'w'
        self.fl, self.student_data = LoadStudentData().load_data()

    def get_student(self):
        for stu in self.student_data:
            if stu["id"] == self.id:
                student_tbu = stu
        return student_tbu

    def update(self, stu):
        self.student_data[self.id] = stu
        write_file(self.fl, self.mode, self.student_data)


class DeleteStudent:
    def __init__(self, id):
        self.id = id
        self.mode = 'w'
        self.fl, self.student_data = LoadStudentData().load_data()
        self.delete()

    def delete(self):
        self.student_data.pop(self.id)
        write_file(self.fl, self.mode, self.student_data)


if __name__ == '__main__':
    cl = ClassName.FIVE
    std1 = Student("Anubhav", "Mishra", "0123456789", "1002", cl)
    print(std1.school_name)
    std1.change_schoolname("hahaha school")
    print(std1.school_name)
