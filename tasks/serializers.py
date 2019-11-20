# snippets/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers
from tasks.models import Task, LANGUAGE_CHOICES, STYLE_CHOICES


class TaskSerializer(serializers.HyperlinkedModelSerializer): # new
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField( # new
        view_name='task-highlight', format='html')

    class Meta:
        model = Task
        fields = ('url', 'id', 'highlight', 'title', 'description', 'linenos',
                  'language', 'style', 'owner',) # new


class UserSerializer(serializers.HyperlinkedModelSerializer): # new
    snippets = serializers.HyperlinkedRelatedField( # new
        many=True, view_name='task-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'tasks') # new