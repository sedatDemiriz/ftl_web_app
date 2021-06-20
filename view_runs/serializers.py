from master_db.models import User_Submitted_Run as Run
from rest_framework import serializers

class RunSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Run
        fields = [
            'datetime',
            # 'ship_used',
            'username',
            'difficulty',
            'result',
            'scrap_collected',
            'beacons_explored',
            'ships_defeated',
            'crew_hired',
            'score',
        ]