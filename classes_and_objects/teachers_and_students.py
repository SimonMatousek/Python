class Teacher:
    def giveAnswer():
        print("The teacher is answering the qustion")
    def teach(student):
        student.learn()
class Student:
    def learn():
        print("the student is actually learning")
    def question(teacher):
        teacher.giveAnswer()
if __name__ == "__main__":
    hofmann = Teacher
    gabriel = Student
    hofmann.giveAnswer()
    gabriel.learn()
    hofmann.teach(gabriel)
    gabriel.question(hofmann)
    