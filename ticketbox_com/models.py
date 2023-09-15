from django.db import models



class TicketBoxEvent(models.Model):
    url = models.CharField(max_length=128)
    
