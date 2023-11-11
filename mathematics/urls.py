urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("mathematics.urls"))

    path('', views.home),
    path('hello/<name>/', views.return_name),
    path('mathematics/<operation>/<int:a>/<int:b>', views.calculator),
]
