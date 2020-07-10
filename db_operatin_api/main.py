from flask import Flask, request, jsonify
import requests
import function as fn

app = Flask(__name__) # Flaskクラスのインスタンス生成

@app.route('/') # URL指定。URLにリクエストが来ると関数内が実行される。
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    

    @app.route('/item_data', methods=['POST'])
    def receive_item_data():
        if request.method == 'POST':
            # jsonをパースできている
            data = request.get_json()

            res = fn.analysis_json(data)
            return res
            # return data
            # return jsonify(data),200
            # result = True
            # if result:
            #     return jsonify({'message': '書き込み成功'}), 200
            # else:
            #     return jsonify({'message': '書き込み失敗'}), 500

    # 次にDBに書き込む処理を書いていく。その返り値によってリターンを変える。
    app.run(host='127.0.0.1', port=8080, debug=True) 