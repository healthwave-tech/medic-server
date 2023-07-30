from django.urls import path
import search.views as views

urlpatterns = [
    path('search/', views.get_doctors),
    path('search/doctor/', views.search_doctor),
]