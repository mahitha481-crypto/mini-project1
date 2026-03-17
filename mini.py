students={}
def add_student(name,marks):
    students[name]=marks
    print("student added")
def display_students():
    for name,marks in students.items():
        print(name,":",marks)
add_student("mahitha",90)
add_student("navya",85)
display_students()