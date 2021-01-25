from django.urls import path
from . import views
from .views import TodoDetailView, TodoCreateView


urlpatterns = [
    path('', views.home, name='todo-home'),
    path('high/', views.home_high, name='todo-home-high'),
    path('medium/', views.home_medium, name='todo-home-medium'),
    path('low/', views.home_low, name='todo-home-low'),
    path('about/', views.about, name='about'),
    path('todo/<int:pk>/', TodoDetailView.as_view(), name="todo-detail"),
    path('todo/delete/<int:pk>', views.delete_activity, name="todo-delete"),
    path('todo/new/', TodoCreateView.as_view(), name='todo-create'),
    #path('todo/new/', TodoCreateView.as_view(), name="todo-create") Create a TodoCreateView for this and make page for it.
]