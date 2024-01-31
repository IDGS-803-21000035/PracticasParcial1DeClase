from flask import Flask, render_template, request
import forms
from math import sqrt

app = Flask(__name__)

@app.route("/distancia",  methods=["GET", "POST"])
def distancia():
    dist_form = forms.UserForm(request.form)
    dis = 0  
    if request.method == 'POST':
        x1 = dist_form.x1.data
        x2 = dist_form.x2.data
        y1 = dist_form.y1.data
        y2 = dist_form.y2.data

        d = int(sqrt(pow((x2-x1),2) + pow((y2-y1),2)))

        dis = d
    return render_template("distancia.html", forms=dist_form, dis=dis)

if __name__ == "__main__":
    app.run(debug=True)
