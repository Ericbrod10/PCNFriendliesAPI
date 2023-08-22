from django.urls import path
from django.contrib import admin
from .views import MyCreateView,MyRetrieveView, create_mymodel, MyUpdateView, MyModelCountView,CloseMyModelView,ResumeMyModelView


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/myendpoint/', MyCreateView.as_view()),
    path('api/myendpoint/', create_mymodel),
    path('api/myendpoint/<str:Unique_Identifier>/', MyRetrieveView.as_view()),
    path('api/myendpoint/<str:Unique_Identifier>/update/', MyUpdateView.as_view()),
    path('api/myendpoint/<str:Unique_Identifier>/close/', CloseMyModelView.as_view()),
    path('api/myendpoint/<str:Unique_Identifier>/resume/', ResumeMyModelView.as_view()),
    path('api/opencount/', MyModelCountView.as_view()),
]
