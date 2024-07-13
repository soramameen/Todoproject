#from django.shortcuts import render
#from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import TodoModel
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.urls import reverse_lazy
def sampleappview(request):
    return HttpResponse('hello')
class ListClass(ListView):
    template_name = 'list.html'
    model = TodoModel
class DetailClass(DetailView):
    model = TodoModel
    template_name='detail.html'
class CreateClass(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title','memo','priority','duedate')
    success_url = reverse_lazy('list')
class DeleteClass(DeleteView):
    template_name ='delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')
class UpdateClass(UpdateView):
    model = TodoModel
    template_name = "update.html"
    success_url = reverse_lazy('list')
    fields =('title','memo','priority','duedate')
