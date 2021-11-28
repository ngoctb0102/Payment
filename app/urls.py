from django.urls import path
from . import views

urlpatterns = [
    path('',views.hello),
    path('choosePayment/',views.choosePaymentMethod),
    path('bankInputPage/',views.bankInputPage),
    path('InputAddressPage/',views.InputAddressPage,name = "InputAddressPage")
]