from django import forms
from .models import Borrow_History, Students

class UserForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['Name', 'course', 'student_No','RFID', 'pic']


class BorrowHistoryForm(forms.ModelForm):
    class Meta:
        model = Borrow_History
        fields = ['Borrower_Name', 'item', 'Professor_Name', 'Room', 'Exp_Time_Ret']
        widgets = {
            'Exp_Time_Ret': forms.TimeInput(attrs={'type': 'time'}),
        }