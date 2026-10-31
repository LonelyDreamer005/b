from flask import Flask, request, jsonify

app = Flask(__name__)

student = {
    1:{"id":1, "name":"vinay", "course":"cse"}, 
    2:{"id":2, "name":"haf", "course":"ece"}
}
nd = 3

@app.route('/')
def home():
    return "APP IS LIVE!"

@app.route('/student', methods=['GET'])
def get_students():
    return jsonify(list(student.values())), 200

@app.route('/students/<int:z>', methods=['GET'])
def get_student(z):
    if z not in student:
        return jsonify(
            {"Error":"Student Id doesn't exist"}
        ), 404
    return jsonify(student[z]), 200

@app.route('/student', methods=['POST'])
def cr_student():
    global nd
    data = request.get_json()
    
    if not isinstance(data, dict):
        return jsonify({"error":"JSON obj required"}), 400
    data["id"]=nd
    student[nd] = data
    nd += 1

    return jsonify(data), 201

@app.route('/student/<int:x>', methods=['PUT'])
def ed_student(x):
    if x not in student:
        return jsonify(
            {"Error":"Student Id doesn't exist"}
        ), 404
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error":"JSON obj required"}), 400
    student[x].update(data)
    student[x]["id"] = x

    return jsonify(student[x]), 200

@app.route('/student/<int:x>', methods=['PATCH'])
def edr_student(x):
    if x not in student:
        return jsonify(
            {"Error":"Student Id doesn't exist"}
        ), 404
    data = request.get_json()
    if not isinstance(data, dict):
        return jsonify({"error":"JSON obj required"}), 400
    data.pop("id", None)
    student[x].update(data)
    student[x]["id"] = x

    return jsonify(student[x]), 200

@app.route('/student/<int:x>', methods=['DELETE'])
def dl_student(x):
    if x not in student:
        return jsonify({"error": "Student not found"}), 404

    del student[x]
    return jsonify({"message": "Student deleted"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)