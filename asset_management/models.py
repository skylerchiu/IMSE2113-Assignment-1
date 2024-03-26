from django.db import models

from django.utils import timezone

class LogMessage(models.Model):
    message = models.CharField(max_length=300)

    log_date = models.DateTimeField("date logged")
    
    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
    

class Asset(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=300, null = True, blank=True)
    assigned = models.BooleanField(default=False)
    registered_user = models.CharField(max_length=300, null = True, blank=True)
    checkout_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"



