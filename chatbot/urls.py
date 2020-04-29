from django.urls import path
from . import views

app_name = 'chatbot'
urlpatterns = [
    path('', views.QuestionListView.as_view(), name="question_list"),
    path('create', views.QuestionCreateView.as_view(), name="question_create"),
    path('<int:pk>/history', views.QuestionHistoryView.as_view(), name="question_history"),
    path('<int:pk>/update', views.QuestionUpdateView.as_view(), name="question_update"),
]