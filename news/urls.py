from django.urls import path

from .views import NewsListView, NewDetailView

urlpatterns = [
    path('', NewsListView.as_view()),
    path('<str:slug>/', NewDetailView.as_view()),
]
