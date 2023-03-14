from rest_framework import serializers


class DebitorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    gender = serializers.CharField()
    age = serializers.IntegerField()
    is_good = serializers.BooleanField()
    birthday = serializers.DateTimeField()

