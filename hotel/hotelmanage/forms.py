from django import forms

from .models import customer_reg_form


class CustomerRegistrationForm(forms.ModelForm):
    c_name = forms.CharField(required=True)
    c_address = forms.CharField(required=True)
    c_mail_id = forms.EmailField(required=True)
    c_mob_no = forms.CharField(required=True)
    c_username = forms.CharField(required=True)
    c_password = forms.CharField(required=True)

    class Meta:
        model = customer_reg_form
        fields = ['c_name', 'c_address', 'c_mail_id', 'c_mob_no', 'c_username', 'c_password']
