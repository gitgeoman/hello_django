
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello),
    path('hello', views.return_name),
    path('hello/<name>/', views.return_name),

    path('mathematics/<operation>/<int:a>/<int:b>', views.calculator),
]
