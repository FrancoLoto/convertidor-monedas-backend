from rest_framework import serializers

from .models import New


class NewSerializer(serializers.ModelSerializer):
    class Meta:
        model = New
        fields = (
            'title',
            'slug',
            'thumbernail',
            'content',
            'time_read',
            'created_at'
        )
