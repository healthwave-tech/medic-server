from django.urls import path
import appointments.views as views
urlpatterns = [
    path('appointments/', views.get_user_appointments),
    path('appointments/set/', views.set_appointment),
]