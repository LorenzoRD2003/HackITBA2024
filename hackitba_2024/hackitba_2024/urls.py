from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', include('user_auth.urls')),
    path('home/', include('exercises.urls'))
]