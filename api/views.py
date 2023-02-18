from rest_framework.generics import CreateAPIView, RetrieveAPIView
from .models import MyModel
from .serializers import MyGetSerializer, MyPostSerializer
from rest_framework import viewsets
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MyModel
from django.utils import timezone
from rest_framework.response import Response


class MyCreateView(CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyPostSerializer

class MyRetrieveView(RetrieveAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyGetSerializer
    lookup_field = 'Unique_Identifier'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.last_accessed = timezone.now() # Update the last_accessed field
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


@csrf_exempt
def create_mymodel(request):
    if request.method == 'POST':
        data = request.POST
        mymodel = MyModel.objects.create(
            Unique_Idenitier=data.get('Unique_Identifier'),
            player_name=data.get('player_name'),
            team_name=data.get('team_name'),
            team_league=data.get('team_league'),
            player_numb=data.get('player_numb'),
            match_pref=data.get('match_pref'),
            player_pref=data.get('player_pref'),
            open_or_close=None,
            opponent_team=None,
            send_v_receive=None,
            ip=data.get('ip'),
            device_info=None
        )
        return JsonResponse({'success': True, 'id': mymodel.id})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


