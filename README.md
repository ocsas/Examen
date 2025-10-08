1. ¿Para qué se puede usar Python en lo que respecta a datos?

Python se puede usar para casi todo lo relacionado con el trabajo con datos. Permite analizar, limpiar, transformar y visualizar información de manera sencilla.
Con librerías como pandas y numpy se pueden hacer análisis complejos; con matplotlib y seaborn se crean gráficos y reportes visuales; y con scikit-learn o TensorFlow se desarrollan modelos predictivos y de machine learning.
También se usa para automatizar tareas, mover datos entre sistemas (ETL) y generar reportes automáticos. En resumen, Python permite convertir datos en información útil de forma rápida y flexible.

2. ¿Cómo se diferencian Flask de Django?

La diferencia principal está en su enfoque:

Flask es un microframework liviano y flexible. Se usa para crear APIs o servicios pequeños y ofrece libertad para decidir la estructura del proyecto y las librerías que se integran.

Django es un framework completo que ya trae muchas funciones incluidas como autenticación, panel de administración, ORM y plantillas. Es ideal para proyectos grandes y complejos.

En resumen: Flask ofrece más libertad y simplicidad, mientras que Django ofrece estructura y rapidez de desarrollo para aplicaciones completas.

3. ¿Qué es un API?

Un API (Application Programming Interface) es una interfaz que permite que diferentes aplicaciones se comuniquen entre sí sin necesidad de acceder directamente al código del otro sistema.
Funciona como un “puente” que recibe solicitudes (por ejemplo, datos o acciones) y devuelve respuestas. Gracias a los APIs, distintas plataformas pueden conectarse y compartir información de manera segura y estandarizada.

4. ¿Cuál es la principal diferencia entre REST y WebSockets?

La diferencia está en la forma en que se comunica el cliente con el servidor:

REST trabaja con solicitudes independientes: el cliente envía un request y el servidor responde. Se usa principalmente para operaciones CRUD (crear, leer, actualizar y eliminar).

WebSockets mantiene una conexión abierta entre cliente y servidor, lo que permite intercambiar información en tiempo real sin tener que enviar solicitudes nuevas.
Es ideal para chats, juegos en línea o dashboards que actualizan datos constantemente.

5. Ejemplo de un API comercial y cómo funciona

Un ejemplo es la API de Spotify. Permite acceder a datos de canciones, artistas y listas de reproducción.
Por ejemplo, un desarrollador puede usar la API para mostrar las canciones más escuchadas o crear playlists automáticas.
Para hacerlo, se obtiene una clave (token) y se realizan peticiones a endpoints como /v1/tracks o /v1/artists.
La API responde en formato JSON con la información solicitada, sin que el usuario tenga que entrar directamente a la plataforma de Spotify.

Código alojado en GitHub:

https://github.com/ocsas/Examen

# API Estudiantes (Flask)

API desarrollada con **Flask** y **SQLite** para gestionar estudiantes (crear, listar, actualizar y eliminar registros).

---

## Setup

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python estudiante.py
python main.py
