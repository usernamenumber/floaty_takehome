from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.urls import reverse_lazy
from .models import Question

class QuestionListView(ListView):
    model = Question

class QuestionHistoryView(DetailView):
    model = Question

class QuestionCreateView(CreateView):
    model = Question
    fields = ['text']
    success_url = reverse_lazy('chatbot:question_list')

class QuestionUpdateView(UpdateView):
    model = Question
    fields = ['text']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('chatbot:question_list')
