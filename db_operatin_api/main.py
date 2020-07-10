from flask import Flask, request, jsonify
import requests
import function as fn

app = Flask(__name__) # Flaskクラスのインスタンス生成

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/item_data', methods=['POST'])
    def receive_item_data():
        if request.method == 'POST':
            # jsonをパースできる
            data = request.get_json()

            if fn.analysis_json(data):
                return jsonify({'message': '書き込み成功'}), 200
            else:
                return jsonify({'message': '書き込み失敗'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True) 