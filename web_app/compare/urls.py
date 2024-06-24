from django.urls import path
from compare import views

urlpatterns = [
    path("", views.home, name="home"),
    path("visu/", views.visu_data, name="visu"),
    path("visu/detail/<id>", views.detail, name="detail"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("add/", views.insert_data, name="insert"),
    path("info/", views.info, name="info"),
    path("constraints/", views.constraints, name="constraints"),
    path("visu/detail/modify/<id>", views.modify, name="modify"),
    path("generate_plot/", views.generate_plot, name="plot")
    ]