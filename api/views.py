from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import MyGetSerializer, MyPostSerializer, MyUpdateSerializer, MyCloseModelSerializer
from rest_framework import viewsets
from .models import MyModel
from .models import MyModel
from django.utils import timezone
from rest_framework.response import Response
import secrets
import string
import json
from django.http import JsonResponse
from django.db.models import Count
from rest_framework import status



# Post Route
class MyCreateView(CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyPostSerializer

# Get Route
class MyRetrieveView(RetrieveAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyGetSerializer
    lookup_field = 'Unique_Identifier'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.last_called = timezone.now() # Update the last_accessed field
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    
# Count Route
class MyModelCountView(APIView):
    def get(self, request, format=None):
        count = MyModel.objects.filter(open_or_close='Open').aggregate(count=Count('id'))['count']
        return Response({'count': count})

# Update Route
class MyUpdateView(UpdateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyUpdateSerializer
    lookup_field = 'Unique_Identifier'

    def patch(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            partial = kwargs.pop('partial', True)
            instance = self.get_object()
            instance.last_called = timezone.now()
            serializer = self.get_serializer(instance, data=data, partial=partial)
            if serializer.is_valid():
                unique_id = instance.Unique_Identifier
                serializer.save()
                return JsonResponse({'success': True, 'Unique_Identifier': unique_id})
            else:
                return JsonResponse({'success': False, 'message': serializer.errors})
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})


# Port Route
@csrf_exempt
def create_mymodel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = MyPostSerializer(data=data)
            if serializer.is_valid():
                unique_id = secrets.token_urlsafe(64)
                mymodel = serializer.save(Unique_Identifier=unique_id)
                return JsonResponse({'success': True, 'Unique_Identifier': mymodel.Unique_Identifier})
            else:
                return JsonResponse({'success': False, 'message': serializer.errors})
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})




class CloseMyModelView(APIView):
    def put(self, request, *args, **kwargs):
        unique_id = self.kwargs.get('Unique_Identifier')
        try:
            mymodel = MyModel.objects.get(Unique_Identifier=unique_id)
            if mymodel.Opponent_Unique_Identifier is not None:
                return Response({'message': 'Opponent Already Found Cannot Close Out'})
            else:
                mymodel.open_or_close = 'Closed'
                mymodel.save()
                serializer = MyCloseModelSerializer(mymodel)
                return Response(serializer.data, status=status.HTTP_200_OK)
        except MyModel.DoesNotExist:
            return Response({'message': 'Record Not Found.'})
        

class ResumeMyModelView(APIView):
    def put(self, request, *args, **kwargs):
        unique_id = self.kwargs.get('Unique_Identifier')
        try:
            mymodel = MyModel.objects.get(Unique_Identifier=unique_id)
            if mymodel.open_or_close == 'Suspended' and mymodel.SuspendMessageSent + timezone.timedelta(minutes=5) <= timezone.now():
                return Response({'message': 'Failed to Rejoin Queue, Passed 5 minutes'})
            elif mymodel.open_or_close == 'Suspended' and mymodel.SuspendMessageSent + timezone.timedelta(minutes=5) > timezone.now():
                mymodel.open_or_close = 'Open'
                mymodel.SuspendMessageSent = None
                mymodel.last_called = timezone.now()
                mymodel.save()
                serializer = MyGetSerializer(mymodel)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Record already closed'})
        except MyModel.DoesNotExist:
            return Response({'message': 'Record Not Found.'})