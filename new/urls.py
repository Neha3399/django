from django.urls import path

from new import views

urlpatterns = [
    path("test",views.test,name="test"),
    path("demo",views.demo,name="demo"),
    path("dash",views.dash,name="dash"),
    path("read",views.read,name="read")

]
