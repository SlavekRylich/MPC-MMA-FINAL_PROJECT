from django.contrib import admin
from .models import TimerPreset, MeasurementHistory

# Registrace našich modelů do administrace
admin.site.register(TimerPreset)
admin.site.register(MeasurementHistory)