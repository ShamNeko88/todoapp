from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import(
    CreateView, UpdateView, DeleteView, FormView
)
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# ログインしていないとアクセスさせないやつ
from django.contrib.auth.mixins import LoginRequiredMixin

from todoapp.models import Task


# Create your views here.
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    # オブジェクト名の定義
    context_object_name = "tasks"

    # ユーザーに紐づいたリストを表示させる
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # ログインユーザーでフィルタリング
        context["tasks"] = context["tasks"].filter(user=self.request.user)
        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = "task"


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "completed"]
    success_url = reverse_lazy("tasks")

    # タスク追加時にログインユーザーを指定
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "completed"]
    template_name_suffix = "_update_form"
    success_url = reverse_lazy("tasks")


class TaskDelete(LoginRequiredMixin, DeleteView):
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


# ユーザー登録
class RegisterTodoApp(FormView):
    template_name = "todoapp/register.html"
    form_class = UserCreationForm
    success_url = reverse_lazy("tasks")

    # ユーザー登録成功で保存してルートページに移動
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)
