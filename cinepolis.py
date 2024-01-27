from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/cinepolis",  methods=["GET", "POST"])
def cine():
    return render_template("cinepolis.html")

@app.route("/ventaBoletos", methods=["GET", "POST"])
def venta():
    if request.method == "POST":
        nombre = request.form.get("nom")
        cantidad = int(request.form.get("cant"))
        tajeta = request.form.get("tarjeta")
        numBoletos = int(request.form.get("boletos"))
        mensaje = "No se puede comprar más de 7 boletos por persona"
        boletoPersona = cantidad * 7
        b = 0

        montoPagar = 12.00 * int(numBoletos)
        

        if int(numBoletos) > int(boletoPersona):
            return render_template("cinepolis.html", mensaje = mensaje)
        else: 
        
            if int(numBoletos) > 5:
                pagar = montoPagar - (float(montoPagar) * .15)               
            
            elif int(numBoletos) >= 3 or int(numBoletos) <= 5:                
                pagar = montoPagar - (float(montoPagar) * .10)                

            else:
                pagar = montoPagar
                
            
            if tajeta == "si":
                descuentot = pagar * .10
                pagar2 = pagar - descuentot
                return render_template("cinepolis.html", pagar2 = pagar2)
            
            elif tajeta == "no":
                pagar2 = pagar 
                return render_template("cinepolis.html", pagar2 = pagar2)
            

        


        
        

if __name__ == "__main__":
    app.run(debug=True)
