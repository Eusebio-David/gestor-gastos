# 📊 Gestor de Gastos Personales

Aplicación web para la gestión y control de gastos personales. Permite a los usuarios registrar sus gastos, categorizarlos, definir presupuestos personalizados y hacer un seguimiento visual de sus finanzas.

---

## 🚀 Tecnologías utilizadas

- **Backend:** Django 5.2 (Python)
- **Frontend:** HTML5, CSS3, JavaScript, Tailwind CSS
- **Base de Datos:** PostgreSQL
- **Otros:** Django Admin, Django Messages Framework, PlantUML (para diagramas), Django Authentication

---

## 🎯 Funcionalidades principales

- ✅ Registro y autenticación de usuarios
- ✅ CRUD de categorías de gasto
- ✅ Registro de gastos con monto, fecha, descripción y categoría
- ✅ Listado de gastos categorizados y recientes
- ✅ Mensajes de éxito al crear, modificar o eliminar gastos
- 🚧 CRUD para presupuesto (en desarrollo)
- 🚧 Validación contra presupuesto (en desarrollo)
- 🚧 Gráficos e informes interactivos (en desarrollo)
- 🚧 Presupuestos mensuales personalizados por usuario (en desarrollo)

---

## 🛠️ Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/gestor-gastos.git
cd gestor-gastos 
````
## 📦 Crear un entorno virtual

Es recomendable trabajar en un entorno virtual para mantener tus dependencias organizadas.

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
````
## 📥 Instalar dependencias

Asegurate de tener el archivo `requirements.txt` en la raíz del proyecto.

```bash
pip install -r requirements.txt
````
## 🧩 Configuración de base de datos

1. Crear una base de datos PostgreSQL en tu sistema.
2. Configurar la conexión en tu archivo `settings.py` de Django:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_base',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
````
O podes dejar la base de datos por defecto que usa Django, en este caso es SQLite
## 🔧 Aplicar migraciones

Aplica las migraciones de Django para crear las tablas en tu base de datos:

```bash
python manage.py makemigrations
python manage.py migrate
````
## 👤 Crear superusuario

Para acceder al panel de administración de Django, necesitás un superusuario:

```bash
python manage.py createsuperuser
````
## 🎨 Configuración de Tailwind CSS

Usamos [Tailwind CSS](https://tailwindcss.com/) como framework de estilos.

### 1. Instalar Tailwind y herramientas

```bash
npm init -y
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p

````
## 🚀 Correr el servidor
Iniciá el servidor de desarrollo de Django con:

```bash
python manage.py runserver
````
## 🚧 Queda en proceso de desarrollo:
- Configurar templates y formularios para restablecer contraseaña
- Cambiar campos y agregar en la base de datos
- Hacer el código más limpio y legible
- Darle funcionalidad a todos los links que no se utilizan
- Adaptar todos los templates para que queden acordes a la app
