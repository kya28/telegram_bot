from django.contrib import admin
from django.urls import path
from words import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('random/', views.RandomWord.as_view()),
    path('next/<int:pk>', views.NextWord.as_view()),
]
