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
# Create your models here.
class Items(models.Model):
    item =  models.CharField(max_length=100, choices=ITEM_CHOICES, default='projector')
    number = models.CharField(max_length=100, default="")
    
    def __str__(self):
        return self.item + ' no.' + self.number


DEPARTMENTS = [
    ('ceit','CEIT'),
    ('caba','CABA'),
    ('coed','COED'),
    ('bacta','BACTA'),
]



# models.py

from django.db import models
from django.utils import timezone

DEPARTMENTS = [
    ('ceit', 'CEIT'),
    ('caba', 'CABA'),
    ('coed', 'COED'),
    ('bacta', 'BACTA'),
]

class Borrow_History(models.Model):
    Borrower_Name = models.CharField(max_length=100)
    item = models.ForeignKey('Items', on_delete=models.CASCADE)  # Make sure 'Items' is defined elsewhere
    Professor_Name = models.CharField(max_length=100)
    department = models.CharField(max_length=100, choices=DEPARTMENTS, default='ceit')
    Room = models.CharField(max_length=100)
    Time_borrowed = models.DateTimeField(default=timezone.now)
    Time_returned = models.DateTimeField(null=True, blank=True)
    Borrower_Selfie = models.ImageField(upload_to='selfies/')  # Specify an upload directory

    def save(self, *args, **kwargs):
        self.Time_borrowed = timezone.now()
        super(Borrow_History, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.Borrower_Name} - {str(self.item)}'
