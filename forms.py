from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField, IntegerField

class UserForm(Form):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')
    
#bandas = [{'nombre1', 'Nombre 1'}, {'nombre2', 'Nombre 2'}, {'nombre3', 'Nombre 3'}]
    bandas = [('0', 'Negro',), ('1', 'Cafe'), ('2', 'Rojo'), ('3', 'Naranja'), ('4', 'Amarillo'),
        ('5', 'Verde'), ('6', 'Azul'), ('7', 'Violeta'), ('8', 'Gris'), ('9', 'Blanco')       ]
    
    bandast = [('1', 'Negro'), ('10', 'Cafe'), ('100', 'Rojo'), ('1000', 'Naranja'), ('10000', 'Amarillo'),
        ('100000', 'Verde'), ('1000000', 'Azul'), ('10000000', 'Violeta'), ('100000000', 'Gris'), ('1000000000', 'Blanco')]
    
    tolerancias = [('.05', 'Oro'), ('.10', 'Plata')]
    banda1 = SelectField('banda1', choices=bandas)
    banda2 = SelectField('banda2', choices=bandas)
    banda3 = SelectField('banda3', choices=bandast)
    tolerancia = RadioField('tolerancia', choices=tolerancias)

    