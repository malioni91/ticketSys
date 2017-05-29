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
    title = models.CharField(max_length=60)
    description = models.TextField()
    user_assigned = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateField(auto_now_add=False)
    upd_date = models.DateField(auto_now=False)
    category = models.CharField(
        max_length=3,
        choices=DEVELOPMENT_CATEGORY,
        default=DYNAX,
    )
    status = models.BooleanField()
    days_allocated = models.IntegerField(default=1)

    def __str__(self):
        return self.title