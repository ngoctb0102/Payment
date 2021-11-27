from django.shortcuts import render
from django.http import HttpResponse
from .forms import choosePaymentMethodForms

def hello(request):
    context = {
        "greet": "Hello",
        "age": 10
    }
    return render(request, 'hello.html', context)

def choosePaymentMethod(request):
    context = {
        "money" : 500000,
        "customerName": "Tuan Vu"
    }

    emptyForm = choosePaymentMethodForms()
    context['form'] = emptyForm
    if request.method == 'POST':
        form = choosePaymentMethodForms(request.POST)
        if form.is_valid():
            print(" form.pays() == ", form.pays())
            if form.pays() == 'bank' :
                return render(request, 'BankInputPage.html', context)
            else:
                return render(request, 'InputAddressPage.html', context)
        else:
            print("Form invalid")

    return render(request, 'choosePayment.html', context)


