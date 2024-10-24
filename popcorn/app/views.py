from flask import Blueprint, render_template, request, redirect, url_for, session, flash #Indica al servidor como va a trabajar
#render template indiica que se va a cargar el archivo HTML
#request es usado para obtener los datos de form del archivo html
#from .methods import *

main =Blueprint('main', __name__) #Almacena el plano de trabajo
#main es el nombre del plano de trabajo (podemos tener varios)
#__name__ indica que el plano de trabajo tome el nombre 'main' 

@main.route('/') #Cuando el usuario entre a la ruta raíz se va a ejecutar el plano llamado main
def home():
    return render_template('index.html') #muestra el archivo html de la pagina web
