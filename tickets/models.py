from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ticket(models.Model):
    
    DYNAX = 'DAX'
    DOTNET = 'Net'
    SQL = 'sql'
    DEVELOPMENT_CATEGORY = (
        (DYNAX, 'DynAX'),
        (DOTNET ,'DotNet'),
        (SQL, 'Sql')
    )

    OPEN_STATUS = 1
    REOPENED_STATUS = 2
    RESOLVED_STATUS = 3
    CLOSED_STATUS = 4
    DUPLICATE_STATUS = 5

    STATUS_CHOICES = (
        (OPEN_STATUS, 'Open'),
        (REOPENED_STATUS, 'Reopened'),
        (RESOLVED_STATUS, 'Resolved'),
        (CLOSED_STATUS, 'Closed'),
        (DUPLICATE_STATUS, 'Duplicate'),
    )

    PRIORITY_CHOICES = (
        (1, '1. Critical'),
        (2, '2. High'),
        (3, '3. Normal'),
        (4, '4. Low'),
        (5, '5. Very Low'),
    )

    title = models.CharField(max_length=60)
    description = models.TextField()
    user_assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=True)
    upd_date = models.DateField(auto_now=True)
    category = models.CharField(
        max_length=3,
        choices=DEVELOPMENT_CATEGORY,
        default=DYNAX,
    )
    status = models.IntegerField(
        'Status',
        choices=STATUS_CHOICES,
        default=OPEN_STATUS,
    )
    priority = models.IntegerField(
        'Priority',
        choices=PRIORITY_CHOICES,
        default=3,
        blank=3,
        help_text='1 = Highest Priority, 5 = Low Priority',
    )
    days_allocated = models.IntegerField(default=1)
    @property
    def sla(self):
        return (self.pub_date + timedelta(self.days_allocated)) - date.today()


    def __str__(self):
        return self.title


    class Meta:
        ordering = ('title', 'pub_date')
