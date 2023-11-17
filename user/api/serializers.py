from rest_framework import serializers

from django.contrib.auth import get_user_model, login, authenticate

from rest_framework.exceptions import ValidationError, AuthenticationFailed, ErrorDetail

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "phone", "password",]

class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(
        label=("Password1"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    password2 = serializers.CharField(
        label=("Password2"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )
    class Meta:
        model = User
        fields = ['username', "email", "password1", "password2", "phone"]
        extra_kwargs = {
            'password': {"write_only" : True}
        }

    def create(self, validated_data):
        password1 = validated_data.pop("password1", None)
        password2 = validated_data.pop("password2", None)
        if password1 == password2:
            instance = self.Meta.model(**validated_data)
            if password1 and password2 is not None:
                instance.set_password(password1)
            else:
                raise ErrorDetail
            instance.save()
        else:
            raise ErrorDetail  
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        max_length=128,
        write_only=True
    )

    class Meta:
        model = User
        fileds = ["email", "password"]

    def validate(self, data):
        email = data["email"]
        password = data["password"]
        if email and password :
            
            try:
                username = User.objects.get(email=email)
                user = authenticate(request=self.context.get('request'), username=username.username, password=password)
            except:
                user = None
            if user is not None:
                login(self.context.get('request'), user)
            else:
                raise AuthenticationFailed
        else:
            raise AuthenticationFailed

        data['user'] = user
        return data
