from django.urls import path
import users.views as views

urlpatterns = [
    path('user/signup/', views.create_user),
    path('user/login/', views.login_user),
    path('user/doctors/recent/', views.get_doctors),
]