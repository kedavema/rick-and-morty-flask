# Aplicación Web con Flask utilizando la API de Rick and Morty y bases de datos.

## **Tecnologías:**
- Flask
- SQLAlchemy
- SQLite3
- TailwindCSS

## Intrucciones

### Para correr la aplicación primero debemos crear nuestro entorno virtual:
> En sistemas basados en UNX
```
python3 -m venv venv
```
> En windows
```
py -m venv venv
```
### Ahora activamos nuestro entorno:
> En sistemas basados en UNIX
```
source venv/bin/activate
```
> En Windows
```
.\venv\Scripts\activate
```
### Instalamos las dependencias
> UNIX:
```
pip install -r requirements.txt
```
> Windows:
```
py -m pip install -r requirements.txt
```

### Creamos una carpeta llamada database y dentro creamos una base de datos con sqlite3(desde la terminal)
```
sqlite3 database.db
```

### Entramos en la shell de python desde la carpeta principal(donde está nuestro app.py) y ejecutamos los sigtes comandos:
> En UNIX:
```
python3
```
> Windows:
```
py
```
### Luego desde la shell creamos la tabla Personaje en la base de datos
```
from app import db
db.create_all()
```
### Para salir de la shell de python ejecutamos
```
exit()
```
### Por úiltimo ejecutamos el programa
```
flask run
```
