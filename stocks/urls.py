from django.contrib import admin
from django.urls import path

from stocks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('rooms/<int:room_id>/', views.room_detail, name='room_detail'),
]
