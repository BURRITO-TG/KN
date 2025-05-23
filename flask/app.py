from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        # Process the user input as needed
        return render_template('result.html', name=name)
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(debug=True)