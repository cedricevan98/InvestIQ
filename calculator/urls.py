from django.urls import path
from . import views

app_name = 'calculator'

urlpatterns = [
    path('', views.index, name='index'),
    path('compound/', views.compound, name='compound'),
    path('sip/', views.sip, name='sip'),
    path('cagr/', views.cagr, name='cagr'),
    path('roi/', views.roi, name='roi'),
    path('emi/', views.emi, name='emi'),
    path('swp/', views.swp, name='swp'),
]
