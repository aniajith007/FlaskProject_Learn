from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/home')
def hell():
    return render_template('index.html',name="It's Meee Jeswa...")

@app.route('/get_data', methods=['GET'])
def get_data():
    # Dummy data for demonstration
    data = "This is data fetched from the server!"
    return data

if __name__ == '__main__':
    app.run(debug=True)
