# 📊 Gestor de Gastos Personales

Aplicación web para la gestión y control de gastos personales, permitiendo a los usuarios registrar gastos, categorizar, establecer presupuestos y realizar seguimiento de sus finanzas.

## 🚀 Tecnologías usadas

- **Backend:** Django 5.2 (Python)
- **Frontend:** HTML5, CSS3, JavaScript
- **Base de Datos:** PostgreSQL
- **Otros:** Django Admin, PlantUML (para diagramas)

## 🎯 Funcionalidades principales

- Registro y autenticación de usuarios.
- Creación y gestión de categorías de gasto.
- Registro de gastos con monto, fecha, descripción y categoría.
- Creación de presupuestos personalizados por usuario.
- Visualización de gastos recientes y categorizados.
- Validaciones para evitar exceder presupuestos (próximamente).
- Gráficos e informes de gastos (próximamente).

## 🛠️ Instalación y ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/gestor-gastos.git
cd gestor-gastos
``` 
### 2. Crear un entorno virtual
```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows

``` 
### 3. Instalar dependencias 
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos
- ** Crear una base de datos PostgreSQL.
- ** Configurar las credenciales
```bash
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

```
### 5. Aplicar migraciones 
```bash
python manage.py makemigrations
python manage.py migrate

```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```
- Te va a solicitar crear credenciales.

### 7. Correr el servidor

```bash
python manage.py runserver
```

Accede a http://127.0.0.1:8000/ para usar la aplicación.
