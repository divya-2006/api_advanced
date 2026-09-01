from flask import Flask, request, jsonify
app = Flask(__name__)

LIST = [
    {
        "usn": "101",
        "name": "Arjun",
        "age": 20,
        "course": "Computer Science",
        "marks": 85
    },
    {
        "usn": "102",
        "name": "Priya",
        "age": 21,
        "course": "Electronics",
        "marks": 90
    },
    {
        "usn": "103",
        "name": "Rahul",
        "age": 19,
        "course": "Mechanical Engineering",
        "marks": 39
    },
    {
        "usn": "104",
        "name": "Sneha",
        "age": 22,
        "course": "Information Technology",
        "marks": 20
    }
]

@app.get("/")
class StudentClass:
    def __init__(self, usn, name,  age, course, marks):
        self.usn = usn
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks
    def  calculate_grade(self, marks):
        if self.marks >= 80:
            return f"Your grade is A"
        elif self.marks >=60 and self.marks < 80 :
            return f"Your grade is B"
        elif self.marks >=40 and self.marks < 60:
            return f"Your grade is C"
        elif self.marks < 40:
            return f"Your grade is F"
    def get_details(self):
        return f"Student name is {self.name}, her USN is{self.student_id}, her age is {self.age}, she is studying course is {self.course}, she scored{self.marks}"
@app.post("/students")
def add_student():
    data = request.get_json()
    LIST.append(data)  
    return LIST[-1], 201  
@app.get("/students")    
def get_students():
    return LIST, 200 
@app.get("/students/<id>")
def get_student_by_id(id):
    student_name = ""
    for i in LIST:
        if i["usn"] == id:
            student_name = i["name"]
    return student_name
@app.patch("/students/<id>")
def update_student(id):
    name = request.args.get("name")
    age = request.args.get("age")
    course = request.args.get("course")
    marks = request.args.get("marks")
    for i in LIST:
        student = i
        if i["usn"] == id:
            i["name"] = name
            i["age"] = age
            i["course"] = course
            i["marks"] = marks
    return student
            
@app.delete("/students/<id>")
def delete_student(id):
    for i in LIST:
        if i["usn"] == id:
            del i
    return LIST
@app.get("/students/passed")
def get_passed():
    passed_students = []
    for i in LIST:
        if i["marks"] > 40:
            passed_students.append(i["name"])
    return jsonify(passed_students)
@app.route("/students/stats")
def calc_stats():
    total_students = 0
    average_marks = 0
    highest_marks = 0
    lowest_marks = 1000
    grand_total_marks = 0
    for i in LIST:
        total_students +=1
        grand_total_marks += i["marks"]
        if i["marks"] > highest_marks:
            highest_marks = i["marks"]
        else:
            lowest_marks = i["marks"]
    average_marks = grand_total_marks/total_students
    return jsonify({
        "total students": total_students,
        "average marks": average_marks,
        "highest marks": highest_marks,
        "lowest marks": lowest_marks,
    })
@app.get("/test")
def test():
    return "API is working fine"

if __name__ == "__main__":
    app.run(debug = True)
    
    