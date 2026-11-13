from flask import Flask, request, jsonify

app = Flask(__name__)

# Danh sách lưu trữ team code tạm thời
team_codes_queue = []

@app.route('/api/nhan-code', methods=['POST'])
def nhan_code():
    data = request.get_json()
    if data and "team_code" in data:
        code = data["team_code"]
        team_codes_queue.append(code)
        return jsonify({"status": "success", "team_code": code}), 200
    return jsonify({"status": "error"}), 400

@app.route('/api/lay-code', methods=['GET'])
def lay_code():
    if team_codes_queue:
        # Lấy team code cũ nhất ra khỏi hàng đợi
        code = team_codes_queue.pop(0)
        return jsonify({"status": "success", "team_code": code}), 200
    return jsonify({"status": "empty", "team_code": None}), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "online"}), 200
