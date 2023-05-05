from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/categories')
def categories():    
    return render_template('categories.html')

if __name__ == '__main__':
    app.run(debug=True)
