from rest_framework import serializers
from .models import MyModel

class MyPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = [ 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref',  'ip', 'device_info']

class MyGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ['Unique_Identifier', 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref', 'open_or_close', 'opponent_team', 'opponent_manager', 'send_v_receive', 'SuspendMessageSent' ]


class MyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('match_pref', 'player_pref')



class MyCloseModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = ('Unique_Identifier', 'open_or_close', 'Opponent_Unique_Identifier', 'match_pref', 'player_pref')