from django.urls import path
from . import views
app_name = "todo"

urlpatterns = [

    path('todo-list/', views.TodoListView.as_view(), name="todo-list"),
    path('add-project/', views.AddTodoView.as_view(), name="add-project"),
    path('update-project/', views.UpdateTodoView.as_view(), name="update-project"),
    path('edit-todo/<int:pk>', views.EditTodoView.as_view(), name="edit-todo"),
    path('delete-todo/<int:pk>', views.DeleteTodoView.as_view(), name="delete-todo"),


]