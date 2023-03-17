from django.urls import path
from django.contrib import admin
from .views import MyRetrieveView, create_mymodel, MyUpdateView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/myendpoint/', MyCreateView.as_view()),
    path('api/myendpoint/', create_mymodel),
    path('api/myendpoint/<str:Unique_Identifier>/', MyRetrieveView.as_view()),
    path('api/myendpoint/<str:Unique_Identifier>/update/', MyUpdateView.as_view()),
]
