from flask import Flask 
import psycopg2 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, AWS!'

@app.route('/d')
def details():
    return 'This is a Flask app running on AWS without connecting to PostgreSQL! ' \
    'This is deployed using ec2 !!'



if __name__=='__main__':
    app.run(debug=True)
