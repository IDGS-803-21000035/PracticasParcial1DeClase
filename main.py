from flask import Flask, render_template, request
import forms
from math import sqrt
from io import open

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

#decorador para formulario1
@app.route("/operaciones")
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
    
def color(valor):
    colores = {
        '0': '#000000',  
        '1': '#99581A',  
        '2': '#FF0000',  
        '3': '#F37E11',  
        '4': '#FFFF00',  
        '5': '#3192CF',  
        '6': '#0000FF',  
        '7': '#8A2BE2',  
        '8': '#808080',  
        '9': '#FFFFFF'   
    }
    return colores.get(valor, '#000000')  

@app.route("/resistencia",  methods=["GET", "POST"])
def resistencia():
    dist_form = forms.UserForm(request.form)
    r = 0  
    rmax = 0
    rmin = 0
    band1 = []
    band2 = []
    band3 = []
    to = ""
    colort = ""

    if request.method == 'POST':
        banda1 = dist_form.banda1.data
        banda2 = dist_form.banda2.data
        banda3 = dist_form.banda3.data
        tolerancia = dist_form.tolerancia.data

        band1 = dist_form.banda1.choices[int(banda1)]
        band2 = dist_form.banda2.choices[int(banda2)]
        
        band3 = dist_form.banda3.choices[int(banda3)-1]
        print('GFKishihu', band3)
        print("Número de rango seleccionado en banda3:", banda3)

        num = int(banda1 + banda2) * int(banda3)  
        t = num * float(tolerancia)

        r = num
        rmax = num + t
        rmin = num - t

        if tolerancia == '.05':
            to = 'Dorado 5%'
            colort = '#CFB53B'
        elif tolerancia == '.10':
            to = "Plata 10%"
            colort = '#BEBEBE'

    return render_template("resistencias.html", forms=dist_form, r=r, rmax=rmax, rmin=rmin, band1=band1, band2=band2, band3=band3, to=to, color=color, colort=colort)


@app.route("/diccionario",  methods=["GET", "POST"])
def diccionario():
    dicc_form = forms.DiccForm(request.form)
    busc_form = forms.BuscForm(request.form)
    ingles = ""
    espaniol = ""
    buscar = ""
    res = ""
    mensaje = ""
    
    if request.method == 'POST':
        

        if 'btnGuardar' in request.form and dicc_form.validate():
            ingles = dicc_form.ingles.data
            espaniol = dicc_form.espaniol.data

            archivo_dicc = open('diccionario.txt', 'a')
            archivo_dicc.write("\n"+ingles+": "+espaniol)
            archivo_dicc.close()
            mensaje = "Palabra registrada"

            

            return render_template("diccionarioEsIn.html", dicc_form=dicc_form, busc_form=busc_form, mensaje = mensaje)
        
        elif 'btnBuscar' in  request.form and busc_form.validate():
            buscar = busc_form.buscar.data
            idioma = busc_form.idioma.data

            if idioma == '1':
                res = traducir(buscar.upper(), idioma)
            else:
                res = traducir(buscar.upper(), idioma)

                


    return render_template("diccionarioEsIn.html", dicc_form=dicc_form, busc_form=busc_form, res=res)


def traducir(palabra, idioma):
    archivo_dicc = open('diccionario.txt', 'r')
    #archivo_dicc.seek(0)
    archivo_dicc.readline() 
    for line in archivo_dicc:
        ing, esp = line.split(':')
        ing = ing.strip().upper()
        esp = esp.strip().upper() #Stip() elimina los espacios --- palabra ---
        if idioma == '1':
            if ing == palabra:
                archivo_dicc.close()
                return esp
        else:
            if esp == palabra:
                archivo_dicc.close()
                return ing
    archivo_dicc.close()
    return "no se encuentra esta palabra"


if __name__ == "__main__":
    app.run(debug=True)
