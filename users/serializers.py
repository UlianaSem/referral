from rest_framework import serializers

from users import models


class UserProfileSerializer(serializers.ModelSerializer):
    users = serializers.SerializerMethodField()

    class Meta:
        model = models.User
        fields = [
            'phone',
            'own_code',
            'entered_code',
            'users'
        ]

    @staticmethod
    def get_users(instance):
        return [user.phone for user in
                models.User.objects.filter(entered_code=instance.own_code)]


class UserCodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            'entered_code',
        ]


class UserAuthSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            'phone'
        ]


class UserVerificationSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4)

    class Meta:
        model = models.User
        fields = [
            'phone',
            'code',
        ]


class ResponseAuthSerializer(serializers.Serializer):
    status = serializers.IntegerField()
    message = serializers.CharField()


class ResponseCodeSerializer(ResponseAuthSerializer):
    token = serializers.CharField()
