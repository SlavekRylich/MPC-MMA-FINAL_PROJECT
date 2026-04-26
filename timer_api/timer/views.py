from rest_framework import viewsets
from .models import TimerPreset, MeasurementHistory
from .serializers import TimerPresetSerializer, MeasurementHistorySerializer

class TimerPresetViewSet(viewsets.ModelViewSet):
    queryset = TimerPreset.objects.all()
    serializer_class = TimerPresetSerializer

    def get_queryset(self):
        # Nejdřív vezmeme všechny záznamy
        queryset = super().get_queryset()
        # Podíváme se, jestli v URL přišel parametr 'user' (např. /api/presets/?user=2)
        user_id = self.request.query_params.get('user')
        
        if user_id is not None:
            # Pokud ano, vyfiltrujeme to jen na tohoto uživatele
            queryset = queryset.filter(user_id=user_id)
            
        return queryset

class MeasurementHistoryViewSet(viewsets.ModelViewSet):
    queryset = MeasurementHistory.objects.all()
    serializer_class = MeasurementHistorySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user')
        
        if user_id is not None:
            queryset = queryset.filter(user_id=user_id)
            
        return queryset