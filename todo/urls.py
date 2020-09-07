from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('AddTask/',views.AddTask, name= 'add task'),
    path('Done/<int:text_id>',views.task_done, name = 'task done'),
    path('DeleteDone/',views.delete_done,name= 'delete done'),
    path('DeleteAll/',views.delete_all,name= 'delete all'),
]