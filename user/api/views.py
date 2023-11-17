from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import login, get_user_model

from .serializers import RegisterSerializer, LoginSerializer

import datetime, jwt

User = get_user_model()

class RegiterUserView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = request.data
        user = User.objects.filter(username=data["username"]).first()
        if user and user.check_password(data["password"]):
            login(request, user)
            # payload = {
            #     "id": user.id,
            #     "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            #     "iat": datetime.datetime.utcnow()
            # }
            # token = jwt.encode(payload, "secret", algorithm="HS256")
            # response = Response()
            # response.set_cookie(key="jwt", value=token, httponly=True)
            # response.data = {
            #     "jwt": token
            # }
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response({"message":"Can not register"}, status=status.HTTP_404_NOT_FOUND)




class LoginUserView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user is None:
            return Response({"Login": "Faild"})

        # payload = {
        #     "id": user.id,
        #     "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     "iat": datetime.datetime.utcnow()
        # }
        # token = jwt.encode(payload, "secret", algorithm="HS256")
        # response = Response()
        # response.set_cookie(key="jwt", value=token, httponly=True)
        # response.data = {
        #     "jwt": token
        # }
        # return response
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    # def get(self, request):
    #     token = request.COOKIES.get("jwt")
    #     if not token:
    #         raise AuthenticationFailed("Unauthentication")
    #     try:
    #         payload = jwt.decode(token, "secret", algorithms=["HS256"])
    #     except jwt.ExpiredSignatureError:
    #         raise AuthenticationFailed("Unauthentication")
    #     user = User.objects.filter(id=payload['id']).first()
    #     serializer = RegisterSerializer(user)
    #     return Response(serializer.data)
