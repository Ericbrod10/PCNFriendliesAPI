from django.contrib import admin

# Register your models here.
from .models import MyModel

class FriendlyModelAdmin(admin.ModelAdmin):
    list_display = ( 'Unique_Identifier','datetime', 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref', 'open_or_close', 'opponent_team', 'opponent_manager', 'send_v_receive', 'ip', 'device_info','last_called','Opponent_Unique_Identifier')
    search_fields = ('id','Unique_Identifier','datetime', 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref', 'open_or_close', 'opponent_team', 'opponent_manager', 'send_v_receive', 'ip', 'device_info','Opponent_Unique_Identifier')
    list_editable = ( 'player_name', 'team_name', 'team_league', 'player_numb', 'match_pref', 'player_pref', 'open_or_close', 'opponent_team', 'opponent_manager', 'send_v_receive', 'ip', 'device_info','Opponent_Unique_Identifier')
    


admin.site.register(MyModel,FriendlyModelAdmin)
