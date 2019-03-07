from django import forms
from . import models


class SaleForm(forms.ModelForm):
    location_type = forms.ChoiceField(choices=[('rural', 'rural'), ('urban', 'urban')], widget=forms.Select(attrs={
        'class': "form-control", 'label': "Location type"
    }))
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Females')], widget=forms.Select(attrs={
        'class': "form-control", 'label': "Gender"
    }))
    vehicle_color = forms.ChoiceField(
        choices=[('red', 'red'), ('green', 'green'), ('blue', 'blue'), ('white', 'white'), ('black', 'black')],
        widget=forms.Select(attrs={
            'class': "form-control", 'label': "Vehicle color"
        }))
    vehicle_type = forms.ChoiceField(choices=[('scooter', 'scooter'), ('motorcycle', 'motorcycle'), ('moped', 'moped'),
                                              ('threewheeler', 'threewheeler')], widget=forms.Select(attrs={
        'class': "form-control", 'label': "Vehicle type"
    }))
    mode_known = forms.ChoiceField(choices=[('newspaper', 'newspaper'), ('tvad', 'tvad'), ('melas', 'melas'),
                                            ('exchangeoffers', 'exchangeoffers'), ('other', 'other')],
                                   widget=forms.Select(attrs={
                                       'class': "form-control", 'label': "Mode known"
                                   }))

    class Meta:
        model = models.Sale
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Name"
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Mobile number",
            }),
            'location': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Location",
            }),
            'age': forms.NumberInput(attrs={
                'class': "form-control", 'placeholder': "Age",
            }),
            'vehicle_name': forms.TextInput(attrs={
                'class': "form-control", 'placeholder': "Vehicle name",
            }),
        }
