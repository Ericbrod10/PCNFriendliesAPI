from rest_framework import serializers
from .models import MyModel

class MyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['Unique_Identifier', 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref',  'ip', 'device_info']

class MyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['Unique_Identifier', 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref', 'open_or_close', 'opponent_team', 'opponent_manager', 'send_v_receive' ]
