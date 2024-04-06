from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', RedirectView.as_view(url='login/')),  # Redirect root URL to login URL
    path('login/', include('user_auth.urls')),
    path('app/', include('exercises.urls'))
]