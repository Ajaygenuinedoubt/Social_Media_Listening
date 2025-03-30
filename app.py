from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

# Homepage route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the comment from the request
    comment = request.form['comment']

    # Ensure the comment is passed as a list (expected by the model)
    comment_list = [comment]

    # Make the prediction using the loaded model
    prediction = model.predict(comment_list)

    # Return the prediction as a JSON object
    return jsonify({"emotion": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True)
