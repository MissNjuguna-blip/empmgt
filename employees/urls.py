from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *


# create a router object
router = DefaultRouter()
router.register('departments', DepartmentViewSet)

urlpatterns=[
    path('', include(router.urls)),
    path('employees', EmployeesListCreateView.as_view()),
    path('employees/<int:pk>',EmployeeDetailView.as_view())
]