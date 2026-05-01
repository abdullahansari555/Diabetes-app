from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = [float(x) for x in request.form.values()]
        input_data = np.array(data).reshape(1, -1)

        prediction = model.predict(input_data)

        result = "Diabetes Positive ⚠️" if prediction[0] == 1 else "Diabetes Negative ✅"

        return render_template("index.html", prediction_text=result)

    except:
        return render_template("index.html", prediction_text="Invalid Input ❌")

if __name__ == "__main__":
    app.run(debug=True)