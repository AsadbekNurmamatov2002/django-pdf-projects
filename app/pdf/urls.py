from django.urls import path
from .views import Home, render_pdf_view


urlpatterns = [
    path('',Home),
    path('pdf/<int:pk>/', render_pdf_view, name='pdf'),
]
