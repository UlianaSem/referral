from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import views, status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users import services, serializers, models


@extend_schema(tags=["Регистрация/ авторизация по номеру телефона"])
class UserAuthAPIView(views.APIView):

    @extend_schema(
        summary="Авторизоваться по номеру телефона: "
                "получить проверочный код на телефон",
        request=serializers.UserAuthSerializer,
        responses={
            200: serializers.ResponseAuthSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')

        if phone is None:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Phone field mandatory'
            })

        auth = services.AuthUser(phone)
        response = auth.get_code()

        return Response(response)


@extend_schema(tags=["Регистрация/ авторизация по номеру телефона"])
class UserVerificationAPIView(views.APIView):

    @extend_schema(
        summary="Авторизоваться по номеру телефона: "
                "верифицировать проверочный код и получить токен авторизации",
        request=serializers.UserVerificationSerializer,
        responses={
            200: serializers.ResponseCodeSerializer,
        }
    )
    def post(self, request, *args, **kwargs):
        phone = request.data.get('phone')
        code = request.data.get('code')

        if phone is None or code is None:
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Phone and code fields mandatory'
            })

        auth = services.AuthUser(phone)
        response = auth.check_code(code)

        return Response(response)


@extend_schema(tags=["Профиль"])
@extend_schema_view(
    retrive=extend_schema(
        summary="Получить профиль пользователя",
    ),
)
class UserProfileRetrieveAPIView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(pk=self.request.user.pk)


@extend_schema(tags=["Профиль"])
@extend_schema_view(
    update=extend_schema(
        summary="Добавить инвайт-код",
    ),
)
class UserCodeAPIView(generics.UpdateAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserCodeSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        if instance.entered_code:
            return Response({
                'status': status.HTTP_409_CONFLICT,
                'message': 'Code already entered'
            })

        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)

        code = serializer.validated_data.get('entered_code')
        if instance.own_code == code:
            return Response({
                'status': status.HTTP_409_CONFLICT,
                'message': "It's your code"
            })

        if not models.User.objects.filter(own_code=code).exists():
            return Response({
                'status': status.HTTP_400_BAD_REQUEST,
                'message': 'Code not exists'
            })

        self.perform_update(serializer)
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
