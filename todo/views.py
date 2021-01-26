from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView
from .models import Todo
# Create your views here.

@login_required
def home(request):
    user = request.user
    activities = Todo.objects.filter(created_by=user)

    context = {
        'activities' : activities
    }

    return render(request, 'todo/home.html', context=context)

def home_high(request):
    user = request.user
    activities = Todo.objects.filter(created_by=user)
    high_activities = activities.filter(priority='h')
    context = {
        'activities' : high_activities
    }

    return render(request, 'todo/home.html', context=context)

def home_medium(request):
    user = request.user
    activities = Todo.objects.filter(created_by=user)
    medium_activities = activities.filter(priority='m')
    context = {
        'activities' : medium_activities
    }

    return render(request, 'todo/home.html', context=context)

def home_low(request):
    user = request.user
    activities = Todo.objects.filter(created_by=user)
    low_activities = activities.filter(priority='l')
    context = {
        'activities' : low_activities
    }

    return render(request, 'todo/home.html', context=context)



class TodoListView(ListView):
    model = Todo
    context_object_name = 'activities'
    template_name = "todo/home.html"

class TodoDetailView(DetailView):
    model = Todo


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'todo/about.html')

def delete_activity(request, pk):
    Todo.objects.filter(id=pk).delete()
    activities = Todo.objects.all()

    context = {
        'activities' : activities
    }
    return render(request, 'todo/home.html', context=context)

class TodoCreateView(LoginRequiredMixin, CreateView):
    model = Todo
    fields = ['activity', 'priority']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
