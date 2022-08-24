from flask import Flask, render_template, request
import re

app = Flask(__name__)

##########################################

@app.route('/', methods=['GET', 'POST'])
def fun_1():
    if request.method == 'POST':
        txt = request.form['in_1']
        reg = request.form['in_2']
        x = re.findall(reg, txt)
        l = len(x)
        return "No of Matches : {} and List of match : {}".format(l,x)

    return render_template("index.html")


#########################################

if __name__ == '__main__':
    app.run(debug=True)