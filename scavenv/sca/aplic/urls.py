from django.urls import path
from . import views

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]
urlpatterns = [
    path("", views.index, name="index"),
]
