from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView
from django.views.decorators.csrf import csrf_exempt
from .serializers import MyGetSerializer, MyPostSerializer, MyUpdateSerializer
from rest_framework import viewsets
from .models import MyModel
from .models import MyModel
from django.utils import timezone
from rest_framework.response import Response
import secrets
import string
import json
from django.http import JsonResponse


class MyCreateView(CreateAPIView):
    queryset = MyModel.objects.all()
    serializer_class = MyPostSerializer

# class MyRetrieveView(RetrieveAPIView):
#     queryset = MyModel.objects.all()
#     serializer_class = MyGetSerializer
#     lookup_field = 'Unique_Identifier'

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.last_accessed = timezone.localtime(timezone.now()) # Update the last_accessed field
#         print(instance.last_accessed)
#         instance.save()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)

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


@csrf_exempt
def create_mymodel(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            serializer = MyPostSerializer(data=data)
            print(serializer)
            if serializer.is_valid():
                unique_id = secrets.token_urlsafe(64)
                print(unique_id)
                mymodel = serializer.save(Unique_Identifier=unique_id)
                return JsonResponse({'success': True, 'Unique_Identifier': mymodel.Unique_Identifier})
            else:
                return JsonResponse({'success': False, 'message': serializer.errors})
        except json.decoder.JSONDecodeError as e:
            return JsonResponse({'success': False, 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
