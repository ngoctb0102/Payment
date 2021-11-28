from django import forms
# import psycopg2
# conn = psycopg2.connect(database ="",  # input db info !!
#                             user = "",  
#                             password = "",  
#                             host = "",  
#                             port = "") #ket noi  toi database
# cur = conn.cursor()
# def getCityList():
#     cur.execute("select city,city from city group by city")
#     city = cur.fetchall()
#     return city
def getCityList():
    return (('1','Ha Noi'),('2','Thanh Hoa'),('3','Ninh Binh'),('4','Nghe An'),('5','Da Nang'))
# def getDistrictList(city):
#     cur.execute("select district,district from city where city = '%s'" % (city))
#     dis = cur.fetchall()
#     return dis
# def list(a):
#     if a == 'a':
#         return (('-','-'),('q','q'),('n','n'))
#     else:
#         return (('-','-'),('e','e'),('g','g'))
class choosePaymentMethodForms(forms.Form):
    CHOICES = [('cod', 'Thanh toán trực tiếp khi giao hàng\n\n'),
               ('bank', 'Thanh toán qua thẻ ngân hàng\n\n')]
    pay = forms.ChoiceField(label="Mời quý khách chọn phương thức thanh toán\n",
                            choices=CHOICES, widget=forms.RadioSelect)
    # a = forms.ChoiceField(label = "a",choices = (('a','a'),('b','b')))
    # b = forms.ChoiceField(label = "b",choices = list(a))



    def pays(self):
        payValue = self.cleaned_data['pay']
        if payValue is None:
            raise forms.ValidationError("Quý khách chưa chọn phương thức thanh toán")
        else:
            return self.cleaned_data['pay']
    # def init_b(self):
    #     a = self.cleaned_data['a']
    #     self.b = forms.ChoiceField(label = "b",choices = list(a))

class payInfoForm(forms.Form):
    name = forms.CharField(label = "Họ và tên", max_length = 50)
    phone = forms.CharField(label = "Số điện thoai", max_length = 10)
    city = forms.ChoiceField(label = "Thành Phố", choices = getCityList())
    add = forms.CharField(label = "Địa chỉ cụ thể", max_length = 100)
    def name(self):
        return self.cleaned_data['name']
    def phone(self):
        return self.cleaned_data['phone']
    def city(self):
        return self.cleaned_data['city']
    def add(self):
        return self.cleaned_data['add']

