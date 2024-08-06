from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    images = forms.ImageField(required=True, widget=forms.ClearableFileInput(attrs={'allow_multiple_selected': True}))  # Optional image field

    class Meta:
        model = Student
        fields = ['name', 'registration_id', 'branch']
        
