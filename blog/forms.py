from django import forms



class OrderForm(forms.Form):
    code_order = forms.CharField()
    description_order = forms.CharField()
    amaunt_order = forms.IntegerField()
    email = forms.CharField()
    phone = forms.CharField()


class OrderFormComf(forms.Form):

    amaunt_availble = forms.CharField()

class ContactForm(forms.Form):
    subject = forms.CharField(label='Тема', widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Текст', widget=forms.Textarea(attrs={'class':'form-control', "rows": 5}))

class SendBidForm(forms.Form):
    code_bid = forms.CharField()
    description_bid = forms.CharField()
    amaunt_bid = forms.IntegerField()
    email = forms.CharField(initial="nomail@nomail.com")
    phone = forms.CharField()