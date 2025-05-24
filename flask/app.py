from flask import Flask,render_template,request,redirect,url_for

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
        age= request.form['age']
        # Process the user input as needed
        return redirect(url_for('submit_age', age=age))
    return render_template('submit.html')

@app.route('/submit_age/<int:age>', methods=['GET'])
def submit_age(age):
    if age>23:
        return "FOSSIL";
    elif age>=18:
        return "YOUR LIFE IS DONE";
    elif age>16:
        return "LAST CHANCE BRO";
    else:
        return "Live your life to the fullest";

if __name__ == '__main__':
    app.run(debug=True)