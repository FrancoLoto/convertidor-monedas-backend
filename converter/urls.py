from django.urls import path

from .views import ConvertCurrencyView, CurrencyListView

urlpatterns = [
    # Endpoint for the ConvertCurrencyView
    path('convert/<str:from_currency>/<str:to_currency>/<str:amount>/',
         ConvertCurrencyView.as_view(), name="convert_currency"),

    # Endpoint for the CurrencyListView
    path('currencies/', CurrencyListView.as_view(), name="currency_list"),
]
