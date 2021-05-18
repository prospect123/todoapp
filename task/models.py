from django.db import models

class TODO(models.Model):
    task = models.TextField(null=True)
    task_name = models.CharField(max_length=30,null=True,blank=False)
    date = models.DateField(auto_now=True)
    last_date = models.DateTimeField(null=True)

    
class HELLO(models.Model):
    task = models.TextField(null=True)
 

