from rest_framework import serializers
from .models import Branch , Bank

class Serializer(serializers.ModelSerializer):
    bank = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Branch
        fields = ('ifsc','name', 'bank','address', 'city','district','state')
