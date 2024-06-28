from datetime import timezone
from django.db import models

from django.db import models
from django.utils import timezone

ITEM_CHOICES = [
    ('projector','Projector'),
    ('monitor','Monitor'),
    ('system unit','System Unit'),
    ('peripherals','Peripherals'),
]

DEPARTMENTS = [
    ('ceit','CEIT'),
    ('caba','CABA'),
    ('coed','COED'),
    ('bacta','BACTA'),
]

from django.db import models
from django.utils import timezone

DEPARTMENTS = [
    ('ceit', 'CEIT'),
    ('caba', 'CABA'),
    ('coed', 'COED'),
    ('bacta', 'BACTA'),
]

# Create your models here.


class Items(models.Model):
    item =  models.CharField(max_length=100, choices=ITEM_CHOICES, default='projector')
    number = models.CharField(max_length=100, default="")
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return self.item + ' no.' + self.number

class Borrow_History(models.Model):
    Borrower_Name = models.ForeignKey('Students', on_delete=models.CASCADE) #reference student table
    item = models.ForeignKey('Items', on_delete=models.CASCADE)  #reference item table
    Professor_Name = models.ForeignKey('Prof', on_delete=models.CASCADE)
    Room = models.CharField(max_length=100)
    Time_borrowed = models.DateTimeField(default=timezone.now)
    Time_returned = models.DateTimeField(null=True, blank=True)
    Exp_Time_Ret = models.TimeField(null=True) #expected time return
     

    def save(self, *args, **kwargs):
        self.Time_borrowed = timezone.now()
        super(Borrow_History, self).save(*args, **kwargs)

    def __str__(self):
         return f"{self.Borrower_Name} - {self.item} - Borrowed: {self.Time_borrowed}"


class Students (models.Model):
    Name = models.CharField(max_length=100, unique=True)
    course = models.CharField(max_length=100, choices=DEPARTMENTS, default='ceit')
    student_No = models.CharField(max_length=7, unique=True)
    RFID = models.CharField(max_length=10, null=True, unique=True)
    pic = models.ImageField(upload_to='selfies/', null=True)

    def __str__(self):
        return self.Name + "  : [" + self.RFID + ']'

class Prof (models.Model):
    Name = models.CharField(max_length=100)
    Department = models.CharField(max_length=100, choices=DEPARTMENTS, default='ceit')
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.Name