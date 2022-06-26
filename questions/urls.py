from unicodedata import name
from django.urls import path
from .views import *


app_name = "questions"

urlpatterns = [
    path("", ResultListView.as_view(), name="results_user_question"),
    path("question/", add_user_question, name="add_user_question"),
    path("result/<int:pk>/", ResultDetailView.as_view(), name="result_user_question"),
]
