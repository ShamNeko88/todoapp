from django.views.generic.list import ListView

from todoapp.models import Task


# Create your views here.
class TaskList(ListView):
    model = Task
