from django.urls import path
from myprojects import views

urlpatterns = [
    path("", views.myproject_index, name="myproject_index"),
    path("<int:pk>/", views.myproject_detail, name="myproject_detail"),
]