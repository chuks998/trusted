from django.db import models
import string, random
from django.utils import timezone

# id genarator
def id_genarator(length=7, var=string.ascii_uppercase + string.digits):
        return ''.join(random.choice(var) for _ in range(length))

def limit_day():
    var = timezone.now() + timezone.timedelta(days=7)
    return var


def next_day():
    num = 0
    while num < 22:
        var = timezone.now() + timezone.timedelta(days=num)
        if var != timezone.now() + timezone.timedelta(days=22):
            num += 1
            return num
        elif var == timezone.now() + timezone.timedelta(days=22):
            return 100

# Create your models here.
class PackageItem(models.Model):
    choice = {
        ('active', 'active'),
        ('pending', 'pending'),
        ('delayed', 'delayed'),
        ('waiting comfirmation', 'waiting comfirmation'),
    }
    # Client side
    tracking_number = models.CharField(unique=True ,blank=True, null=True, max_length=7, default=id_genarator)
    destination_name = models.CharField(max_length=50, help_text='enter the client full names')
    destination_email = models.CharField(max_length=50, help_text='enter the client email address', null=True)
    destination_phone = models.CharField(max_length=15, help_text='enter the client phone number')
    destination_address = models.CharField(max_length=50, help_text='enter the destination address')
    # Your side
    my_name = models.CharField(max_length=50, help_text='enter your name here')
    my_email = models.CharField(max_length=50, help_text='enter your email here')
    # package info
    content = models.CharField(max_length=100, default='i-Phone12, D&G Designers Hand Bag')
    date_pushed = models.DateField(default=timezone.now)
    delivery_date = models.DateField(default=limit_day)
    current_location = models.CharField(max_length=20)
    progress = models.IntegerField(default=next_day, blank=True, null=True)
    status = models.CharField(max_length=21, choices=choice ,default=3)

    def __str__(self):
        return self.destination_name
