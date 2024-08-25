from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        # Check if the request is JSON
        if request.is_json:
            data = request.json.get('data', [])
            numbers = [x for x in data if x.isdigit()]
            alphabets = [x for x in data if x.isalpha()]
            lowercase_alphabets = [x for x in alphabets if x.islower()]

            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_lowercase_alphabet": [max(lowercase_alphabets)] if lowercase_alphabets else []
            }

            return jsonify(response), 200
        else:
            return jsonify({"is_success": False, "error": "Content-Type must be application/json"}), 415
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def handle_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
