from django.db import models
from django.contrib.auth.models import User

class TimerPreset(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    duration_seconds = models.IntegerField(default=60)
    # Barvu můžeme ukládat jako HEX kód, např. "#FF0000" pro červenou
    color_scheme = models.CharField(max_length=20, default="#FF0000")
    # Způsob konečné signalizace (blikání, pípání, atd.)
    signal_type = models.CharField(max_length=50, default="flash")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.duration_seconds}s) - {self.user.username}"

class MeasurementHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Pokud uživatel smaže preset, historii si chceme nechat, proto SET_NULL
    # preset = models.ForeignKey(TimerPreset, on_delete=models.SET_NULL, null=True, blank=True)
    preset = models.ForeignKey(TimerPreset, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Measurement by {self.user.username} at {self.started_at}"