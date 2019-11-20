# snippets/views.py
from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new

from .models import Task
from .permissions import IsOwnerOrReadOnly
from .serializers import TaskSerializer, UserSerializer


@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        # 'users': reverse('user-list', request=request, format=format),
        'tasks': reverse('task-list', request=request, format=format)
    })


class TaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new

    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new


class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class TaskHighlight(generics.GenericAPIView): # new
    queryset = Task.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)