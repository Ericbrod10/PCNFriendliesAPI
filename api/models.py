from django.db import models

class MyModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    Unique_Identifier = models.CharField(max_length=255, null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    player_name = models.CharField(max_length=125, null=True)
    team_name = models.CharField(max_length=125, null=True)
    team_league = models.CharField(max_length=2, null=True)
    player_numb = models.CharField(max_length=6, null=True)
    match_pref = models.CharField(max_length=15, null=True)
    player_pref = models.CharField(max_length=15, null=True)
    open_or_close = models.CharField(max_length=255, null=True, default="Open")
    opponent_team = models.CharField(max_length=255, null=True)
    opponent_manager = models.CharField(max_length=255, null=True)
    send_v_receive = models.CharField(max_length=255, null=True)
    ip = models.CharField(max_length=255, null=True)
    device_info = models.CharField(max_length=255,null=True)
    last_called = models.DateTimeField(auto_now=True)
    Opponent_Unique_Identifier = models.CharField(max_length=255, null=True)




