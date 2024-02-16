# Django Metalnor Project

Proyecto base de Django diseñado específicamente para migrar cada modulo de metalnor. Con una estructura escalable y preparado para ser utilizado con una base de datos PostgreSQL.

## Pasos de instalación

### 1. Crear un entorno virtual

Utilizamos `venv` para manejar entornos virtuales. Para crear un nuevo entorno virtual llamado `venv-metalnor`, ejecuta:

````
python -m venv venv-metalnor
````


Activar el entorno virtual:

- **Linux o Mac**:

source venv-metalnor/bin/activate

- **Windows**:

cd venv-metalnor

cd Scripts

```./activate```

(Windows) En caso de no poder realizarlo porque la ejecucion de scripts esta deshabilitada en este sistema. Usar
el comando
```Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser```

### 2. Instalación de dependencias

Una vez dentro del entorno virtual, navega hasta la raíz del proyecto y ejecuta:

pip install -r requirements.txt


### 3. Configuración de credenciales

Dentro de la raíz del proyecto, crea un archivo llamado `secret.json` con la siguiente estructura:

```json
{
    "FILENAME": "secret.json",
    "SECRET_KEY": "clave_secreta_pedir_administrador_del_sistema",
    "DB_NAME": "db_metalnor",
    "DB_USER": "postgres",
    "DB_PASSWORD": "password",
    "DB_HOST": "localhost",
    "DB_PORT": 5432,

    "EMAIL_HOST":"smtp.gmail.com",
    "EMAIL_HOST_USER":"metalnor.ejemplo@gmail.com",
    "EMAIL_HOST_PASSWORD":" <<password>>"
}
```
Nota: Asegúrate de cambiar los valores de SECRET_KEY, DB_NAME, DB_USER y DB_PASSWORD a los apropiados para tu configuración.

### 4. Configuración de la base de datos

Dado que utilizamos PostgreSQL como base de datos, asegúrate de tenerlo instalado y en ejecución.

### 5. Variable de entorno
al ejecutar la aplicación o al configurar tu entorno virtual. Puedes hacerlo directamente en la terminal antes de ejecutar tu aplicación.

**En sistemas basados en Unix/Linux/Mac**

```export DEVELOPMENT_ENVIRONMENT=True```

**En Windows (CMD)**

```set DEVELOPMENT_ENVIRONMENT=True```

**En Windows (Powershell)**
```$env:DEVELOPMENT_ENVIRONMENT="True"```
```echo $env:DEVELOPMENT_ENVIRONMENT```

### 6. Crear y aplicar migraciones

Para crear las migraciones y aplicarlas, ejecuta:

python manage.py makemigrations
python manage.py migrate

### 7. Ejecutar el proyecto

```python manage.py runserver```

¡Listo! Ahora puedes acceder a tu proyecto Django desde http://localhost:8000/.