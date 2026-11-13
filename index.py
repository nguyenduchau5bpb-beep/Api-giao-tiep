from flask import Flask, request, jsonify

app = Flask(__name__)

# Lưu ý: Trên Vercel, dữ liệu lưu trong biến toàn cục (như list này) 
# sẽ không lưu trữ vĩnh viễn vì serverless function sẽ "ngủ" sau khi xử lý xong request.
# Nếu bạn chỉ cần chuyển tiếp hoặc in log, cách này hoàn toàn ổn.
received_codes = []

@app.route('/api/nhan-code', methods=['POST'])
def nhan_team_code():
    data = request.get_json()
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    
    team_code = data.get("team_code")
    uid = data.get("uid")
    nickname = data.get("nickname")
    
    print(f"[API NHẬN] Team Code: {team_code} từ UID: {uid} ({nickname})")
    
    received_codes.append({
        "team_code": team_code,
        "uid": uid,
        "nickname": nickname
    })
    
    return jsonify({"status": "success", "message": "Received successfully"}), 200

@app.route('/api/lay-code', methods=['GET'])
def lay_team_code():
    if received_codes:
        item = received_codes.pop(0)
        return jsonify({"status": "success", "data": item}), 200
    return jsonify({"status": "empty", "data": None}), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"status": "online", "message": "Free Fire API Server is running on Vercel!"}), 200
