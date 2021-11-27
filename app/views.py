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

    form = choosePaymentMethodForms()
    context['form'] = form
    if request.method == 'POST':
        print("a")
        form = choosePaymentMethodForms(request.POST)
        if form.is_valid():
            print("a")
            if form.pays() == 'bank' :
                print("!11")
                return render(request, 'BankInputPage.html', context)
            else:
                return render(request, 'InputAddressPage.html', context)
        else:
            print("Form invalid")

    return render(request, 'choosePayment.html', context)
def bankInputPage(request):
    return render(request,'BankInputPage.html')
def InputAddressPage(request):
    return render(request, 'InputAddressPage.htm')


