from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import status

from django.contrib.auth import login, get_user_model

from .serializers import (RegisterSerializer, 
                          LoginSerializer, 
                          UserProfileSerializer, 
                          ChangePasswordSerilizer
                          )

# import datetime, jwt

User = get_user_model()


class RegiterUserView(APIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = request.data
        user = User.objects.filter(username=data["username"]).first()
        if user and user.check_password(data["password1"]):
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        else:
            return Response(
                {"message":"Can not register"}, 
                status=status.HTTP_404_NOT_FOUND
                )


class LoginUserView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        if user is None:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.data, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        if request.user.is_authenticated:
            return Response(self.serializer_class(request.user).data)
        else:
            return Response(
                {"message":"Unauthenticated"}, 
                status=status.HTTP_203_NON_AUTHORITATIVE_INFORMATION
                )


class ChangePasswordView(UpdateAPIView):
    serializer_class = ChangePasswordSerilizer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def put(self, request):
        if request.user.is_authenticated:
            serilizer = self.serializer_class(
                data=request.data, 
                context={"request":request}
                )
            serilizer.is_valid(raise_exception=True)
            serilizer.update(
                instance=User.objects.get(id=request.user.id), 
                validated_data=request.data
                )
            return Response({"message":"success"})



class ProfileUserView(UpdateAPIView):
    serializer_class = UserProfileSerializer
    
    def put(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(
                User.objects.filter(id=request.user.id).first(), 
                data=request.data
                )
            serializer.is_valid(raise_exception=True)
            serializer.update(
                instance=User.objects.filter(id=request.user.id).first(), 
                validated_data=request.data
                )
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(
                {"message":"error"}, 
                status=status.HTTP_400_BAD_REQUEST
                )

    def get(self, request):
        if request.user.is_authenticated:
            user = User.objects.filter(id=request.user.id).first()
            serializer = self.serializer_class(user)
            return Response(serializer.data, status=status.HTTP_200_OK)