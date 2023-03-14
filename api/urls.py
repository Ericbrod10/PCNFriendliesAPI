from django.urls import path
from .views import MyCreateView, MyRetrieveView, create_mymodel
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/myendpoint/', MyCreateView.as_view()),
    path('api/myendpoint/', create_mymodel),
    path('api/myendpoint/<str:Unique_Identifier>/', MyRetrieveView.as_view()),
]
