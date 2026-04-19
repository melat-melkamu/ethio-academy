from django import forms
from .models import Student
import re

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'grade', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Age'}),
            'grade': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Grade'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if not first_name.isalpha():
            raise forms.ValidationError("First name must contain letters only")
        return first_name.capitalize()  

    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if not last_name.isalpha():
            raise forms.ValidationError("Last name must contain letters only")
        return last_name.capitalize()

    
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 1:
            raise forms.ValidationError("Age must be a positive number")
        return age

    
    def clean_grade(self):
        grade = self.cleaned_data.get('grade')
        if not grade.isdigit():
            raise forms.ValidationError("Grade must be a number")
        return grade

    
    def clean_email(self):
        email = self.cleaned_data.get('email').lower() 
        return email

    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        age = cleaned_data.get("age")
        grade = cleaned_data.get("grade")
        email = cleaned_data.get("email")

        
        if Student.objects.filter(
            first_name=first_name,
            last_name=last_name,
            age=age,
            grade=grade,
            email=email
        ).exists():
            raise forms.ValidationError("This student is already registered with these exact details.")

        return cleaned_data