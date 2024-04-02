from flask import Flask, render_template
from flask_restx import Api, Resource
from flask_qrcode import QRcode

app = Flask(__name__)
api = Api(app)
QRcode(app)

@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return render_template('index.html')
    
@app.route('/qr')
def qr():
    return render_template('index.html')
if __name__ == '__main__' :
    app.run(debug=True)