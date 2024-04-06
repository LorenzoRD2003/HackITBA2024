import json
import random
import math
from time import sleep
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

from .models import *

class InfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'info.html')


class ExerciseView(LoginRequiredMixin, View):
    def get(self, request):
        all_exercises = Exercise.objects.all()
        exercise_list = []

        context = {'exercise_list': exercise_list}
        return render(request, 'exercises.html', context)

class AchievementView(LoginRequiredMixin, View):
    def get(self, request):
        all_achievements = Achievement.objects.all()

        return render(request, 'achievements.html')
    
class OpenAIView(LoginRequiredMixin, View):
    def post(self, request):
        message = json.loads(request.body)['message']

        if 'api_used' in request.session:
            ai_response = "IMPLENTACION A FUTURO: Integrar API de OpenAI"
            return JsonResponse({'response': ai_response})

        sleep(2)

        ai_responses = ["La dislexia es un trastorno que afecta la capacidad de leer y escribir con fluidez. Las personas con dislexia suelen tener dificultades para reconocer palabras, especialmente en textos largos o complejos. El apoyo y la comprensión son fundamentales para quienes viven con esta condición. ¿Qué más te gustaría saber al respecto?",
                        "La dislexia es una condición que afecta la forma en que el cerebro procesa el lenguaje escrito, lo que puede dificultar la lectura, la escritura y la ortografía para algunas personas. Con el apoyo adecuado y estrategias específicas, las personas con dislexia pueden aprender a manejar sus desafíos y tener éxito académico y personal. ¿Hay algo más específico que te interese sobre este tema?",
                        "La dislexia es un trastorno del aprendizaje que afecta la lectura, la escritura y la ortografía. Las personas con dislexia pueden tener dificultades para reconocer palabras, recordar la secuencia de letras o comprender el significado de lo que leen. Es importante ofrecerles apoyo individualizado y herramientas adaptativas para ayudarles a superar estos desafíos y alcanzar su máximo potencial. ¿Hay algo más que te gustaría saber sobre la dislexia?",
"El Alzheimer es una enfermedad neurodegenerativa que afecta la memoria, el pensamiento y el comportamiento de las personas. A medida que avanza, puede dificultar las tareas cotidianas y la comunicación. Es fundamental brindar cuidados compasivos y adaptar el entorno para apoyar a quienes viven con esta enfermedad. ¿Te interesa saber más detalles sobre el Alzheimer y cómo se maneja?",
                                  "El Alzheimer es una enfermedad progresiva que afecta la memoria, el pensamiento y la capacidad de realizar actividades diarias. Las personas con Alzheimer pueden experimentar dificultades para recordar información reciente, reconocer rostros familiares o tomar decisiones. El apoyo emocional, la estimulación cognitiva y la atención médica especializada son clave para mejorar su calidad de vida. ¿Quieres saber más sobre cómo se diagnostica y trata el Alzheimer?",
                                  "El Alzheimer es una enfermedad neurodegenerativa que afecta principalmente a la memoria y otras funciones cognitivas. Con el tiempo, puede causar dificultades en la comunicación, la toma de decisiones y el manejo de actividades diarias. Es importante ofrecer un ambiente seguro y comprensivo a las personas con Alzheimer, así como brindar apoyo a sus cuidadores y familiares. ¿Te gustaría saber más acerca de los síntomas y el cuidado del Alzheimer?"]

        request.session['api_used'] = True

        ai_response = ai_responses[math.ceil(random.random() * 5)]
        return JsonResponse({'response': ai_response})
