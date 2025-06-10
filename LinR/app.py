from flask import Flask,render_template,request,redirect,url_for
import pickle

app=Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        DMC = float(request.form['DMC'])
        DC = float(request.form['DC'])
        ISI = float(request.form['ISI'])
        BUI = float(request.form['BUI'])

        scaled_features = scaler.transform([[DMC, DC, ISI, BUI]])
        prediction = model.predict(scaled_features)
    return render_template('predict.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)