import uuid
from django.db import models
from simple_history.models import HistoricalRecords


class Kolo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    owner = models.ForeignKey('authentication.User', related_name='ownner', on_delete=models.CASCADE)
    wallet_balance = models.DecimalField(decimal_places=2, max_digits=50)
    currency = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    log = HistoricalRecords()
    
    def __str__(self) -> str:
        return f"{self.owner.display_name} - {self.wallet_balance}"
    