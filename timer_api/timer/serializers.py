from rest_framework import serializers
from .models import TimerPreset, MeasurementHistory

class TimerPresetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimerPreset
        fields = '__all__'  # Vezme všechna pole z modelu (name, duration, color atd.)

class MeasurementHistorySerializer(serializers.ModelSerializer):
    # Tento řádek řekne Djangu, aby se podívalo do propojeného modelu Preset a vytáhlo pole 'name'
    preset_name = serializers.ReadOnlyField(source='preset.name')

    class Meta:
        model = MeasurementHistory
        fields = ['id', 'user', 'preset', 'preset_name', 'started_at', 'completed']