from django.urls import path , include
from . import views
urlpatterns = [
    path('',views.api),
    path('employeelist/',views.employeelist),
    path('employee/<str:pk>/',views.employee),
    path('create-employee/',views.create_employee),
    path('update-employee/<str:pk>/',views.update_employee),
    path('delete-employee/<str:pk>/',views.delete_employee),

]
