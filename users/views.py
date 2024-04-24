from rest_framework import views, status
from rest_framework.response import Response

from users import services


class UserAuthAPIView(views.APIView):

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


class UserVerificationAPIView(views.APIView):

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
