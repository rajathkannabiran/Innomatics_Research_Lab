from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def regex():
    text = request.form['input_text']
    pattern = request.form['regex_pattern']
    match = re.findall(pattern, text)
    
    return render_template('result.html', text=text, pattern=pattern, match=match, size=len(match))

@app.route('/email', methods=['GET', 'POST'])
def email():
    return render_template('email.html')

@app.route('/email-checker', methods=['GET', 'POST'])
def emailChecker():
    email = request.form["email"]
    if re.match(r'[A-Za-z][A-Za-z0-9.]*@[A-Za-z]+\.[A-Za-z]{2,}', email):
        return "The Email Id you entered is Valid !"
    else:
        return "The Email Id you entered is Invalid. Better Luck next time !"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)