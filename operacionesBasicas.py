from flask import Flask, render_template, request

app = Flask(__name__)


#decorador para formulario1
@app.route("/formulario1")
def formulario():
    return render_template("operaciones.html")

@app.route("/resultado", methods = ["GET","POST"])
def resultado():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        rest = request.form.get("operaciones")
        print(rest)
        if rest == "suma":
            return "<h1> La suma es: {} </h1>".format(str(int(num1)+int(num2)))
        elif rest == "resta":
            return "<h1> La resta es: {} </h1>".format(str(int(num1)-int(num2)))
        elif rest == "multiplicacion":
            return "<h1> La multiplicación es: {} </h1>".format(str(int(num1)*int(num2)))
        else: 
            return "<h1> La divición es: {} </h1>".format(str(int(num1)/int(num2)))
    

if __name__== "__main__":
    app.run(debug=True)