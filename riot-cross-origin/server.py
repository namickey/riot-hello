from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/j', methods=['GET'])
def jso():
    j = {'title':'hello world'}
    response = jsonify(j)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    app.run()

