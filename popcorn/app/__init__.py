from flask import Flask
import psycopg2

app = Flask(__name__) #guarda el servidor en esta variable y se asegura que se ejecute el init
#app.config.from_object('config.Config')#Indica al servidor que se configure desde su propia libreria

from .views import main as main_blueprint
app.register_blueprint(main_blueprint)

#Creará la aplicación devuelve la variable creada anteriormente retorna todo el servidor
def create_app():
   return app