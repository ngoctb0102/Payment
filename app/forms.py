from django import forms

class choosePaymentMethodForms(forms.Form):
    CHOICES = [('cod', 'Thanh toán trực tiếp khi giao hàng\n\n'),
               ('bank', 'Thanh toán qua thẻ ngân hàng\n\n')]
    pay = forms.ChoiceField(label="Mời quý khách chọn phương thức thanh toán\n",
                            choices=CHOICES, widget=forms.RadioSelect)

    def pays(self):
        payValue = self.cleaned_data['pay']
        if payValue is None:
            raise forms.ValidationError("Quý khách chưa chọn phương thức thanh toán")
        else:
            return self.cleaned_data['pay']