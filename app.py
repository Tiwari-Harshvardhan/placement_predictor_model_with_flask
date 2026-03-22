from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        cgpa = float(request.form['cgpa'])
        iq = int(request.form['iq'])
        response = requests.post('http://localhost:8000/predict', json={'cgpa': cgpa, 'iq': iq})
        if response.status_code == 200:
            prediction = response.json()['placement']
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)