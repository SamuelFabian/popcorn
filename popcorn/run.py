from app import create_app #importamos el metodo desde __init__

#almacena el servidor en la variable app
app = create_app()

#corre el servidor, debug indica que está en modo de desarrollo
app.run(debug=True, port=5050)