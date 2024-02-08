from django.urls import path

from .views import ConvertCurrencyView, CurrencyListView

urlpatterns = [
    path('convert/<str:from_currency>/<str:to_currency>/<str:amount>/',
         ConvertCurrencyView.as_view(), name="convert_currency"),
    path('currencies/', CurrencyListView.as_view(), name="currency_list"),
]
