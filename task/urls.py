from django.urls import path
from .import views

urlpatterns = [
    path('', views.HOME, name='home'),
    path('task_delete/<int:del_id>/',views.TASK_DELETE, name='task_delete'),
    path('task_update/<int:tas_id>/',views.TASK_UPDATE, name='task_update'),

]