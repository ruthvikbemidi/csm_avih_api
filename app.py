from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return f"Hello my name is ruthvik"


@app.route('/students', methods=['GET'])
def get():
  return jsonify(students)

@app.route('/student/<student_id>', methods=['GET'])
def get_student_details(student_id):
  for i in students:
    if(student_id.upper() == i['id']):
      data = i;
  return jsonify(data)

if __name__ == "__main__":
  app.run(debug=True)
