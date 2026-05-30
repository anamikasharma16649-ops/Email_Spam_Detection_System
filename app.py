from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

try:
    with open('model.pkl', 'rb') as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except:
    print("Model file not found!")
    model = None

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return render_template('index.html', prediction="Model not loaded!")

    message = request.form['message']
    
    if not message or message.strip() == '':
        return render_template('index.html', prediction="Please enter some text")
    
    try:
        prediction = model.predict([message])        
        if prediction[0] == 1:
            result = "Spam"
        else:
            result = "Not Spam"
            
        return render_template('index.html', prediction=result)
    
    except Exception as e:
        return render_template('index.html', prediction=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)

