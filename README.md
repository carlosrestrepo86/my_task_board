# Proyecto API con FastAPI + SQLModel

### API REST construida con FastAPI, SQLModel y Pydantic, que permite:

* Registro y autenticación de usuarios (JWT).
* Creación y gestión de tareas.
* Creación y gestión de etiquetas.
* Asociación de tareas con etiquetas.

### 📂 Estructura del proyecto
```
my_task_board/
├── app/
│   ├── __init__.py
│   ├── api/                  # Endpoints relacionados con usuarios, autenticación, tareas y etiquetas.
│   │   ├── auth.py         
│   │   ├── tags.py         
│   │   ├── tasks.py         
│   │   └── users.py          
│   ├── core/                 # Seguridad, dependencias y utilidades.
│   │   ├── dependencies.py    
│   │   ├── security.py   
│   ├── CRUD/                 # Métodos relacionados a usuarios, autenticación, tareas y etiquetas.
│   │   ├── auth.py         
│   │   ├── tags.py         
│   │   ├── tasks.py         
│   │   └── users.py   
│   ├── db/                   
│   │   ├── db.py             # Configuración de la base de datos.
│   ├── models/               # Modelos para SQLAlchemy.
│   │   ├── link_table.py         
│   │   ├── tags.py         
│   │   ├── tasks.py         
│   │   └── users.py
│   ├── schemas/              # Modelos para Pydantic (input/output).       
│   │   ├── tags.py         
│   │   ├── tasks.py         
│   │   └── users.py
│   ├── config.py             # Configuración (DB, JWT, etc.).
│   ├── filters.py            # Metodo para filtrar datos desde la base de datos.    
│   ├── main.py               # Entrada de la aplicación.
├── requirements.txt          # Dependencias.
└── README.md                 # Este archivo.
```
### ⚙️ Requisitos

* Python 3.13.7
* FastAPI
* SQLModel
* Pydantic
* PyJWT
* SQLite

### 📦 Instalar SQLite

1. Descargar desde:<br>
SQLite → https://sqlite.org/download.html

2. Realizar instalación.

### 🔧 Configuración del entorno
1. Crear entorno virtual:
```
python3 -m venv .venv    # Linux/Mac
python -m venv .venv     # Windows
```
2. Activar entorno virtual:
```
source .venv/bin/activate    # Linux/Mac
.venv\Scripts\Activate       # Windows
```
3. Instalar dependencias
```
pip install -r requirements.txt
```

### 🔹 Paso 1. Crear archivo ```.env``` en la raíz del proyecto
```
# .env

SECRET_KEY = "llave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 5
```

### ▶️ Ejecución

Ejecutar el servidor en modo desarrollo:
```
fastapi dev .\app\main.py
```
Accede a la documentación interactiva:<br>
Swagger UI → http://127.0.0.1:8000/docs

### 🔑 Autenticación

El sistema usa JWT para proteger endpoints.
1. Registrar un usuario:
```
POST /users
```
2. Iniciar sesión (obtener token) mediante el botón ```Authorize``` o el candado del endpoint requerido.

### 📌 Endpoints principales

Usuarios

```POST /users → Registrar usuario```<br>
```GET /users → Listar usuarios```<br>
```GET /users/{id} → Obtener usuario por ID```

Etiquetas

```POST /tags → Crear etiqueta```<br>
```GET /tags → Listar etiquetas```<br>
```PATCH /tags/{id} → Actualizar etiqueta```<br>
```DELETE /tags/{id} → Eliminar etiqueta```

Tareas

```POST /tasks → Crear tarea```<br>
```GET /tasks → Listar tareas (con filtros opcionales)```<br>
```PATCH /tasks/{id} → Actualizar tarea```<br>
```DELETE /tasks/{id} → Eliminar tarea```<br>
```POST /tasks/{id}/add-tag/{tag_id} → Asociar etiqueta a tarea``` <br>
```DELETE /tasks/{id}/add-tag/{tag_id} → Eliminar etiqueta a tarea```

Autenticación

```POST /auth/login → Login con JWT```