from django.urls import path

from main_app.views.base import IndexView



urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]

