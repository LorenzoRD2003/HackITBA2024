from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('user_auth.urls')),
    path('home/', include('exercises.urls'))
]