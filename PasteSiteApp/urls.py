from django.urls import path

from PasteSiteApp import views

urlpatterns = [
    path('', views.paste),
    path('detail/<id>/', views.detail),
    path('save/', views.paste_save)
]