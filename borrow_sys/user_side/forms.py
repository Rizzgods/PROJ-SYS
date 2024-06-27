from django import forms
from .models import Students

class UserForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['Name', 'course', 'student_No','RFID', 'pic']
