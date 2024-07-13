# from django.contrib import admin
from django.urls import path
from .views import sampleappview,ListClass,DetailClass,CreateClass,DeleteClass,UpdateClass

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('view/',sampleappview),
    path('list/',ListClass.as_view(), name ='list'),
    path('detail/<int:pk>',DetailClass.as_view(), name = 'detail'),
    path('create/',CreateClass.as_view() ,name= 'create'),
    path('delete/<int:pk>',DeleteClass.as_view(), name ='delete'),
    path('update/<int:pk>',UpdateClass.as_view(), name = 'update'),
    
]
