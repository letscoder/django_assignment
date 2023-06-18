from django.db import models
class Issue(models.Model):
    issueID=models.CharField(max_length=50)
    userID=models.CharField(max_length=50)
    location=models.TextField()
    problem=models.TextField()
    time=models.TimeField()
    STATUS_CHOICES = [
        ('INQUEUE', 'INQUEUE'),
        ('ASSIGNED', 'ASSIGNED'),
        ('DISPATCHED', 'DISPATCHED'),
    ]

    Status=models.CharField(max_length=50,choices=STATUS_CHOICES)
class Agents(models.Model):
    AgentID=models.CharField(max_length=50)
    Queue=models.IntegerField()

class Mechanic(models.Model):
    mechanicID=models.CharField(max_length=50)
    availability=models.BooleanField(default=True)
    

       