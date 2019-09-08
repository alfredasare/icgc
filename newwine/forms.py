from django import forms
from .models import RegisteredMembers


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = RegisteredMembers
        fields = ['first_name', 'surname', 'email', 'gender', 'date_of_birth', 'course', 'year',
                  'hall_or_hostel', 'room', 'department', 'covenant_family', 'home_temple', 'phone']
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'surname': forms.TextInput(attrs={'placeholder': 'Surname'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'gender': forms.TextInput(attrs={'placeholder': 'Gender'}),
            'date_of_birth': forms.TextInput(attrs={'placeholder': 'Date of birth (mm/dd/yyyy)'}),
            'course': forms.TextInput(attrs={'placeholder': 'Course'}),
            'year': forms.TextInput(attrs={'placeholder': 'Year'}),
            'hall_or_hostel': forms.TextInput(attrs={'placeholder': 'Hall or Hostel'}),
            'room': forms.TextInput(attrs={'placeholder': 'Room'}),
            'department': forms.TextInput(attrs={'placeholder': 'Church Department'}),
            'covenant_family': forms.TextInput(attrs={'placeholder': 'Covenant Family'}),
            'home_temple': forms.TextInput(attrs={'placeholder': 'Home Temple'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone Number'}),
        }
