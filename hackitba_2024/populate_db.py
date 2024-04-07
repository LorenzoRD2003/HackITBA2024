from exercises.utils import create_achievement, create_exercise
from exercises.models import VALID_DIFFICULTIES

create_achievement("100 días de racha", 100, 'streak')
create_achievement("50 días de racha", 50, 'streak')
create_achievement("25 días de racha", 25, 'streak')
create_achievement("10 días de racha", 10, 'streak')
create_achievement("50 ejercicios fáciles", 50, 'exer_amount')
create_achievement("20 ejercicios intermedios", 20, 'exer_amount')
create_achievement("10 ejercicios difíciles", 10, 'exer_amount')
create_achievement("5 logros obtenidos", 5, 'achiv_amount')

create_exercise('Palabras', 'descripcion', VALID_DIFFICULTIES[1], "ex1", 'img/words.jpeg')
create_exercise('Palabras con imágenes', 'descripcion', VALID_DIFFICULTIES[1], "ex2", 'img/image_words.jpeg')
create_exercise('Palabras con espacios', 'descripcion', VALID_DIFFICULTIES[1], "ex3", 'img/text_spaces.jpeg')
create_exercise('Lectura con API', 'descripcion', VALID_DIFFICULTIES[1], "ex4", 'img/api_reading.jpeg')