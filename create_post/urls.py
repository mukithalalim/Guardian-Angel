from django.urls import path, include

from post import views

urlpatterns = [
    path('emergency-posts/', views.EmergencyPostsList.as_view()),
]
