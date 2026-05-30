from flask import Flask
import pickle

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def home():
    return "Email Spam Detection App"

if __name__ == "__main__":
    app.run(debug=True)