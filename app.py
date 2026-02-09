from flask import Flask, jsonify, request
import datetime

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def return_json():
    if request.method == 'GET':
        data = {
            "status": "ok",
            "service": "ecs-demo",
            "timestamp": datetime.datetime.now()
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)