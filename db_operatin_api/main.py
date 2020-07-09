from flask import Flask, request, jsonify
import requests

app = Flask(__name__) # Flaskクラスのインスタンス生成

@app.route('/') # URL指定。URLにリクエストが来ると関数内が実行される。
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    

    @app.route('/item_data', methods=['POST'])
    def receive_item_data():
        if request.method == 'POST':
            data = request.get_json()
            return data
            # return jsonify(data),418

    app.run(host='127.0.0.1', port=8080, debug=True) 