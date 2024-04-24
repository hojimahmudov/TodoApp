from django.urls import path, include
from .views import TodoListApiView, TodoDetailApiView, TodoViewSet, RetrieveDeleteItem, CreateListItems, \
    RetrieveUpdateDelete, ListAPIItem, MovieCreateItem
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api-viewset', TodoViewSet)

urlpatterns = [
    path('api/', TodoListApiView.as_view()),
    path('api/<int:todo_id>/', TodoDetailApiView.as_view()),
    path('', include(router.urls)),
    path('generic/<int:pk>/', RetrieveDeleteItem.as_view()),
    path('mixin/', CreateListItems.as_view()),
    path('mixin/<int:pk>/', RetrieveUpdateDelete.as_view()),
    path('concreate-view/', ListAPIItem.as_view()),
    path('movie/create/', MovieCreateItem.as_view())
]
