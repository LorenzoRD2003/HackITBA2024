# HackItba 2024

### [Como ejecutar](#como-ejecutar)
----------
## CIFUMIND: Mantené tu cerebro activo
CIFUMIND (Cuidado Integral para el Fortalecimiento Unificado de la Mente)

CIFUMIND es una aplicación web diseñada para brindar ejercicios cognitivos y seguimiento de logros, orientado para personas mayores, con el objetivo de promover la salud cerebral y prevenir enfermedades neurodegenerativas como el Alzheimer. Nuestra plataforma ofrece una variedad de actividades estudiadas por expertos en neurociencia y salud mental, adaptadas específicamente para mejorar la memoria, la concentración y otras habilidades cognitivas.

### Características principales
* Ejercicios personalizados: Cada usuario recibe ejercicios adaptados a su nivel y necesidades específicas.
* Seguimiento de progreso: Mantén un registro de tu desempeño y avances a lo largo del tiempo.

----------

### Próximos pasos
TODO
----------
## Como ejecutar
El proyecto está pensado para ser ejecutado en Linux, pero no hay problema en utilizar Windows, teniendo en
cuenta que existe la posibilidad de tener que usar:
- `python` en vez de `python3`
- `python -m pip ...` en vez de `pip ...`

Pasos a seguir:
1. Clonar repositorio (ejemplo: `git clone https://github.com/LorenzoRD2003/HackITBA2024.git`)
2. Instalar requerimientos de pip: `pip install -r requirements.txt` (ya dentro de la carpeta `HackITBA2024`).
3. Popular la base de datos: `python3 populate_db.py` (Idealmente se ejecuta una única vez).
4. Correr el servidor web (local): `python3 hackitba_2024/manage.py runserver`.
(Cada vez que quiero correr el servidor local, utilizo `manage.py runserver`)