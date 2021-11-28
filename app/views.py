from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import choosePaymentMethodForms,payInfoForm

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
        form = choosePaymentMethodForms(request.POST)
        if form.is_valid():
            if form.pays() == 'bank' :
                return render(request, 'BankInputPage.html', context)
            else:
                # return render(request, 'InputAddressPage.html')
                return redirect("InputAddressPage")
        else:
            print("Form invalid")

    return render(request, 'choosePayment.html', context)
def bankInputPage(request):
    return render(request,'BankInputPage.html')
def InputAddressPage(request):
    form = payInfoForm()
    context={
        'form' : form
    }
    if request.method == 'POST':
        form = payInfoForm(request.POST)
        if form.is_valid():
            return render(request, 'result.html',{'name':form.cleaned_data['name'],'phone':form.cleaned_data['phone'],'city':form.cleaned_data['city'],'add':form.cleaned_data['add']})
    return render(request, 'InputAddressPage.html',context)



