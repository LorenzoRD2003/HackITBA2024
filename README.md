# HackItba 2024

### [Como ejecutar](#como-ejecutar)
----------
## CIFU: Mantené tu cerebro activo
CIFU (Cuidado Integral para el Fortalecimiento Unificado de la Mente)

CIFU es una aplicación web diseñada para brindar ejercicios cognitivos y seguimiento de logros, con el objetivo de promover la salud cerebral y poder darle un acompañamiento interactivo a ciertas personas afectadas por complicaciones en relación al cerebro.

### Características principales
* Ejercicios personalizados: Cada usuario recibe ejercicios adaptados a su nivel y necesidades específicas.
* Seguimiento de progreso: Mantén un registro de tu desempeño y avances a lo largo del tiempo.

### Próximos pasos
- Implentar API de OpenAI (ya está el código, falta utilizar una llave válida).
- Aplicar a más tipos de condiciones, principalmente Alzheimer.
----------
## Cómo ejecutar
Se recomienda crear un entorno virtual de python antes de comenzar. Existen varios métodos, siendo el más común
[venv](https://docs.python.org/3/library/venv.html).

La manera más sencilla es clonar el repositorio y ejecutar `install_and_run.sh` (`.ps1` en Windows) y listo.
(En linux es necesario hacer `chmod +x ./install_and_run.sh` para poder ejecutar el script).

Para un paso a paso manual más detallado, seguimos las instrucciones a continuación.

El proyecto está pensado para ser ejecutado en Linux, pero no hay problema en utilizar Windows, teniendo en
cuenta que existe la posibilidad de tener que usar:
- `python` en vez de `python3`
- `python -m pip ...` en vez de `pip ...`

Pasos a seguir:
1. Clonar repositorio (ejemplo: `git clone https://github.com/LorenzoRD2003/HackITBA2024.git`)
2. Instalar requerimientos de pip: `pip install -r requirements.txt` (ya dentro de la carpeta `HackITBA2024`).
3. Entrar al directorio `cd hackitba_2024`.
4. Recopilar migraciones de las aplicaciones: `python3 manage.py makemigrations`
5. Aplicar migraciones a la base de datos: `python3 manage.py migrate`
6. Poblar la base de datos: `python3 manage.py shell < populate_db.py` (`echo 'import populate_db' | python manage.py shell` en Windows)
7. Correr el servidor web (local): `python3 manage.py runserver`.
(Cada vez que quiero correr el servidor local, utilizo `manage.py runserver`)

El servidor local escucha en la dirección `127.0.0.1:8000` (`localhost:8000`).
Para dejar de ejecutar, utilizamos `Ctrl + C`.
Django nos permite ver cambios en el código de manera instantánea, por lo que no hace falta reiniciar el servidor si se modifican los archivos del proyecto (a excepción de los archivos en `models.py`, que afectan la base de datos).
