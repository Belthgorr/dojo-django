from django.urls import path
from decaToRoma import views

urlpatterns = [
    path('convert/<int:number>', views.decToRoma.as_view()),
]