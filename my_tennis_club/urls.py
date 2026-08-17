from django.contrib import admin
from django.urls import include, path
from members import views

urlpatterns = [
    path('', views.main, name='main'),
    path('admin/', admin.site.urls),
    path('members/', include('members.urls')),
]