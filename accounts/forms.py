from django import forms

class update_profile(forms.Form):
      address = forms.CharField(max_length = 100)
      mobile_no = forms.CharField(max_length = 10)
