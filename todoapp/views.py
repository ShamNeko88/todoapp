from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# ログインしていないとアクセスできない
from django.contrib.auth.mixins import LoginRequiredMixin

from todoapp.models import Task


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # オブジェクト名の定義
    context_object_name = "tasks"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("tasks")


class TaskDelete(DeleteView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
    context_object_name = "tasks"


class TaskListLoginView(LoginView):
    fields = "__all__"
    # デフォルトではregistration/login.htmlなので変更
    template_name = "todoapp/login.html"

    def get_success_url(self):
        return reverse_lazy("tasks")

