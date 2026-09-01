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
def home():
    return jsonify({
        "message": "Student API is running!",
        "routes": {
            "GET /": "Show all available routes",
            "POST /students": "Add a new student",
            "GET /students": "Get all students",
            "GET /students/<id>": "Get a student by USN",
            "PATCH /students/<id>": "Update a student by USN",
            "DELETE /students/<id>": "Delete a student by USN",
            "GET /students/passed": "Get names of students who passed",
            "GET /students/stats": "Get student statistics",
            "GET /test": "Test whether the API is working"
        }
    })


@app.post("/students")
def add_student():
    data = request.get_json()
    LIST.append(data)
    return jsonify(LIST[-1]), 201


@app.get("/students")
def get_students():
    return jsonify(LIST), 200


@app.get("/students/<id>")
def get_student_by_id(id):
    for student in LIST:
        if student["usn"] == id:
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.patch("/students/<id>")
def update_student(id):
    data = request.get_json()

    for student in LIST:
        if student["usn"] == id:
            student.update(data)
            return jsonify(student)

    return jsonify({"error": "Student not found"}), 404


@app.delete("/students/<id>")
def delete_student(id):
    for student in LIST:
        if student["usn"] == id:
            LIST.remove(student)
            return jsonify(LIST)

    return jsonify({"error": "Student not found"}), 404


@app.get("/students/passed")
def get_passed():
    passed_students = []

    for student in LIST:
        if student["marks"] >= 40:
            passed_students.append(student["name"])

    return jsonify(passed_students)


@app.get("/students/stats")
def calc_stats():
    if not LIST:
        return jsonify({
            "total students": 0,
            "average marks": 0,
            "highest marks": 0,
            "lowest marks": 0
        })

    marks = [student["marks"] for student in LIST]

    return jsonify({
        "total students": len(LIST),
        "average marks": sum(marks) / len(marks),
        "highest marks": max(marks),
        "lowest marks": min(marks)
    })


@app.get("/test")
def test():
    return "API is working fine"


if __name__ == "__main__":
    app.run(debug=True)