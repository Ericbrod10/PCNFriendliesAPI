from django.urls import path
from .views import MyCreateView, MyRetrieveView
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/myendpoint/', MyCreateView.as_view()),
    path('api/myendpoint/<str:Unique_Identifier>/', MyRetrieveView.as_view()),
]
