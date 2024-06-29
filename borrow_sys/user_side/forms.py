from django import forms
from .models import Borrow_History, Students

class UserForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['Name', 'course', 'student_No','RFID', 'pic']


# forms.py


class BorrowHistoryForm(forms.ModelForm):
    class Meta:
        model = Borrow_History
        fields = ['Borrower_Name', 'Professor_Name', 'Room', 'item']
